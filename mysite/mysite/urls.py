
from django.contrib import admin
from django.urls import path,include
from blog.views import blog_list
from . import index_view
urlpatterns = [
    path('', index_view.home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),

]
