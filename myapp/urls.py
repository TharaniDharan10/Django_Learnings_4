from django.urls import path
from . import views
urlpatterns = [

    path("list/", views.display),
    path("display/", views.select, name="select"),
    path('update/<int:id>',views.update, name='update')
]
