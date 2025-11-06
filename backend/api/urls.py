from django.urls import path
from .views import users, listings

urlpatterns = [
    path("users/", users.userList),
    path("users/<int:user_id>/", users.userDetail),
    path("listings/", listings.listingList),
    path("listings/<int:listing_id>/", listings.listingDetail),
]