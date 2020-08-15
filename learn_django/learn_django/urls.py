from django.contrib import admin
from django.urls import path, include


from learn_django.otusPlus.views.views import index_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('myblog.urls')),
    path('otus/', index_view),
]
