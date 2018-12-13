from rest_framework import serializers


class JandiSerializer(serializers.Serializer):
    body = serializers.CharField()
    connectColor = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    connectInfo = serializers.JSONField(required=False)
