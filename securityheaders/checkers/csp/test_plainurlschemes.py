import unittest

from securityheaders.checkers.csp import CSPPlainUrlSchemesChecker


class UnsafeUrkSchemeTest(unittest.TestCase):

    def setUp(self):
       self.x = CSPPlainUrlSchemesChecker()

    def test_checkNoCSP(self):
       nox = dict()
       nox['test'] = 'value'
       self.assertEquals(self.x.check(nox), [])

    def test_checkNone(self):
       nonex = None
       self.assertEquals(self.x.check(nonex), [])

    def test_checkNoneCSP(self):
       hasx = dict()
       hasx['content-security-policy'] = None
       self.assertEquals(self.x.check(hasx), [])


    def test_All(self):
       hasx4 = dict()
       hasx4['content-security-policy'] = "script-src https: http: data:"
       self.assertIsNotNone(self.x.check(hasx4))
       self.assertEquals(len(self.x.check(hasx4)), 3) #all 3 of them

    def test_http(self):
       hasx3 = dict()
       hasx3['content-security-policy'] = "script-src http:"
       self.assertIsNotNone(self.x.check(hasx3))
       self.assertEquals(len(self.x.check(hasx3)), 1) #http:

    def test_validCSP(self):
       hasx2 = dict()
       hasx2['content-security-policy'] = "default-src 'self'; script-src tweakers.net"
       self.assertEquals(self.x.check(hasx2), [])

if __name__ == '__main__':
    unittest.main()