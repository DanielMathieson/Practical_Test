from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from models import Course


def course(request):
    course_list = Course.objects.get()
    context_dict = {}
    context_dict['courses'] = course_list
    return render(request, 'ga_courses/course.html', context=context_dict)
