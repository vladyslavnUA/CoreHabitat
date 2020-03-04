from django.urls import path
from .views import (
    home,
    CodeList,
    CodeDetail,
    CodeCreate,
    CodeUpdate,
    CodeDelete,
)

app_name = 'listings'

urlpatterns = [
    path('', home, name='home_page'),
    # view for the results/reference page (the list view)
    path('listings/', CodeList.as_view(), name='reference'),
    path('listings/add-propertyitem/', CodeCreate.as_view(), name='add_propertyitem'),
    path('listings/<slug:slug>/edit/', CodeUpdate.as_view(), name='edit_propertyitem'),
    path('listings/<slug:slug>/delete/', CodeDelete.as_view(),
         name='remove_listing'),
    path('listings/<slug:slug>/', CodeDetail.as_view(), name='details'),
    path('listings/', inclue('listings.urls')),
]