from rest_framework import serializers
from website.models import Avito


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avito
        fields = [
            "id",
            "title",
            "url",
            "address",
            "price",
            "kolichestvo_komnat",
            "obshchaya_ploshchad",
            "god_postroyki",
            "kapremont_date",
            "etazh_val",
            "etazh_count"
        ]
