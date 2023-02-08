from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'total_sum', 'items']

    def create(self, validated_data):
        items = validated_data.pop('items')
        print(self.context)
        validated_data['author'] = self.context['request'].user
        order = super().create(validated_data)
        total_sum = 0
        order_items = []
        for item in items:
            print(item)
            order_items.append(
                OrderItem(order=order,
                        product=item['product'],
                        quantity=item['quantity']

            ))
            total_sum += item['product'].price * item['quantity']
        OrderItem.objects.bulk_create(order_items)
        order.total_sum = total_sum
        order.save()
        return order

