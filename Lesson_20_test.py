import unittest
from Lesson_20 import maxnumber, stringTitle, juftNumbers, fiboNumber

# class MaxxNumberTest(unittest.TestCase):
#     def maxx3Number(self):
#         numbers = maxnumber(3,2,5)
#         self.assertAlmostEqual(numbers,5)
# unittest.main()

# class StringTitleTest(unittest.TestCase):
#     def stringTest(self):
#         stringvalue = stringTitle(['azamat','jumabayev','izzat', 'raximov'])
#         self.assertIs(stringvalue,['Azamat','Jumabayev','Izzat', 'Raximov'])
# unittest.main()

# class juftNumberTest(unittest.TestCase):
#     def juft_number(self):
#         numberArray = juftNumbers(1, 2, 3, 4, 5, 6)
#         self.assertAlmostEqual(numberArray, 2,4,6)
# unittest.main()

class fiboTrueFalse(unittest.TestCase):
    def trueFibo(self):
        self.assertTrue(fiboNumber(8,13))
    def falseFibo(self):
        self.assertFalse(fiboNumber(8,12))
unittest.main()