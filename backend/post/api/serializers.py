from rest_framework.serializers import ModelSerializer
from ..models import post
class PostSerializers(ModelSerializer):
    class Meta:
        model = post
        fields = ('id', 'title', 'body')