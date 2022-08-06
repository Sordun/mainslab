from datetime import datetime

from rest_framework import serializers

from bills.models import Bill


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_client_name(self, value):
        if len(value) > 0 and value != "-":
            return value
        else:
            raise serializers.ValidationError("This field must be not empty")

    def validate_client_org(self, value):
        if len(value) > 0 and value != "-":
            return value
        else:
            raise serializers.ValidationError("This field must be not empty")

    def validate_number(self, value):
        if type(value) == int:
            return value
        else:
            raise serializers.ValidationError("This field must be integer")

    def validate_date(self, value):
        if type(value) == datetime.date:
            return value
        else:
            raise serializers.ValidationError("This field must be date")

    def validate_sum(self, value):
        if type(value) == float:
            return value
        else:
            raise serializers.ValidationError("This field must be float")

    def validate_service(self, value):
        if len(value) > 0 and value != "-":
            return value
        else:
            raise serializers.ValidationError("This field must be not empty")


class BillSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField()
    client_org = serializers.CharField()
    number = serializers.IntegerField()
    date = serializers.DateField()
    sum = serializers.FloatField()
    service = serializers.CharField()

    class Meta:
        model = Bill
        fields = [
            "client_name",
            "client_org",
            "number",
            "sum",
            "date",
            "service",
        ]


class BillFilterSerializer(serializers.Serializer):
    organization = serializers.CharField(required=False)
    client = serializers.CharField(required=False)
