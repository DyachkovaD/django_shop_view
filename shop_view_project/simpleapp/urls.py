# from django.urls import path
# from .views import (
#     ProductsList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete
# )
# from .views import IndexView
#
# urlpatterns = [
#     path('', IndexView.as_view()),
#     # path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
#     # path('create/', ProductCreate.as_view(), name='product_create'),
#     # path('<int:pk>/update', ProductUpdate.as_view(), name='product_update'),
#     # path('<int:pk>/delete', ProductDelete.as_view(), name='product_delete'),
# ]

from django.urls import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]