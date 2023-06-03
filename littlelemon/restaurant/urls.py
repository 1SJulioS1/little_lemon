from django.urls import path
from .views import MenuItemsView, SingleMenuItemView
urlpatterns = [
    # path('', views.index, name='index'),

    path("menu/", MenuItemsView.as_view(), name="menu"),
    path("menu/<int:pk>", SingleMenuItemView.as_view(), name="menu"),
    # path("booking/", BookingView.as_view(), name="menu"),
    #    path("menu_item/<int:pk>", views.display_menu_item, name="menu_item"),
]
