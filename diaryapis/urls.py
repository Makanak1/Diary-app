from django.urls import path
from  . import views

urlpatterns = [
    path('diaries/',views.DiaryView.as_view()),
    path('diaries/<str:id>/',views.DiaryDetailView.as_view()),
    path('register/',views.RegisterUserView.as_view()),
    path('login/',views.LoginUserView.as_view()),
    path('logout/',views.LogoutUserView.as_view()),
]