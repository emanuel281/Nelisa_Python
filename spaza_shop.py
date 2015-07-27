import csv

def get_sales(filename="Nelisa Sales History.csv"):
	sales = {}

	with open(filename) as sales_file:
		sales_history = csv.reader(sales_file, delimiter=";")
		for line in sales_history:
			if line[2] == 'stock item':
				print
			elif line[2] not in sales:
				sales[line[2]] = int(line[3])
			else:
				sales[line[2]] += int(line[3])

	return sales

def get_most_pop_item(sales):
	val = sales.items()
	most = {}
	most[val[0][0]] = val[0][1]

	for key in sales:
		if most.values()[0] < sales[key]:
			most = {}	
			most[key] = sales[key]

	return  most

def get_most_pop_cat(sales):
	most = {}
	cats = {"junk_food" : 0,
			"dairy" : 0,
			"not_edible"  : 0,
			"veg_and_carbs" : 0,
			"fruit" : 0}

	for key in sales:
		if key == "Milk 1l" or key == "Imasi":
			cats["dairy"] += sales[key]
		elif key == "Bread" or key == "Chakalaka Can" or key == "Gold Dish Vegetable Curry Can":
			cats["veg_and_carbs"] += sales[key]
		elif key == "Fanta 500ml" or key == "Coke 500ml" or key == "Cream Soda 500ml" or key == "Iwisa Pap 5kg" or key == "Top Class Soy Mince":
			cats["junk_food"] += sales[key]
		elif key == "Bananas - loose" or key == "Apples - loose":
			cats["fruit"] += sales[key]
		else:
			cats["not_edible"] += sales[key]

	val = cats.items()
	most[val[0][0]] = val[0][1]

	for key in cats:
		if most.values()[0] < cats[key]:
			most = {}	
			most[key] = cats[key]

	return  most