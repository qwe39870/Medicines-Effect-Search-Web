from django.urls import path
from .views import Index, Search, Find, Detail, Nothing


urlpatterns = [
    path('', Index.as_view(), name='Index'),
    path('search/', Search.as_view(), name='search'),
    path('find/', Find.as_view(), name='find'),
    path('nothing/', Nothing.as_view(), name='nothing'),
    path('detail/<int:id>', Detail.as_view(), name='detail'),

]