import unittest
from src.vuln_scanner import scan_vulnerabilities

class TestVulnScanner(unittest.TestCase):
    def test_scan_vulnerabilities(self):
        self.assertIsNone(scan_vulnerabilities())

if __name__ == '__main__':
    unittest.main()
