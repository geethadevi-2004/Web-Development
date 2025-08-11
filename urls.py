from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('build/', views.build_resume, name='build_resume'),
    path('preview/<int:resume_id>/', views.preview_resume, name='preview_resume'),
    
]
