from django.shortcuts import render
from django.http import HttpResponse
from models import Course


def course(request):
    course_list = Course.objects
    context_dict = {}
    context_dict['courses'] = course_list
    return render(request, 'ga_courses/course.html', context=context_dict)
