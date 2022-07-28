from rest_framework import serializers
from payment.models import PaymentHistory


class PaymentHistorySerailizer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = [
            'id',
            'api_version',
            'created',
        ]