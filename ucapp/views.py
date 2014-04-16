from django.core import serializers
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse

from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery, Clean
from haystack.models import SearchResult

from models import Analyst
import json

# Create your views here.
def home(request):
    return render(request, "home.html", {})

def analyst_details(request, analyst_id):
    analyst = Analyst.objects.get(pk=analyst_id)
    return render(request, 'analyst_details.html', {'analyst': analyst})

def ajax_search(request):
    #if request.is_ajax():
    search_data = {}
    found_entries = SearchQuerySet()
    if ('searchText' in request.GET) and request.GET['searchText'].strip():
        query_string = request.GET['searchText']
        found_entries = SearchQuerySet().filter(
            content=AutoQuery(query_string)
        )
    search_data['found_entries'] = found_entries

    print(found_entries)
    pages = {}
    analyst_page = render(request, 'ajax_analyst.html', search_data)
    #analyst_firm_page = render(request, 'ajax_analyst_firm.html', search_data)
    print(analyst_page)
    pages['analyst_page'] = str(analyst_page.content)
    #pages['analyst_firm_page'] = analyst_firm_page
    data = json.dumps(pages)
    return HttpResponse(data, content_type='application/json')

def analyst(request):
    analysts = Analyst.objects.all()
    return render(request, "analyst.html", {'analysts': analysts})

def search(request):
    return render(request, "search/search.html", {})

def analyst_firm(request):
    analysts = Analyst.objects.all()
    return render(request, "analyst_firm.html", {'analysts': analysts})

def pr_agency(request):
    analysts = Analyst.objects.all()
    return render(request, "pr_agency.html", {'analysts': analysts})

def analyst_firm(request):
    analysts = Analyst.objects.all()
    return render(request, "analyst_firm.html", {'analysts': analysts})

def pr_agency(request):
    analysts = Analyst.objects.all()
    return render(request, "pr_agency.html", {'analysts': analysts})
