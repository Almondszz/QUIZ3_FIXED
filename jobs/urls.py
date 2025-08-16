from django.urls import path
from . import views
from .views import job_apply
urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<int:pk>/', views.job_detail, name='job_detail'),
    path('<int:pk>/update/', views.JobUpdateView.as_view(), name='job_update'),
    path('<int:pk>/delete/', views.JobDeleteView.as_view(), name='job_delete'),
    path('<int:pk>/apply/', job_apply, name='job_apply'),
    path('create/', views.create_job, name='create_job'),
]