import unittest
from src.nmap_scanner import run_nmap_scan

class TestNmapScanner(unittest.TestCase):
    def test_run_nmap_scan(self):
        self.assertIsNone(run_nmap_scan())

if __name__ == '__main__':
    unittest.main()
