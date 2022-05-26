from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from urllib import request
from bs4 import BeautifulSoup


# Create your views here.
def index(HttpRequest):
    return render(HttpRequest, "ARI_app/index.html")


def compute(HttpRequest):
    """Gives applicable reading level for designated text"""
    # 4.71(chars/words) + 0.5(words/setences) - 21.43 rounding up to full number#

    ari_scale = {
        1: {"ages": "5-6", "grade_level": "Kindergarten"},
        2: {"ages": "6-7", "grade_level": "1st Grade"},
        3: {"ages": "7-8", "grade_level": "2nd Grade"},
        4: {"ages": "8-9", "grade_level": "3rd Grade"},
        5: {"ages": "9-10", "grade_level": "4th Grade"},
        6: {"ages": "10-11", "grade_level": "5th Grade"},
        7: {"ages": "11-12", "grade_level": "6th Grade"},
        8: {"ages": "12-13", "grade_level": "7th Grade"},
        9: {"ages": "13-14", "grade_level": "8th Grade"},
        10: {"ages": "14-15", "grade_level": "9th Grade"},
        11: {"ages": "15-16", "grade_level": "10th Grade"},
        12: {"ages": "16-17", "grade_level": "11th Grade"},
        13: {"ages": "17-18", "grade_level": "12th Grade"},
        14: {"ages": "18-22", "grade_level": "College"},
    }

    dog = HttpRequest.POST.get("url")

    response = request.urlopen(dog)
    raw = response.read()

    # Copied from https://stackoverflow.com/questions/35956045/extract-title-with-beautifulsoup
    # Returns title of book
    soup = BeautifulSoup(raw, "html.parser")
    book_title = soup.title.string
    # ------------------------------------#

    text = raw.decode("utf-8-sig")

    # Get number of characters
    chars = len(text.replace(" ", ""))

    # Get number of words
    words = len(text.split())

    # Get number of sentences
    sentences = int(text.count(".") + text.count("?") + text.count("!"))

    # Get ARI level
    x = round((chars / words) * 4.71 + (words / sentences) * 0.5 - 21.43)
    if x > 14:
        x = 14

    grade_level = ari_scale[x]["grade_level"]
    age = ari_scale[x]["ages"]

    context = {"book_title": book_title, "x": x, "grade_level": grade_level, "age": age}

    # Return ARI level with text
    return render(HttpRequest, "ARI_app/result.html", context)
