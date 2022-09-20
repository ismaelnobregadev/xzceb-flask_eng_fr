import unittest
from translator import english2french, french2english

class TestTranslationEnglishFrench(unittest.TestCase):
   
    def test_null(self):
        self.assertTrue(english2french(''), None)

    def test_translation(self):
        e = 'Hello'
        f = 'Bonjour'
        self.assertEqual(english2french(e), f)
          
class TestTranslationFrenchEnglish(unittest.TestCase):

    def test_null(self):
        self.assertTrue(french2english(''), None)

    def test_translation(self):
        e = 'Hello'
        f = 'Bonjour'
        self.assertEqual(french2english(f), e)
    
if __name__ == '__main__':
    unittest.main()