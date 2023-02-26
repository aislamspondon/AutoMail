from customerview import views
from django.urls import path

urlpatterns = [
    path('', views.intro, name="intro"),
    path('input', views.customerInput, name='customer_input'),
    path('customerlist', views.customerList, name='customerlist'),
    path('downloadinvoice', views.generate_invoice, name='generate_input'),
    path('createpreview', views.create_customer_preview, name='create_preview'),
    path('latestpreview', views.latest_preview_list, name='latest_preview'),
    path('previewlist', views.customer_preview_list, name='previewlist'),
    path('updatepreview/<int:preview_id>', views.customer_preview_edit, name='update_preview'),
    path('deletepreview/<int:preview_id>', views.customer_preview_delete, name='delete_preview'),

    
]