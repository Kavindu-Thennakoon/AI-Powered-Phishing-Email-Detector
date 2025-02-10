from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('analyze/', views.analyze_email_ajax, name='analyze_email_ajax'),

]