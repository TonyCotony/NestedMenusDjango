from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import show_menu
from app.views import show_menu, about


urlpatterns = [
    path('home/', show_menu, {'name': 'Home'}, name='home'),
    path('company/', show_menu, {'name': 'About company'}, name='company'),
    path('development/', show_menu, {'name': 'Development'}, name='development'),
    path('development/cpp', show_menu, {'name': 'Development C++'}, name='development_cpp'),
    path('development/cpp/qt', show_menu, {'name': 'Development C++/Qt'}, name='development_cpp_qt'),
    path('development/python', show_menu, {'name': 'Development Python'}, name='development_python'),
    path('development/python/django', show_menu, {'name': 'Development Python/Django'}, name='development_python_django'),
    path('development/python/tornado', show_menu, {'name': 'Development Python/Tornado'}, name='development_python_tornado'),
    path('prices/', show_menu, {'name': 'Prices'}, name='prices'),
]

# urlpatterns = [
#     path('', show_menu, name='home'),
#     path('about/', about, name='about'),
# ]
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)