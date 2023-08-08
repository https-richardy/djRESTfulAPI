from .products_urls import urlpatterns as product_urls
from .books_urls import urlpatterns as book_urls
from .clothings_urls import urlpatterns as clothing_urls

app_name = 'store'

urlpatterns = product_urls
urlpatterns += book_urls

urlpatterns += clothing_urls
