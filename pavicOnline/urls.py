from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('painel/', include('painel.urls', namespace="users")),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
