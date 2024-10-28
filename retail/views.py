from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from retail.models import Network, Contacts, Product
from retail.serializers import NetworkSerializer, ContactsSerializer, ProductSerializer


class NetworkViewSet(ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class ContactsCreateAPIView(CreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactsListAPIView(ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


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
