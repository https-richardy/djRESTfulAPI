from django.urls import path
from store.views import (
    ClothingList, ClothingDetail,
    ClothingCreate, ClothingListWithFilters,
    ClothingUpdate
)


urlpatterns = [
    path('clothings/', ClothingList.as_view(), name='clothings-list'),
    path('clothings/search/', ClothingListWithFilters.as_view(), name='clothing-search'),  # noqa
    path('clothing/create/', ClothingCreate.as_view(), name='clothing-create'),
    path('clothing/<int:pk>/', ClothingDetail.as_view(), name='clothing-detail'),  # noqa
    path('clothing/<int:pk>/update/', ClothingUpdate.as_view(), name='clothing-update')  # noqa
]
