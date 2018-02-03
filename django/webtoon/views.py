from django.http import HttpResponse
from django.shortcuts import render

from .models import Webtoon


def webtoon_list(request):
    return HttpResponse('list')


def webtoon_detail(request, pk):
    return HttpResponse('detail')
