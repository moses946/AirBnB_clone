"""
Test module for the Place class.
"""
import unittest
from models.place import Place
from models.engine.file_storage import FileStorage


storage = FileStorage(file_path="test_file.json")

class TestUser(unittest.TestCase):
    """
    Tests for Place class
    """
    def setUp(self):
        """
        Create Place instance to be used in all tests.
        """
        self.Place = Place()

    def tearDown(self):
        """
        Test cleanup method.
        """
        keys = [ key for key in storage.all().keys() ]
        for key in keys:
            del storage.all()[key]
        storage.save()

    def test_initialization(self):
        self.assertEqual(type(self.Place).__name__, "Place")
        self.assertEqual(isinstance(self.Place.id, str), True)
        self.assertEqual(self.Place.created_at, self.Place.updated_at)
        self.assertEqual(self.Place.name, '')
        self.assertEqual(isinstance(self.Place.latitude, float), True)

if "__name__" == "__main__":
    unittest.main()