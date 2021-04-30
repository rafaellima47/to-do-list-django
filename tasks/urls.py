from django.urls import path

from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("delete/<int:pk>", views.delete, name="delete"),
	path("update/<int:pk>", views.update, name="update"),
	path("complete/<int:pk>", views.complete, name="complete"),
	path("not_complete/<int:pk>", views.not_complete, name="not_complete"),
	path("clear", views.clear, name="clear")
]