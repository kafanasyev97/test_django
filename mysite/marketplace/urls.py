from django.urls import path
from .views import AccountView, another_register_view, AnotherLoginView, update_balance_get, GoodListView, create_order


app_name = 'marketplace'

urlpatterns = [
    path('register/', another_register_view, name='register'),
    path('login/', AnotherLoginView.as_view(), name='another_login'),
    path('account/', AccountView.as_view(), name='account'),
    path('account/<int:pk>/balance', update_balance_get, name='update_balance'),
    path('goods/', GoodListView.as_view(), name='goods_list'),
    path('create/', create_order, name='create_order'),
    ]
