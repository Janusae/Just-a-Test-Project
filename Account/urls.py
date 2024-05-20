from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
urlpatterns = [
    path("dashboard" , views.dashboard, name="dashboard"),
    path("Edit/Dashboard" , views.Edit_DashboardView.as_view() , name="edit_dashboard"),
    path("login" , auth_views.LoginView.as_view() , name = "login") ,
    path("register" , views.RegisterView.as_view() , name = "Register")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
