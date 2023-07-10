from django.urls import path
from . import views

app_name = 'mysite'

urlpatterns = [
            path('', views.resume_list, name='resume_list'),
            path('/list/', views.list, name='list'),
            path('<int:id2>', views.resume_detail, name='resume_detail'),
            # path('/invite/', views.invitation, name='invitation'),
            path('/invite/', views.invitation, name='invitation'),

            ]
