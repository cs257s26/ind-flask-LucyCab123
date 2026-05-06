
from ProductionCode.app import *
import unittest
class TestSOMETHING(unittest.TestCase):
    def setUp(self):
        #Sets up the SEARCH class to access our data
        self.data = Search()
    
    def test_nametoInfoCorrect(self):
        #sets up test app
        self.app = app.test_client() 
        #test app returns TestResponse object
        response = self.app.get('/name/Actinote zikani/', follow_redirects=True)
        #TestResponse successfull pulls data, and checks if ID's match
        self.assertEqual(self.data.data[2][0], response.data.decode("utf-8")[3])

    def test_typetolistCorrect(self):
        #sets up test app
        self.app = app.test_client() 
        #test app returns TestResponse object
        response = self.app.get('/type/Plant (Tree)/', follow_redirects=True) 
        #TestResponse sucessfully pulls data and checks if ID's match
        self.assertEqual(self.data.data[1][0], response.data.decode("utf-8")[3])

    def test_nametoInfoIncorrect(self):
        #sets up test app
        self.app = app.test_client() 
        #test app returns TestResponse object
        response = self.app.get('/name/fake/', follow_redirects=True)
        #TestResponse successfull pulls data and checks if error messages match
        self.assertEqual('Sorry! No animal found. Make sure you are entering the taxonomical name! Not all names are common names!', response.data.decode("utf-8"))

    def test_typetolistIncorrect(self):
        #sets up test app
        self.app = app.test_client() 
        #test app returns TestResponse object
        response = self.app.get('/type/fake/', follow_redirects=True) 
        #TestResponse sucessfully pulls data and checks if error messages match
        self.assertEqual('Sorry! No info found; make sure you entered a valid classification!', response.data.decode("utf-8"))

    def test_defaultError(self):
        #sets up test app
        self.app = app.test_client() 
        #test app returns TestResponse object
        response = self.app.get('/fake/fake/', follow_redirects=True) 
        #TestResponse sucessfully pulls data and checks if error messages match
        self.assertEqual("sorry, wrong format! Make sure your URL looks like 'http://127.0.0.1:<port>/'type/name'/'search criteria", response.data.decode("utf-8"))


if __name__ == '__main__':
    unittest.main()