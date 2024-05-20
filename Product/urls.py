from django.urls import path
from . import views
urlpatterns = [
    path("" , views.ProductView.as_view() , name = "List_Product"),
    path("Search-Tag/<str:tag>" , views.Search_Tag , name = "Search_Tag"),
    path("Detail/<int:pk>/<str:name>" , views.Detail_Product , name = "Detail_Product"),
]