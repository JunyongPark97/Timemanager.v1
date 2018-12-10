from rest_framework import serializers


class CSVSerializer(serializers.Serializer):
    csv = serializers.FileField()

    # def create(self, validated_data):

class UserSerializer(serializers.Serializer):
    csv = serializers.FileField()
