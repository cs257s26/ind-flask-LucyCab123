
from app import *
import unittest
"""I have no idea why these fail"""
class TestSOMETHING(unittest.TestCase):
    data = load_data()
    def test_nametoInfo(self):
        #sets up a special test app
        self.app = app.test_client() 
        #test app returns TestResponse object
        response = self.app.get('/name/Actinote%zikan/', follow_redirects=True) 
        #TestResponse has webpage in .data
        self.assertEqual(nameToInfo("Actinotezikan"), response.data)

    def test_typetolist(self):
        #sets up a special test app
        self.app = app.test_client() 
        #test app returns TestResponse object
        response = self.app.get('/type/Insect/', follow_redirects=True) 
        #TestResponse has webpage in .data
        self.assertEqual(typeToList("Insect"), response.data)