from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from sitewomen import settings
from women import views
from women.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
    path('users/', include('users.urls', namespace="users")),
    path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = page_not_found

admin.site.site_header = "Панель адміністратора"
admin.site.index_title = "Відомі жінки світу"
