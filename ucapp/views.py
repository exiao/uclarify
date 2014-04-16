from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Analyst

# Create your views here.
def home(request):
    return render_to_response("home.html", {}, context_instance=RequestContext(request))

def analyst(request):
    analysts = Analyst.objects.all()
    return render_to_response("analyst.html", {'analysts': analysts}, context_instance=RequestContext(request))

def search(request):
    return render_to_response("search/search.html", {}, context_instance=RequestContext(request))

def analyst_firm(request):
    analysts = Analyst.objects.all()
    return render_to_response("analyst_firm.html", {'analysts': analysts}, context_instance=RequestContext(request))

def pr_agency(request):
    analysts = Analyst.objects.all()
    return render_to_response("pr_agency.html", {'analysts': analysts}, context_instance=RequestContext(request))
