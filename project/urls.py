from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view, name = "home"),
    path("add/", add_view, name = "add"),
    path("update/<str:id>", update_view, name="update"),
    path("delete/<str:id>", delete_view, name="delete")
]
