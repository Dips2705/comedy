from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('profile/', views.profile, name='profile'),
    path('shows/', views.shows, name='shows'),
    re_path(r'^details(?:/(?P<show_id>[0-9]+))?/$', views.details, name='details'),
    path('submitreview/',views.submitreview,name='submitreview'),

    re_path(r'^profile/(?P<comedian_id>\d+)(?:/(?P<page_no>[0-9]+))?/$',views.profile,name='profile'),
    re_path(r'^shows(?:/(?P<page_no>[0-9]+))?/$', views.shows, name='shows'),

]
