from django.urls import path

from .views import PersonAPIView, PersonAllAPIView

urlpatterns = [
    path(
        "persons", PersonAllAPIView.as_view(),
    ), path(
        "persons/<int:pk>", PersonAPIView.as_view(),
    )
]
