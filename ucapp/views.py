import json
import datetime
from django.db.models import Avg
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from forms import ResendActivationEmailForm
from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery
from ucapp.forms import AnalystReviewForm
from ucapp.utils import add_new_review_to_analyst, add_new_review_to_analyst_firm
from models import Analyst, AnalystFirm, AnalystReview, AnalystRatingText, AnalystRating, Specialization
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from li_registration.models import UserProfile
import random

from hashlib import sha1 as sha_constructor
from django.contrib.sites.models import RequestSite



# Create your views here.
def home(request):
    analysts = Analyst.objects.all()[0:4]
    return render(request, "home.html", {'analysts': analysts})


def analyst_details(request, analyst_id):
    analyst = Analyst.objects.get(pk=analyst_id)
    reviews = AnalystReview.objects.all().filter(analyst=analyst).order_by("-time_created")
    ratingsAvg = AnalystRating.objects.all().filter(review__analyst=analyst).values('text').annotate(
        average_rating=Avg('rating'))
    for i in range(len(ratingsAvg)):
        ratingsAvg[i]['text'] = AnalystRatingText.objects.get(pk=int(ratingsAvg[i]['text']))
    return render(request, "analyst_details.html", {'analyst': analyst, 'reviews': reviews, 'ratingsAvg': ratingsAvg})


def analyst_firm_details(request, analyst_firm_id):
    analyst_firm = AnalystFirm.objects.get(pk=analyst_firm_id)
    reviews = AnalystReview.objects.all().filter(analyst__analyst_firm=analyst_firm).order_by("-time_created")
    return render(request, "analyst_firm_details.html", {'analyst_firm': analyst_firm, 'reviews': reviews})


def ajax_search(request):
    #if request.is_ajax():
    search_data = {}
    found_entries = SearchQuerySet()
    if ('query' in request.GET) and request.GET['query'].strip():
        query_string = request.GET['query']
        found_entries = SearchQuerySet().filter(
            content=AutoQuery(query_string)
        )

    # Sorting Results by Model
    analysts = found_entries.models(Analyst)
    analyst_firms = found_entries.models(AnalystFirm)

    if ('sort' in request.GET) and request.GET['sort'].strip():
        sort = request.GET['sort']
        if sort == 'best_rating':
            analysts = analysts.order_by('-average_rating')
            analyst_firms = analyst_firms.order_by('-average_rating')
        elif sort == 'most_reviewed':
            analysts = analysts.order_by('-num_reviews')
            analyst_firms = analyst_firms.order_by('-num_reviews')

    if ('specialization' in request.GET) and request.GET['specialization'].strip():
        specialization = request.GET['specialization'] # this is a PK of the specialization object
        if specialization != 'All':
            analysts = analysts.filter(specializations__contains=specialization)

    search_data['analysts'] = analysts
    search_data['analyst_firms'] = analyst_firms

    pages = {}

    # Creating HTML Templates for each search
    analyst_page = render(request, 'search/analysts.html', search_data)
    analyst_firm_page = render(request, 'search/analyst_firms.html', search_data)

    pages['analyst_page'] = str(analyst_page.content)
    pages['analyst_firm_page'] = str(analyst_firm_page.content)
    pages['analyst_number'] = analysts.count()
    pages['analyst_firm_number'] = analyst_firms.count()

    data = json.dumps(pages)
    return HttpResponse(data, content_type='application/json')


def analyst(request):
    analysts = Analyst.objects.all()[0:10]
    return render(request, "analyst.html", {'analysts': analysts})


def search(request):
    data = {}
    data['specializations'] = Specialization.objects.all()
    if "query" in request.GET:
        data["query"] = request.GET["query"];
    return render(request, "search/search.html", data)


def analyst_firm(request):
    analyst_firms = AnalystFirm.objects.all()[0:10]
    return render(request, "analyst_firm.html", {'analyst_firms': analyst_firms})


def pr_agency(request):
    analysts = Analyst.objects.all()
    return render(request, "pr_agency.html", {'analysts': analysts})


@login_required
def write_review(request):
    if request.method == "GET":
        form = AnalystReviewForm()
        rating_texts = AnalystRatingText.objects.all()
        analysts = Analyst.objects.all()
        return render(request, "write_review.html", {'rating_texts': rating_texts, 'analysts': analysts, 'form': form})
    else:

        return process_review(request, request.POST['analyst_id'])


@login_required
def review_analyst(request, analyst_id):
    analyst = Analyst.objects.get(id=analyst_id)
    if request.method == "GET":
        form = AnalystReviewForm()
        rating_texts = AnalystRatingText.objects.all()

        data = {'form': form, 'rating_texts': rating_texts, 'analyst': analyst}
        return render(request, "review_analyst/review_analyst.html", data)
    elif request.method == "POST":
        return process_review(request, analyst_id)


def process_review(request, analyst_id):
    analyst = Analyst.objects.get(id=analyst_id)
    form = AnalystReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.author = request.user
        review.analyst = analyst
        review.save()
    else: #throw error handler
        rating_texts = AnalystRatingText.objects.all()

        data = {'form': form, 'rating_texts': rating_texts, 'analyst': analyst}
        return render(request, "review_analyst/review_analyst.html", data)

    for rating_text in AnalystRatingText.objects.all():
        rating = request.POST['rating-text-' + str(rating_text.id)]
        analyst_rating = AnalystRating.objects.create(review=review, text=rating_text, rating=int(rating))

    add_new_review_to_analyst(analyst, review)
    add_new_review_to_analyst_firm(analyst.analyst_firm, review)

    return redirect(analyst)

def resend_activation_email(request):
    form = None
    if request.method == 'POST':
        form = ResendActivationEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            users = User.objects.filter(email=email, is_active=0)

            if not users.count():
                form._errors["email"] = (_("Account for email address is not registered or already activated."),)

            for user in users:
                for profile in UserProfile.objects.filter(user=user):
                    # need to write this
                    if profile.activation_key_expired():
                        salt = sha_constructor(str(random())).hexdigest()[:5]
                        profile.activation_key = sha_constructor(salt+user.username).hexdigest()
                        user.date_joined = datetime.now()
                        user.save()
                        profile.save()

                    site = RequestSite(request)

                    # need to write this also
                    profile.send_activation_email(site)
                    return render(request, "registration/resend_activation_email_done.html", {"form" : form})

    if not form:
        form = ResendActivationEmailForm()

    return render(request, "registration/resend_activation_email_form.html", {"form" : form})
