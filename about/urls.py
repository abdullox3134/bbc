from django.urls import path

from about.views import AboutListView, aboutdetail


urlpatterns = [
    path('about/', AboutListView.as_view(), name='about-list'),
    path('about/<int:pk>/', aboutdetail, name='about-detail'),
]
