from django.shortcuts import render
from django_app.models import Post



# Create your views here.
def post_list(request):
    return render(request, 'post_list.html',)

