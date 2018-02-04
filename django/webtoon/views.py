from django.http import HttpResponse
from django.shortcuts import render

from .models import Webtoon, Episode


def webtoon_list(request):

    webtoon = Webtoon.objects.all()
    context = {
        'webtoon': webtoon,
    }
    return render(
        request=request,
        template_name='blog/post_list.html',
        context=context,
    )


def webtoon_detail(request, episode_id):

    episode = Episode.objects.get(pk=episode_id)
    context = {
        'episode': episode,
    }
    return render(
        request=request,
        context=context,
    )
