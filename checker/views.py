from django.shortcuts import render
from django.http import HttpResponse
# importing datetime module
import datetime
# Create your views here.

def index(request):
    return HttpResponse("the site is working,try newyear in url and see what happens :D")


def checker(request):
    now = datetime.datetime.now()
    return render(request,"index.html",{
    # or comment from now and set to True to see what happens
    "newyear": now.day == 1 and now.month == 1
    })
