from django.http import HttpResponse
from django.shortcuts import render

from .models import Webtoon


def webtoon_list(request):

    webtoons = Webtoon.objects.all()
    context = {
        'webtoons': webtoons,
    }
    return render(
        request=request,
        template_name='webtoon_list.html',
        context=context,
    )


def webtoon_detail(request, pk):

    webtoon = Webtoon.objects.get(pk=pk)
    webtoon.get_episode_list()
    context = {
        'webtoon': webtoon,
    }
    return render(
        request=request,
        template_name='webtoon_detail.html',
        context=context,
    )
