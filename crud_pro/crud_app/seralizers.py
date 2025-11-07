from rest_framework import serializers
from .models import deploy_data

class DeploySerializer(serializers.ModelSerializer):
    class Meta:
        model = deploy_data
        fields = '__all__'