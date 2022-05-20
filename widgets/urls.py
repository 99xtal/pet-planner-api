from django.urls import path
from widgets import views

urlpatterns =[
    path('', views.UserWidgetList.as_view()),
    path('<int:pk>/', views.WidgetDetail.as_view())
]