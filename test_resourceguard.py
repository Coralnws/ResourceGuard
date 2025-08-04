# test_resourceguard.py
"""
Tests for ResourceGuard module.
"""

import unittest
from resourceguard import ResourceGuard

class TestResourceGuard(unittest.TestCase):
    """Test cases for ResourceGuard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ResourceGuard()
        self.assertIsInstance(instance, ResourceGuard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ResourceGuard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
