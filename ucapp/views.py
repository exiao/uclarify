from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery, Clean
from haystack.models import SearchResult
from ucapp.forms import AnalystReviewForm

from models import Analyst, AnalystFirm, AnalystReview, AnalystRatingText, AnalystRating
import json

# Create your views here.
def home(request):
    return render(request, "home.html", {})

def analyst_details(request, analyst_id):
    analyst = Analyst.objects.get(pk=analyst_id)
    reviews = AnalystReview.objects.all().filter(analyst=analyst)
    return render(request, "analyst_details.html", {'analyst': analyst, 'reviews': reviews})

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
    analysts = Analyst.objects.all()
    return render(request, "analyst.html", {'analysts': analysts})

def search(request):
    data = {}
    if "query" in request.GET:
        data["query"] = request.GET["query"];
    return render(request, "search/search.html", data)

def analyst_firm(request):
    analyst_firms = AnalystFirm.objects.all()
    return render(request, "analyst_firm.html", {'analyst_firms': analyst_firms})

def pr_agency(request):
    analysts = Analyst.objects.all()
    return render(request, "pr_agency.html", {'analysts': analysts})

def review_analyst(request, analyst_id):
    analyst = Analyst.objects.get(id=analyst_id)
    if request.method == "GET":
        form = AnalystReviewForm()
        rating_texts = AnalystRatingText.objects.all()

        data = {'form': form, 'rating_texts': rating_texts, 'analyst': analyst}
        return render(request, "review_analyst/review_analyst.html", data)
    elif request.method == "POST":
        form = AnalystReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.analyst = analyst
            review.save()

        for rating_text in AnalystRatingText.objects.all():
            rating = request.POST['rating-text-' + str(rating_text.id)]
            analyst_rating = AnalystRating.objects.create(review=review, text=rating_text, rating=int(rating))



        return render(request, "home.html", {})

#helper function to update analyst summary
def update_analyst(analyst, analyst_review):
    return None