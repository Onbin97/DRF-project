from django.urls import path
from rest_framework import routers

from .views import HelloAPI, BookAPI, BooksAPI, BooksAPIMixins, BookAPIMixins, BookAPIGenerics, BooksAPIGenerics, BookViewSet

# urlpatterns = [
#     path('hello/', HelloAPI),
#     path('books/', BooksAPI.as_view()),
#     path('book/<int:bid>/', BookAPI.as_view()),
#     path('mix/books/', BooksAPIMixins.as_view()),
#     path('mix/book/<int:bid>/', BookAPIMixins.as_view()),
#     path('gen/books/', BooksAPIGenerics.as_view()),
#     path('gen/book/<int:bid>/', BookAPIGenerics.as_view()),
# ] 
# 

router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls