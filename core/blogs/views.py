from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.
def indexView(request):

    """
    function based view
    """
    context = {"name": "Kiyan"}
    return render(request, 'index.html', context)

class IndexView(TemplateView):
    """
    class based view
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['name'] = 'Kiyan'
        return context


class PostList(ListView):
    # queryset = Post.objects.all()
    model = Post
    context_object_name = 'posts'
    ordering = ['-id']

class PostDetail(DetailView):
    model = Post