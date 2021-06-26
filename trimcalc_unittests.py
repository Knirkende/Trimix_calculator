import unittest
from trimcalc import GasCalc

class TestGasCalc(unittest.TestCase):
	def test_gases_getter_standard_empty(self):
		"""
		Test for a standard gas with an empty starting mix.
		"""
		g = GasCalc()
		standard_dict = {
		'tank_size': 24,
		'current_pressure': 0,
		'current_o2': 21,
		'current_he': 35,
		'top_o2': 21,
		'want_o2': 21,
		'want_he': 35,
		'want_pressure': 220
		}
		g.gases_setter(standard_dict)
		expected = (123, 77, 20)
		actual = g.gases_getter()
		self.assertEqual(expected, actual,
			'Unexpected result from standard gas with empty starting mix.')

	def test_gases_getter_standard_empty(self):
		"""
		Test for a standard gas with a non-empty starting mix.
		"""
		g = GasCalc()
		standard_dict = {
		'tank_size': 24,
		'current_pressure': 50,
		'current_o2': 21,
		'current_he': 35,
		'top_o2': 21,
		'want_o2': 21,
		'want_he': 35,
		'want_pressure': 220
		}
		g.gases_setter(standard_dict)
		expected = (95, 59, 16)
		actual = g.gases_getter()
		self.assertEqual(expected, actual,
			'Unexpected result from standard gas with non-empty starting mix.')

	def test_gases_getter_no_helium(self):
		"""
		Test for a mix containing no helium.
		"""
		g = GasCalc()
		standard_dict = {
		'tank_size': 24,
		'current_pressure': 50,
		'current_o2': 21,
		'current_he': 0,
		'top_o2': 21,
		'want_o2': 32,
		'want_he': 0,
		'want_pressure': 220
		}
		g.gases_setter(standard_dict)
		expected = (139, 0, 31)
		actual = g.gases_getter()
		self.assertEqual(expected, actual,
			'Unexpected result from mix containing no helium.')

	def test_gases_getter_edge_case(self):
		"""
		Test for a standard gas with an almost empty starting mix.
		"""
		g = GasCalc()
		standard_dict = {
		'tank_size': 24,
		'current_pressure': 1,
		'current_o2': 21,
		'current_he': 35,
		'top_o2': 21,
		'want_o2': 21,
		'want_he': 35,
		'want_pressure': 220
		}
		g.gases_setter(standard_dict)
		expected = (122, 77, 20)
		actual = g.gases_getter()
		self.assertEqual(expected, actual,
			'Unexpected result from standard gas with almost empty starting mix.')

	def test_gases_getter_impossible(self):
		"""
		Test for an unachievable gas mix.
		"""
		g = GasCalc()
		standard_dict = {
		'tank_size': 24,
		'current_pressure': 200,
		'current_o2': 21,
		'current_he': 35,
		'top_o2': 21,
		'want_o2': 18,
		'want_he': 45,
		'want_pressure': 220
		}
		g.gases_setter(standard_dict)
		expected = (-8, 29, -1)
		actual = g.gases_getter()
		self.assertEqual(expected, actual,
			'Unexpected result from unachievable case.')

	def test_gases_getter_weird_case(self):
		"""
		Test for a small tank size with a non-standard mix.
		"""
		g = GasCalc()
		standard_dict = {
		'tank_size': 3,
		'current_pressure': 10,
		'current_o2': 21,
		'current_he': 35,
		'top_o2': 32,
		'want_o2': 50,
		'want_he': 45,
		'want_pressure': 220
		}
		g.gases_setter(standard_dict)
		expected = (10, 96, 105)
		actual = g.gases_getter()
		self.assertEqual(expected, actual,
			'Unexpected result from weird case.')

	def test_the_tester(self):
		"""
		Test to make sure tests fail on incorrect return values.
		"""
		g = GasCalc()
		standard_dict = {
		'tank_size': 3,
		'current_pressure': 10,
		'current_o2': 21,
		'current_he': 35,
		'top_o2': 21,
		'want_o2': 50,
		'want_he': 45,
		'want_pressure': 220
		}
		g.gases_setter(standard_dict)
		expected = (10, 90, 0)
		actual = g.gases_getter()
		self.assertEqual(expected, actual,
			'This test should fail.')

if __name__ == '__main__':
	unittest.main()