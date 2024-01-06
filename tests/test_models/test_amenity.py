"""
Test module for the Amenity class.
"""
import unittest
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


storage = FileStorage(file_path="test_file.json")

class TestUser(unittest.TestCase):
    """
    Tests for Amenity class
    """
    def setUp(self):
        """
        Create Amenity instance to be used in all tests.
        """
        self.Amenity = Amenity()

    def tearDown(self):
        """
        Test cleanup method.
        """
        keys = [ key for key in storage.all().keys() ]
        for key in keys:
            del storage.all()[key]
        storage.save()

    def test_initialization(self):
        self.assertEqual(type(self.Amenity).__name__, "Amenity")
        self.assertEqual(isinstance(self.Amenity.id, str), True)
        self.assertEqual(self.Amenity.created_at, self.Amenity.updated_at)
        self.assertEqual(self.Amenity.name, '')

if "__name__" == "__main__":
    unittest.main()