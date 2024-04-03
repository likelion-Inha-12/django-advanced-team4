from django.shortcuts import render

from django.http import HttpResponse


def member(request):
    return HttpResponse("member server ok!")