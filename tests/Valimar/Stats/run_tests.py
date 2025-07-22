#!/usr/bin/env python3
"""
Simple test runner for Stats Spotlight SID tests.
"""

import unittest
import sys
import os

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from TEST_Stats_Spotlight_Sid import TEST_Stats_Spotlight_Sid

if __name__ == "__main__":
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TEST_Stats_Spotlight_Sid)
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)