from django.test import TestCase, RequestFactory
from restaurant.models import MenuItem
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        MenuItem.objects.create(
            title="Pizza",
            price=200.00,
            inventory=5
        )
        MenuItem.objects.create(
            title="Cake",
            price=150.00,
            inventory=4
        )

    def test_getall(self):
        menuitems = MenuItem.objects.all()
        serialized_menuitems = MenuItemSerializer(menuitems, many=True)
        request = self.factory.get('restaurant/menu/')
        response = MenuItemsView.as_view()(request)

        self.assertEqual(response.data, serialized_menuitems.data)
