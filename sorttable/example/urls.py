from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tablerow/<int:tablerow_id>/table_tr/', views.single_tablerow_row, name='tablerow_tr'),
    path('tablerow/update/', views.single_tablerow_form, name='tablerow_post_update'),
    path('tablerow/<int:tablerow_id>/update/', views.single_tablerow_form, name='tablerow_get_update'),
]
