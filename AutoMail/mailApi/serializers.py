from rest_framework import serializers


class MailSerializer(serializers.Serializer):
    missing_mail = serializers.CharField()