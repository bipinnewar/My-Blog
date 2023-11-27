from django.shortcuts import render, get_object_or_404

from App.models import Post
from django.views import generic

# Create your views here.
class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'index.html'


class DetailView(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'
  

# def post_list(request):
#     posts = Post.objects.filter(status=1).order_by('-created_on')
#     return render(request, 'index.html', {'posts': posts})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'post_detail.html', {'object': post})
