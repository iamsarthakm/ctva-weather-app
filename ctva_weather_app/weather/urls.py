from django.urls import path

from . import views

urlpatterns = [
    # path("supervisor", views.Supervisor.as_view()),
    # path("farmer", views.Farmer.as_view()),
    # path("extension-worker", views.ExtensionWorker.as_view()),
    path("<int:id>", verify_auth_token(views.Partner.as_view())),
]
