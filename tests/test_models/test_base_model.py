"""
Test Module for BaseModel class.
"""
import unittest
from models.base_models import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage

storage = FileStorage(file_path = "test_file.json")

class TestBaseModel(unittest.TestCase):
    """
    Class testing BaseModel functionality.
    """
    def setUp(self):
        """
        Invoked before each test to create an instance of BaseModel
        """
        self.model = BaseModel()
    
    def tearDown(self):
        """
        Invoked after each test is done running
        """
        keys = [key for key in storage.all().keys()]
        for key in keys:            
            del storage.all()[key]
        storage.save()
    
    def test_initialization(self):
        self.assertEqual(isinstance(self.model.id, str), True)
        self.assertEqual(isinstance(self.model.created_at, datetime), True)
        self.assertEqual(self.model.created_at, self.model.updated_at)
    
    def test_printing(self):
        self.assertEqual(self.model.__str__(), f"[BaseModel]({self.model.id}){self.model.__dict__}")
    
    def test_saving(self):
        self.model.save()
        self.assertNotEqual(self.model.created_at, self.model.updated_at)
        self.assertEqual(isinstance(self.model.created_at, datetime), True)

    def test_init_with_dict_values(self):
        arg = self.model.to_dict()
        model2 = BaseModel(**arg)
        for key in arg.keys():
            with self.subTest(key=key):
                if key == "__class__":
                    continue
                self.assertEqual(getattr(self.model, key), getattr(model2, key))

if "__name__" == "__main__":
    unittest.main()