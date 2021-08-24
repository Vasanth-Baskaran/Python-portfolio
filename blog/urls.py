from django.urls import path
from blog import views

app_name="blog"
urlpatterns = [
    path('', views.all_blogs_list, name="all_blogs_list"),
    #path('<int:pk>', views.detail_view, name="detail_view"),
]