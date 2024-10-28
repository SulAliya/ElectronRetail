
from rest_framework.serializers import ModelSerializer

from retail.models import Network, Contacts, Product


class NetworkSerializer(ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'


class ContactsSerializer(ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
