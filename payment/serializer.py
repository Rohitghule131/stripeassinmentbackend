from payment.models import PaymentHistory
from rest_framework import serializers


class PaymentHistoryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = [
            'name',
            'email',
            'amount',
            'city',
            'state',
            'country',
            'status'
        ]