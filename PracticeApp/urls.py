from django.urls import path
from PracticeApp import views


urlpatterns=[
    path('',views.index,name='my_index'),
    path('about/',views.about,name='my_about'),
    path('contact/',views.contact,name='my_contacts'),
    path('blog/',views.blog,name='my_blog'),
    path('services/',views.services,name='my_services'),
]