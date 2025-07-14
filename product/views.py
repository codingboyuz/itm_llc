
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import ProductModel
from shared.utils import log_request


class ProductsView(View):
    def get(self, request):
        log_request(logger_name="product",request=request)

        data = ProductModel.objects.all().order_by('id')

        search_query = request.GET.get('q')
        if search_query:
            data = data.filter(name__icontains=search_query)

        page_size = int(request.GET.get('page_size', 10))
        paginator = Paginator(data, page_size)

        page_num = request.GET.get('page', 1)
        pages = paginator.get_page(page_num)

        # Sahifalash uchun elided page range (… bilan qisqartirilgan raqamlar)
        page_range = paginator.get_elided_page_range(
            number=pages.number,
            on_each_side=1,
            on_ends=2
        )

        categories = ["All Products", "Vehicles", "Communication Systems", "Protective Gear"]

        context = {
            'pages': pages,
            'page_range': page_range,
            "categories": categories
        }
        return render(request, 'products.html', context)


class ProductsDetailView(View):
    def get(self, request, pk):
        log_request(logger_name="product_detail",request=request)

        product = get_object_or_404(ProductModel, pk=pk)

        images = product.images.all()  # ProductImage modelidagi rasmlar
        fields = product.fields.all()  # ProductField modelidagi qo‘shimcha maydonlar

        context = {
            'product': product,
            'images': images,
            'fields': fields
        }
        return render(request, 'product_detail.html', context)
