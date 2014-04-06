from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def home(request):
    return render_to_response("home.html", {}, context_instance=RequestContext(request))

def analyst(request):
    return render_to_response("analyst.html", {}, context_instance=RequestContext(request))

def search(request):
    return render_to_response("search/search.html", {}, context_instance=RequestContext(request))