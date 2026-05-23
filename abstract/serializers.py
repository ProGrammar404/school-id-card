from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class BaseModelSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"


class BaseOwnerModelSerializer(BaseModelSerializer):
    def create(self, validated_data):
        request = self.context.get("request")

        if not request or not hasattr(request, "user") or not request.user.is_authenticated:
            raise serializers.ValidationError("User must be authenticated to create an object.")

        validated_data["created_by"] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get("request")

        if not request or not hasattr(request, "user") or not request.user.is_authenticated:
            raise serializers.ValidationError("User must be authenticated to update an object.")

        validated_data["updated_by"] = request.user
        return super().update(instance, validated_data)
