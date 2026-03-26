# Импортируем настройки проекта.
from django.conf import settings
# Импортируем функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
    path('users/', include('users.urls')),
    # Добавляем новый путь для регистрации.
    # В конце добавляем к списку вызов функции static.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

handler404 = 'core.views.page_not_found'
handler403 = 'core.views.access_denied'
