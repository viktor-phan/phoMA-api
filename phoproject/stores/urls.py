from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns = [
    path('', views.PhoPlaceListAPIView.as_view(), name='phoplace_list'),
    path('<int:id>/', views.PhoPlaceRetrieveView.as_view(), name='phoplace_detail'),
    path('create/', views.PhoPlaceCreateAPIView.as_view(), name='phoplace_create'),
    path('update/<int:id>/', views.PhoPlaceRetrieveUpdateView.as_view(),
         name='phoplace_update'),
    path('delete/<int:id>/', views.PhoPlaceDeleteView.as_view(), name='pholace_delete')
]
