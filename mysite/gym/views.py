import json
from django.shortcuts import render, redirect
from django.views import View
from customer.models import OrderModel
# Create your views here.
def shalom(request):

    return render(request, 'shalom.html')

def robot(request):

    return render(request, 'aiortc/examples/server/index.html')

class OrderConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }

        return render(request, 'customer/order_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)

        if data['isPaid']:
            order = OrderModel.objects.get(pk=pk)
            order.is_paid = True
            order.save()

        return redirect('payment-confirmation')