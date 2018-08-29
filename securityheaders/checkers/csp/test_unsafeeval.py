import unittest

from securityheaders.checkers.csp import CSPUnsafeEvalChecker

class UnsafeEvalTest(unittest.TestCase):
    def setUp(self):
       self.x = CSPUnsafeEvalChecker()

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

    def test_wildCardOk(self):
       hasx5 = dict()
       hasx5['content-security-policy'] = 'script-src *'
       self.assertEquals(self.x.check(hasx5), [])

    def test_UnsafeEvalNok(self):
       hasx4 = dict()
       hasx4['content-security-policy'] = "script-src 'unsafe-eval'"
       result = self.x.check(hasx4)
       self.assertIsNotNone(result)
       self.assertEquals(len(result), 1)

    def test_CSPOK(self):
       hasx2 = dict()
       hasx2['content-security-policy'] = "default-src 'self'; script-src tweakers.net"
       self.assertEquals(self.x.check(hasx2), [])

    def test_UnsafeEvalNok2(self):
       hasx6 = dict()
       hasx6['content-security-policy'] = "default-src 'none'; script-src 'unsafe-eval';"
       result = self.x.check(hasx6)
       self.assertIsNotNone(result)
       self.assertEquals(len(result), 1)

    def test_UnsafeEvalNok3(self):
       hasx7 = dict()
       hasx7['content-security-policy'] = "default-src 'none'; script-src 'unsafe-eval' 'unsafe-inline';"
       result = self.x.check(hasx7)
       self.assertIsNotNone(result)
       self.assertEquals(len(result), 1)

    def test_UnsafeEvalDefaultSrcNok(self):
       hasx8 = dict()
       hasx8['content-security-policy'] = "default-src 'unsafe-eval';"
       result = self.x.check(hasx8)
       self.assertIsNotNone(result)
       self.assertEquals(len(result), 1)

    def test_UnsafeEvalDefaultSrcNok2(self):
       hasx9 = dict()
       hasx9['content-security-policy'] = "default-src 'unsafe-eval' 'unsafe-inline';"
       result = self.x.check(hasx9)
       self.assertIsNotNone(result)
       self.assertEquals(len(result), 1)


if __name__ == '__main__':
    unittest.main()