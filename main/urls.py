from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from example.views import index


from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('all-news',views.all_news,name='all-news'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('all-categories',views.all_category,name='all-category'),
    path('category/<int:id>',views.category,name='category'),
    path('', index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
