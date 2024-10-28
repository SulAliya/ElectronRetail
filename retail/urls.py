from django.urls import path
from rest_framework.routers import SimpleRouter

from retail.views import NetworkViewSet, ContactsCreateAPIView, ContactsListAPIView, ContactsRetrieveAPIView, \
    ContactsUpdateAPIView, ContactsDestroyAPIView, ProductListAPIView, ProductCreateAPIView, ProductRetrieveAPIView, \
    ProductUpdateAPIView, ProductDestroyAPIView
from retail.apps import RetailConfig

app_name = RetailConfig.name

router = SimpleRouter()
router.register("", NetworkViewSet)


urlpatterns = [
    path("contacts/", ContactsListAPIView.as_view()),
    path("contacts/create/", ContactsCreateAPIView.as_view()),
    path("contacts/<int:pk>/", ContactsRetrieveAPIView.as_view()),
    path("contacts/<int:pk>/update/", ContactsUpdateAPIView.as_view()),
    path("contacts/<int:pk>/delete/", ContactsDestroyAPIView.as_view()),
    path("product/", ProductListAPIView.as_view()),
    path("product/create/", ProductCreateAPIView.as_view()),
    path("product/<int:pk>/", ProductRetrieveAPIView.as_view()),
    path("product/<int:pk>/update/", ProductUpdateAPIView.as_view()),
    path("product/<int:pk>/delete/", ProductDestroyAPIView.as_view()),

]

urlpatterns += router.urls
