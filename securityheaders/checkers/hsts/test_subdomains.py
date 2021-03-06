import unittest

from securityheaders.checkers.hsts import HSTSSubdomainsChecker

class HSTSSubdomainsCheckerTest(unittest.TestCase):
    def setUp(self):
       self.x = HSTSSubdomainsChecker()

    def test_checkNoHSTS(self):
       nox = dict()
       nox['test'] = 'value'
       self.assertEqual(self.x.check(nox), [])

    def test_checkNone(self):
       nonex = None
       self.assertEqual(self.x.check(nonex), [])

    def test_checkNoneHSTS(self):
       hasx = dict()
       hasx['strict-transport-security'] = None
       result = self.x.check(hasx)
       self.assertIsNotNone(result)
       self.assertEqual(len(result), 1)

    def test_ValidHSTS(self):
       hasx4 = dict()
       hasx4['strict-transport-security'] = "max-age=31536000; includeSubDomains"
       result = self.x.check(hasx4)
       self.assertEqual(self.x.check(hasx4), [])

    def test_NoSubdomains(self):
       hasx5 = dict()
       hasx5['strict-transport-security'] = "max-age=31536000"
       result = self.x.check(hasx5)
       self.assertIsNotNone(result)
       self.assertEqual(len(result), 1)

if __name__ == '__main__':
    unittest.main()
