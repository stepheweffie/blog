from django.shortcuts import render
from django.utils import timezone
from django_app.models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print('---- posts ----')
    print(posts)
    print(Post.objects.all())
    print(timezone.now())
    return render(request, 'post_list.html', {'posts': posts})