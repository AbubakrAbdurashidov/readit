from django.urls import path
from .views import (
    article_list_view,
    article_detail_view,
)

app_name = 'article'

urlpatterns = [
    path('list/', article_list_view, name='list'),
    path('detail/<slug:slug>/', article_detail_view, name='detail'),
]
