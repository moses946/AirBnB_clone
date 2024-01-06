"""
Test module for the City class.
"""
import unittest
from models.city import City
from models.engine.file_storage import FileStorage


storage = FileStorage(file_path="test_file.json")

class TestUser(unittest.TestCase):
    """
    Tests for City class
    """
    def setUp(self):
        """
        Create City instance to be used in all tests.
        """
        self.city = City()

    def tearDown(self):
        """
        Test cleanup method.
        """
        keys = [ key for key in storage.all().keys() ]
        for key in keys:
            del storage.all()[key]
        storage.save()

    def test_initialization(self):
        self.assertEqual(type(self.city).__name__, "City")
        self.assertEqual(isinstance(self.city.id, str), True)
        self.assertEqual(self.city.created_at, self.city.updated_at)
        self.assertEqual(self.city.name, '')
        self.assertEqual(self.city.state_id, '')

if "__name__" == "__main__":
    unittest.main()