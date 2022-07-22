from django.urls import path
from .views import *

urlpatterns =[
    path("", getRoutes, name='routes'),
    path("notes/", NotesView.as_view(), name='notes'),
    path("notes/create/", CreateView.as_view(), name='create-note'),
    path("notes/<str:pk>/update/", UpdateView.as_view(), name='update-note'),
    path("notes/<str:pk>/delete/", DeleteView.as_view(), name='delete-note'),
    path("notes/<str:pk>/", NoteView.as_view(), name='note'),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("changepassword/", UserChangePasswordView.as_view(), name="changepassword"),
    path("resetemail/", SendPasswordResetEmailView.as_view(), name="resetemail"),
    path("resetpassword/<uid>/<token>/", UserPasswordResetView.as_view(), name="resetpassword"),
]