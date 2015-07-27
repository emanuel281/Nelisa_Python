import unittest
import spaza_shop

class unittesting(unittest.TestCase):
	"""docstring for unittesting"""
	def test_get_sales(self):
		sales = spaza_shop.get_sales("Nelisa.csv")

		expected = {"Milk 1l" : 30,
					"Imasi" : 1,
					"Bread" : 2,
					"Chakalaka Can" : 3,
					"Gold Dish Vegetable Curry Can" : 2,
					"Fanta 500ml" : 3,
					"Coke 500ml" : 2,
					"Cream Soda 500ml" : 2}
		self.assertEquals(sales, expected, "Got sales")

	def test_get_most_pop_item(self):
		sales = spaza_shop.get_sales("Nelisa.csv")
		most_pop = spaza_shop.get_most_pop_item(sales)
		expected = {"Milk 1l" : 30}
		self.assertEquals(expected, most_pop)

	def test_get_most_pop_cat(self):
		sales = spaza_shop.get_sales("Nelisa.csv")
		most_pop_cat = spaza_shop.get_most_pop_cat(sales)
		expected = {"dairy" : 310}
		self.assertEquals(expected, most_pop_cat)		

if __name__ == '__main__':
	unittest.main()
