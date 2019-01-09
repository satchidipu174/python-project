import unittest
import account as AccountClass

class Test(unittest.TestCase)
    accInfo = AccountClass.account()
    def test_check_password_length(self):
        print("Checking possible password\n")
        passwordList = [ 'abeautifulday', 'astrictboss', 'alovelyhouse' ]

        for password in passwordList:
            print("Checking password " + password + "\n")
            passInfo = self.accInfo.check_password_length(passwd)
            self.assertTrue(passInfo)

if __name__ == '__main__' :
    unittest.main()
