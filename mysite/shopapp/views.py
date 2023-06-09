from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from timeit import default_timer
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from .models import Product, Order
from .forms import ProductForm, OrderForm, GroupForm


class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        products = [
            ('Laptop', 1999),
            ('Desktop', 2999),
            ('Smartphone', 999)
        ]
        context = {
            'time_running': default_timer(),
            'products': products
        }
        return render(request, 'shopapp/shop-index.html', context=context)


class GroupsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'form': GroupForm(),
            'groups': Group.objects.prefetch_related('permissions').all(),
        }
        return render(request, 'shopapp/groups-list.html', context=context)

    def post(self, request: HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(request.path)


def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # price = form.cleaned_data['price']
            # Product.objects.create(**form.cleaned_data)
            form.save()
            url = reverse('shopapp:products_list')
            return redirect(url)
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'shopapp/create-product.html', context=context)


class OrdersListView(LoginRequiredMixin, ListView):
    queryset = (Order.objects.select_related('user').prefetch_related('products'))


class OrdersDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shopapp.view_order'
    queryset = (Order.objects.select_related('user').prefetch_related('products'))


class OrderCreateView(CreateView):
    template_name = 'shopapp/create-order.html'
    model = Order
    fields = 'delivery_address', 'promocode', 'user', 'products'
    success_url = reverse_lazy('shopapp:orders_list')


class OrderUpdateView(UpdateView):
    template_name = 'shopapp/order_update_form.html'
    model = Order
    fields = 'delivery_address', 'promocode', 'user', 'products'

    def get_success_url(self):
        return reverse(
            'shopapp:order_details',
            kwargs={'pk': self.object.pk}
        )


class OrderDeleteView(DeleteView):
    template_name = 'shopapp/order_confirm_delete.html'
    model = Order
    success_url = reverse_lazy('shopapp:orders_list')


class ProductDetailsView(DetailView):
    template_name = 'shopapp/products-details.html'
    model = Product
    context_object_name = 'product'


class ProductsListView(ListView):
    template_name = 'shopapp/products-list.html'
    # model = Product
    context_object_name = 'products'
    queryset = Product.objects.filter(archived=False)


class ProductCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        # return self.request.user.groups.filter(name='secret-group').exists()
        return self.request.user.is_superuser
    model = Product
    fields = 'name', 'price', 'description', 'discount', 'created_by'
    success_url = reverse_lazy('shopapp:products_list')


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        if self.request.user.is_superuser or (self.request.user.has_perm('shopapp.change_product') and
                self.request.user.id == self.get_object().created_by_id):
            return True
        return False
    model = Product
    fields = 'name', 'price', 'description', 'discount'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse(
            'shopapp:product_details',
            kwargs={'pk': self.object.pk}
        )


# class ProductUpdateView(PermissionRequiredMixin, UpdateView):
#     permission_required = 'shopapp.change_product'
#     model = Product
#     fields = 'name', 'price', 'description', 'discount'
#     template_name_suffix = '_update_form'
#
#     def get_success_url(self):
#         return reverse(
#             'shopapp:product_details',
#             kwargs={'pk': self.object.pk}
#         )


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shopapp:products_list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)
