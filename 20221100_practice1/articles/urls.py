from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
]
