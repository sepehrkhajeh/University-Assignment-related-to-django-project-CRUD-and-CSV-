from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('uploadfile/', views.upload_file, name='upload'),
    path('delete/<int:pk>/', views.delete_item, name='del'),
    path('updatedata/<int:pk>/', views.update_item, name='update'),
    path('addnewitem/', views.AddNewItemView.as_view(), name='add_item'),
    path('search/', views.SearchView.as_view(), name='search'),
]
