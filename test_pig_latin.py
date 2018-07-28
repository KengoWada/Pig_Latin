import unittest
from pig_latin import *

class TestPigLatin(unittest.TestCase):
	
	def test_output(self):
		# Tests the output for various input values
		self.assertEqual(pig_latin('kengo'), 'engokay')
		self.assertEqual(pig_latin('will'), 'illway')
		self.assertEqual(pig_latin('eggplant'), 'eggplantway')
		self.assertEqual(pig_latin('Andela'), 'andelaway')

	def test_input(self):
		# Ensure only strings are input
		self.assertRaises(ValueError, pig_latin, 45)
		self.assertRaises(ValueError, pig_latin,2.33)
		self.assertRaises(ValueError, pig_latin, ['new'])
