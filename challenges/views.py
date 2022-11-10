from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "No meat for a whole month",
    "february": "Walk for at least 10 minutes",
    "march": "drink a lot of water",
    "april": "No meat for a whole month",
    "may": "Walk for at least 10 minutes",
    "june": "drink a lot of water",
    "july": "No meat for a whole month",
    "august": "Walk for at least 10 minutes",
    "september": "drink a lot of water",
    "october": "No meat for a whole month",
    "november": "Walk for at least 10 minutes",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def challenges_int(request, month):
    month_number = list(monthly_challenges.keys())

    if month > len(month_number):
        return HttpResponseNotFound("<h2>Invalid month number, please enter in range of (1-12)</h2>")

    redirect_month = month_number[month - 1]  # reverse
    redirect_path = reverse("string_challenge", args=[redirect_month])                         # challenges path
    return HttpResponseRedirect(redirect_path)


def challenges_class(request, month):
    try:
        challenge_text = monthly_challenges[month]                   # render
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404()
