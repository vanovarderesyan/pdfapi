from rest_framework import serializers

class UploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    class Meta:
        fields = ['file']