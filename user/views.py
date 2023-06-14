from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def what_are_my_permissions(request):
    return HttpResponse('hello world!!!')