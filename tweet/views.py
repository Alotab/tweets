from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .models import Tweet

# Create your views here.


def home_view(request):
    return render(request, 'tweet/home.html', {})



def tweet_detail_view(request, id):

    data = {
        "id": id,
      
    }
    status = 200
    try:
        obj = Tweet.objects.get(pk=id)
        data['content'] = obj.content
        
    except:
        data['message'] = "Not found"
        status = 404

    queryset = get_object_or_404(Tweet, pk=id)
    return JsonResponse(data, status=status)