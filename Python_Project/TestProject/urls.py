from django.urls import path
from . import views   #important . this after one space need rule 

app_name = 'Python_Project'

urlpatterns = [
    path("", views.index, name="index"),
    # path("details", views.details, name="details"),
    path("details/<int:details_id>", views.details, name="details"), #Dynamic URL values 
    
    path("new_url", views.new_url_view, name="new_page_url"),
    path("old_url", views.old_url_redirect, name="old_url"),
]