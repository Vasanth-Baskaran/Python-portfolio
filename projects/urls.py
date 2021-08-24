from django.urls import path
from projects import views

app_name="projects"
urlpatterns = [
    path('', views.all_project_list, name="all_project_list"),
    path('<int:pk>', views.detail_view, name="detail_view"),
]