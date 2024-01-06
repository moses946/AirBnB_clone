"""
Test module for the User class.
"""
import unittest
from models.user import User
from models.engine.file_storage import FileStorage


storage = FileStorage(file_path="test_file.json")

class TestUser(unittest.TestCase):
    """
    Tests for user class
    """
    def setUp(self):
        """
        Create User instance to be used in all tests.
        """
        self.user = User()

    def tearDown(self):
        """
        Test cleanup method.
        """
        keys = [ key for key in storage.all().keys() ]
        for key in keys:
            del storage.all()[key]
        storage.save()

    def test_initialization(self):
        self.assertEqual(type(self.user).__name__, "User")
        self.assertEqual(isinstance(self.user.id, str), True)
        self.assertEqual(self.user.created_at, self.user.updated_at)
        self.assertEqual(self.user.first_name, '')

if "__name__" == "__main__":
    unittest.main()