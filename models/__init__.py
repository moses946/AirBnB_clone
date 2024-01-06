#!/usr/bin/python3
"""
The initialization module for imports
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()