from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "basepage/home.html", )

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id":x.id, "content":x.content} for x in qs]
    data = {
        "isUser": False,
        "response":tweets_list

    }

    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
        #"image_path": obj.image.url,
    }

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
    except:
        data["message"] = "Not Found"
        status = 404

    return JsonResponse(data, status=status)
