"""
Test module for the State class.
"""
import unittest
from models.state import State
from models.engine.file_storage import FileStorage


storage = FileStorage(file_path="test_file.json")

class TestUser(unittest.TestCase):
    """
    Tests for State class
    """
    def setUp(self):
        """
        Create State instance to be used in all tests.
        """
        self.State = State()

    def tearDown(self):
        """
        Test cleanup method.
        """
        keys = [ key for key in storage.all().keys() ]
        for key in keys:
            del storage.all()[key]
        storage.save()

    def test_initialization(self):
        self.assertEqual(type(self.State).__name__, "State")
        self.assertEqual(isinstance(self.State.id, str), True)
        self.assertEqual(self.State.created_at, self.State.updated_at)
        self.assertEqual(isinstance(self.State.name, str), True)

if "__name__" == "__main__":
    unittest.main()