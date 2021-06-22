from django.urls import path
from .views import home, CityDetailView, CityCreateView, CityUpdateView, CityDeleteView, CityListView

urlpatterns = [
    path('add/', CityCreateView.as_view(), name='add'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
    # path('', home, name='home'),
    path('', CityListView.as_view(), name='home'),
    # path('<int:pk>/', CityDetailView.as_view(), name='home'),
]
