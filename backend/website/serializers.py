from rest_framework import serializers
from website.models import Avito


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avito
        fields = ("title", "url", "address")