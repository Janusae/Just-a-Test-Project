from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path("dashboard" , views.dashboard, name="dashboard"),
    path("Edit/Dashboard" , views.Edit_DashboardView.as_view() , name="edit_dashboard")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
