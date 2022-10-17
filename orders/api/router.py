from rest_framework.routers import DefaultRouter

from orders.api.view import OrderApiViewSet

router_orders = DefaultRouter()

router_orders.register(
    prefix='orders', basename='orders', viewset=OrderApiViewSet
)