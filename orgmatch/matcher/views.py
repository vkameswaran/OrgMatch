from django.shortcuts import render
from .utils.matching import *

# Create your views here.

def index(request):
    context = {
        "interests": "",
    }
    if ("interests" in request.GET and request.GET["interests"]):
        # TODO: Check if I need to clean this input
        interests = request.GET["interests"].replace(",", "").replace("  ", " ").strip().split(" ")
        context["results"] = get_results(rank_against_keywords(interests), 10)
        context["empty"] = context["results"].size == 0
        context["interests"] = request.GET["interests"]
    return render(request, 'matcher/index.html', context=context)
