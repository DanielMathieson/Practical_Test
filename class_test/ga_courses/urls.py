from django.urls import path
import views as v

app_name = 'ga_courses'

urlpatterns = [
path('', v.course, name='course'),

]
