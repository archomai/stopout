from django.http import HttpResponse
from django.shortcuts import render

from .models import Webtoon, Episode


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


def webtoon_detail(request, episode_id):

    episodes = Episode.objects.get(pk=episode_id)
    context = {
        'episodes': episodes,
    }
    return render(
        request=request,
        template_name='webtoon_detail.html',
        context=context,
    )
