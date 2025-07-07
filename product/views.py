from django.views import View
from django.shortcuts import render
from .models import ProductModel
import logging
from django.core.paginator import Paginator

logger = logging.getLogger(__name__)

# class ProductsPage(View):
#     def get(self, request):
#         try:
#             data = ProductModel.objects.all()
#             categories = ["All Products", "Vehicles", "Communication Systems", "Protective Gear"]
#             product = list(data)*20
#             return render(request, "products.html", {
#                 "data": product,
#                 "categories": categories
#             })
#         except Exception as e:
#             logger.error(f"Home sahifasida xatolik: {str(e)}")
#             return render(request, "error.html", {"message": "Noma'lum xatolik yuz berdi."})


# class ProductsPage(View):
#     def get(self,request):
#         data  =ProductModel.objects.all().order_by('id')
#         product = list(data)*100
#         search_query = request.GET.get('q')

#         if search_query:
#             product=product.filter(title__icontais=search_query)
        
#         page_size = request.GET.get('page_size', 8)
#         paginator = Paginator(product, page_size)

#         page_num = request.GET.get('page', 1)
#         pages = paginator.get_page(page_num)
#         categories = ["All Products", "Vehicles", "Communication Systems", "Protective Gear"]
#         context = {'pages': pages,"categories": categories}
#         return render(request=request,template_name='products.html',context=context)



from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import ProductModel

class ProductsView(View):
    def get(self, request):
        data = ProductModel.objects.all().order_by('id')
        # product = list(data) * 100

        search_query = request.GET.get('q')
        if search_query:
            data = data.filter(name__icontains=search_query)
            product = list(data)

        page_size = int(request.GET.get('page_size', 10))
        paginator = Paginator(data, page_size)

        page_num = request.GET.get('page', 1)
        pages = paginator.get_page(page_num)

        # 👉 Custom page range with ellipsis
        page_range = paginator.get_elided_page_range(
            number=pages.number,
            on_each_side=1,
            on_ends=2
        )

        categories = ["All Products", "Vehicles", "Communication Systems", "Protective Gear"]

        context = {
            'pages': pages,
            'page_range': page_range,  # qo‘shildi
            "categories": categories
        }
        return render(request, 'products.html', context)



class ProductsDetailView(View):
    def get(self, request, pk):
        product = ProductModel.objects.all().get(pk=pk)

        context = {
            'product': product,
        }
        return render(request, 'product_detail.html', context)
