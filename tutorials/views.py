from django.shortcuts import render
from .models import C, Cpp, Java, JavaScript, Php, Python

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.


def home_view(request):
    return render(request, "home.html")




def trial(request):
    python = Python.objects.all()
    context = {"python": python}
    return render(request, "registration/video.html", context)


# @login_required
# def add_to_course(request, slug):
#     item = get_object_or_404(Item, slug=slug)
# order_item, created = OrderItem.objects.get_or_create(
#     item=item,
#     user=request.user,
#     ordered=False
# )
# order_qs = Order.objects.filter(user=request.user, ordered=False)
# if order_qs.exists():
#     order = order_qs[0]
#     # check if the order item is in the order
#     if order.items.filter(item__slug=item.slug).exists():
#         order_item.quantity += 1
#         order_item.save()
#         messages.info(request, "This item quantity was updated.")
#         return redirect("core:order-summary")
#     else:
#         order.items.add(order_item)
#         messages.info(request, "This item was added to your cart.")
#         return redirect("core:order-summary")
# else:
#     ordered_date = timezone.now()
#     order = Order.objects.create(
#         user=request.user, ordered_date=ordered_date)
#     order.items.add(order_item)
#     messages.info(request, "This item was added to your cart.")
#     return redirect("core:order-summary")
