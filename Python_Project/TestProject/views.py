from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    return HttpResponse("hello world ")

# def details(request):
#     return HttpResponse(" See yoyr second /Page ")


def details(request , details_id):
    return HttpResponse(f" See yoyr second /Page ID is {details_id} ")

def old_url_redirect(request):
    return redirect(reverse("Python_Project:new_page_url"))

def new_url_view(request):
    return HttpResponse("this is the new URL")


