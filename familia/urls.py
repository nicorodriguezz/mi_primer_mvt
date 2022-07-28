from django.contrib import admin
from django.urls import path
from integrantes.views import full_integrantes, define_integrante_1, define_integrante_2, define_integrante_3, define_integrante_4


urlpatterns = [
    path('admin/', admin.site.urls),
    path('full-integrantes/', full_integrantes, name = 'full_integrantes'),
    path('integrante-1/', define_integrante_1, name = 'define_integrante_1'),
    path('integrante-2/', define_integrante_2, name = 'define_integrante_2'),
    path('integrante-3/', define_integrante_3, name = 'define_integrante_3'),
    path('integrante-4/', define_integrante_4, name = 'define_integrante_4'),
]
