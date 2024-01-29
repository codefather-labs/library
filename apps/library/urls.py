from django.conf.urls import url

from apps.library import views

urlpatterns = [
    # url(r'^author/([a-A][z-Z])/$', views.get_author_by_name, name='home')
    url(r'', views.index, name='index'),
    url('author/(?P<name>[\w.@+-]+)/', views.get_author_by_name, name='get_author_by_name')
]
