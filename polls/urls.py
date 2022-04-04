from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView 

from .views import *

app_name = 'polls'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', QuestionDetailView.as_view(), name='detail'),
    path('<int:pk>/results/', QuestionResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('accounts/login/', LoginView.as_view()),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("<int:pk>/profile/", ProfileUpdateView.as_view(), name="profile"),
    # path("accounts/success", SuccessView.as_view(), name="success"),
]