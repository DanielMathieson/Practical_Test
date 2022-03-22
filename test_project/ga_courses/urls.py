from django.urls import path
from ga_courses import views

app_name = 'ga_courses'

urlpatterns = [
path('', views.course, name='course'),

]
