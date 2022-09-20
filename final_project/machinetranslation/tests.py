import unittest

from translator import englishToFrench, frenchToEnglish

class TestTranslationEnglishFrench(unittest.TestCase):
   
    def test_null(self):
        self.assertTrue(englishToFrench(''), None)

    def test_translation(self):
        e = 'Hello'
        f = 'Bonjour'
        self.assertEqual(englishToFrench(e), f)
        
        

class TestTranslationFrenchenglish(unittest.TestCase):

    def test_null(self):
        self.assertTrue(frenchToEnglish(''), None)

    def test_translation(self):
        e = 'Hello'
        f = 'Bonjour'
        self.assertEqual(frenchToEnglish(f), e)

    
if __name__ == '__main__':
    unittest.main()