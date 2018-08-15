from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name='first_app2'),
    url(r'^a$', views.index2, name='firt_app2'),
    url(r'^g$', views.index0, name='first_app0'),
]
