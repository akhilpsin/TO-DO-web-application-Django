from . import views
from django.urls import path

#name spacing

urlpatterns = [
    path('',views.home,name="home"),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:taskid>/', views.update, name='update'),
    #class based just for learning purposes
    path('class_home/',views.Tasklistview.as_view(),name='class_home'),
    path('class_detail/<int:pk>/', views.TaskDetailview.as_view(),name='class_detail'),
    path('class_update/<int:pk>/', views.TaskUpdateview.as_view(),name='class_update'),
    path('class_delete/<int:pk>/', views.TaskDeleteview.as_view(),name='class_delete'),

]
