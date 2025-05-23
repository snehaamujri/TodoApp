from django.contrib import admin
from django.urls import path, include
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel here
    path('todos/', include('todo.urls')),
    path('login/', views.login_view, name='login'),
    path('', include('todo.urls')),
  
]
