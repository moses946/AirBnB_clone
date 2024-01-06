"""
Test module for the Review class.
"""
import unittest
from models.review import Review
from models.engine.file_storage import FileStorage


storage = FileStorage(file_path="test_file.json")

class TestUser(unittest.TestCase):
    """
    Tests for Review class
    """
    def setUp(self):
        """
        Create Review instance to be used in all tests.
        """
        self.Review = Review()

    def tearDown(self):
        """
        Test cleanup method.
        """
        keys = [ key for key in storage.all().keys() ]
        for key in keys:
            del storage.all()[key]
        storage.save()

    def test_initialization(self):
        self.assertEqual(type(self.Review).__name__, "Review")
        self.assertEqual(isinstance(self.Review.id, str), True)
        self.assertEqual(self.Review.created_at, self.Review.updated_at)
        self.assertEqual(self.Review.user_id, '')
        self.assertEqual(isinstance(self.Review.text, str), True)

if "__name__" == "__main__":
    unittest.main()