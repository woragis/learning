from django.test import TestCase

# Create your tests here.
# tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Item
from django.utils import timezone
from datetime import timedelta

class ItemModelTestCase(TestCase):

    def setUp(self):
        """Create an initial test item"""
        self.item = Item.objects.create(
            name="Test Item",
            description="A test item description",
            price=10.99
        )

    def test_create_item(self):
        """Test creating an item"""
        item = Item.objects.create(
            name="New Item",
            description="Description for new item",
            price=20.50
        )
        self.assertEqual(Item.objects.count(), 2)
        self.assertEqual(item.name, "New Item")
        self.assertEqual(item.price, 20.50)
    
    def test_read_item(self):
        """Test reading an item"""
        item = self.item
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.description, "A test item description")
        self.assertEqual(item.price, 10.99)
    
    def test_update_item(self):
        """Test updating an item"""
        self.item.name = "Updated Item"
        self.item.description = "Updated description"
        self.item.price = 15.99
        self.item.save()

        updated_item = Item.objects.get(id=self.item.id)
        self.assertEqual(updated_item.name, "Updated Item")
        self.assertEqual(updated_item.description, "Updated description")
        self.assertEqual(updated_item.price, 15.99)
    
    def test_delete_item(self):
        """Test deleting an item"""
        item_to_delete = Item.objects.create(
            name="Item to delete",
            description="Item to be deleted",
            price=5.99
        )
        item_to_delete.delete()
        self.assertEqual(Item.objects.count(), 1)
    
    def test_item_creation_url(self):
        """Test if the item creation view works"""
        response = self.client.get(reverse('item_create'))
        self.assertEqual(response.status_code, 200)
    
    def test_item_list_url(self):
        """Test if the item list view works"""
        response = self.client.get(reverse('item_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_item_update_url(self):
        """Test if the item update view works"""
        response = self.client.get(reverse('item_update', args=[self.item.id]))
        self.assertEqual(response.status_code, 200)

    def test_item_delete_url(self):
        """Test if the item delete view works"""
        response = self.client.get(reverse('item_delete', args=[self.item.id]))
        self.assertEqual(response.status_code, 200)
    
    def test_item_model_str(self):
        """Test if the model's string representation works correctly"""
        self.assertEqual(str(self.item), "Test Item")
