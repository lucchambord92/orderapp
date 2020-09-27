from django.urls import path

from . import views

app_name = 'order'
urlpatterns = [
	# path /shop/1/
	path('shop/<int:shop_id>/', views.shop, name='shop_detail'),
	path('', views.OrderListView.as_view(), name='order_list'),
	path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
	path('orderline/create/<int:pk>/', views.order_line_create, name='order_line_create'),
]
