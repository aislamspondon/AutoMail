from account.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    event_count = serializers.SerializerMethodField(read_only=True)
    group_event = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ['id', 'full_name', 'profile_pic', 'username','email', 'group_event', 'event_count', 'phone_number', 'created', 'updated']
    
