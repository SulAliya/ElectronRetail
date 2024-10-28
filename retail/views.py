from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from retail.models import Network, Contacts, Product
from retail.serializers import NetworkSerializer, ContactsSerializer, ProductSerializer
from users.permissions import IsActive


class NetworkViewSet(ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    filterset_fields = ['country',]
    permission_classes = [IsActive]


class ContactsCreateAPIView(CreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactsListAPIView(ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    filterset_fields = ['city',]


class ContactsRetrieveAPIView(RetrieveAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactsUpdateAPIView(UpdateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactsDestroyAPIView(DestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
