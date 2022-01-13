import unittest

from WatsonTranslatorTest import englishToFrench, frenchToEnglish

class  TestTransEng(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(englishToFrench("Hello my friend"),"Hello my friend")

unittest.main()
