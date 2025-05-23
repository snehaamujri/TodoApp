from django.urls import path

from todo import views

urlpatterns = [
    path('',views.todos, name='todos'),
    path('<int:pk>/', views.todo, name='todo'),
    path('delete/<int:id>/', views.delete_todo, name='delete_todo'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('todos/', views.todos, name='todos'),
    path('logout/', views.logout_view, name='logout'),
    
]