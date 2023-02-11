from django.urls import path

from bank_app.api import views


urlpatterns = [
    path('banklist/', views.BankList.as_view()),
    path('<int:pk>/branchlist/', views.BranchList.as_view()),
]
