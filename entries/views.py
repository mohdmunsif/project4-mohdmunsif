from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("FINAL PROJECT TOYS")


def submit(request):
    return HttpResponse("FINAL PROJECT TOYS - submission URL")


def browse(request):
    return HttpResponse("FINAL PROJECT TOYS - browse URL")
