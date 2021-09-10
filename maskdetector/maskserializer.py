
from rest_framework import serializers



class MaskSerializer(serializers.Serializer):
    image = serializers.CharField()
    
    class Meta:
        fields = ('image')