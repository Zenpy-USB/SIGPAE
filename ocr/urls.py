from django.conf.urls import url

from . import views

app_name = 'ocr'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^borradores$', views.borradores, name='borradores'),
]
