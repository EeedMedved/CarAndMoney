from django.urls import path

from . import views
from .views import CreateRefillView

urlpatterns = [
    path('add', CreateRefillView.as_view(), name='refill_add'),
    path('', views.refill_list, name='refill_list')
]