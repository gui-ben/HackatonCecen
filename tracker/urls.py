from django.conf.urls import url

from . import views

urlpatterns = [
   
    url(r'^$', views.HomePage, name='index'),
    # ex: /rejected/something/
    url(r'^task/(?P<what>[\w-]+)/$', views.Pending, name='detail'),
	url(r'^new-task',views.NewTask,name='create new task'),
]