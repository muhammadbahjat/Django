from django.urls import path

from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),

    path('(?P<question_id>[0-9]+)/detail$', views.detail, name="detail"),

    path('(?P<question_id>[0-9]+)/vote$', views.vote, name="vote"),

]
