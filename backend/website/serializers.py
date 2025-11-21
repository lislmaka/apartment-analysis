from rest_framework import serializers
from website.models import Avito


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avito
        fields = [
            "id",
            "title",
            "rating_all",
            "rating_house",
            "rating_flat",
            "rating_infrastructure",
            "price",
            "url",
            "address",
            "kolichestvo_komnat",
            "obshchaya_ploshchad",
            "district",
            "god_postroyki",
            "kapremont_date",
            "etazh_val",
            "etazh_count",
            "kapremont_diff",
            "is_new_lift",
        ]