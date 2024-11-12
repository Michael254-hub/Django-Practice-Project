from django.urls import path
from PracticeApp import views


urlpatterns=[
    path('',views.index,name='my_index'),
    path('about/',views.about,name='my_about'),
    path('why/',views.why,name='my_why'),
    path('team/',views.team,name='my_team'),
    path('service/',views.service,name='my_service'),

]