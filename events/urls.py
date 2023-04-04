from django.urls import path
from events import views

urlpatterns = [
    path("", views.UserEventList.as_view()),
    path("<int:pk>/", views.EventDetail.as_view()),
    path("categories/", views.EventCategoryList.as_view()),
]
