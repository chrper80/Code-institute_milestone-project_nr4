from django.urls import path
from . import views


urlpatterns = [
    path('success', views.success, name="success"),
    path('cancel', views.CancelView.as_view()),
    path('create_checkout_session', views.create_checkout_session,
         name="create_checkout_session"),
]
