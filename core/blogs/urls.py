from django.urls import path
from django.views.generic import TemplateView, RedirectView
from . import views

from .views import indexView

urlpatterns = [
    path('fbv-index', views.indexView, name='fbv-test'),
    # path('cbv-index/', TemplateView.as_view(template_name='index.html', extra_context={"name":"Kiyan"}), name='cbv-index'),
    path('cbv-index', views.IndexView.as_view(), name='cbv-test'),
    path('digikala.com', RedirectView.as_view(url='https://digikala.com/', permanent=True)),
    path('post/', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]