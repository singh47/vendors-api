from django.urls import path

from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('get_expired', views.get_expired.as_view(), name='get_expired'),
    path('get_categories', views.get_categories.as_view(), name='get_categories'),
    path('load_data', views.load_data.as_view(), name='load_data'),
]
