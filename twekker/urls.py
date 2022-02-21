from tweets.views import home_view, tweet_detail_view, tweet_list_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('tweets', tweet_list_view),
    path('tweets/<int:tweet_id>', tweet_detail_view),

]
