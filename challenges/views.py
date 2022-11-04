from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

monthly_challenges = {
    "january": "Walk at least 10 000 steps a day.",
    "february": "Don't eat meat for a month.",
    "march": "Drink 1,5 l of water every day.",
    "april": "Celebrate your birthday!",
    "may": "Read four books",
    "june": "Exercise every day for 30 minutes.",
    "july": "Talk to your cat 15 minutes/day.",
    "august": "Find a reason why to smile",
    "september": "Write 1 A4 every day.",
    "october": "Learn Django for 1 hour every day.",
    "november": "Slither",
    "december": "Meditate 15 min/day after and before going to bed",
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month :P")
    redirect_month = months[month - 1]

    # creates path /challenges/month
    redirect_path = reverse("month-challenge", args=[redirect_month])
    # return HttpResponseRedirect("/challenges/" + redirect_month)
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month_name": month},
        )

    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
