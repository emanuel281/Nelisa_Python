import csv

with open("Nelisa Sales History.csv") as sales_file:
	sales_history = csv.reader(sales_file, delimiter=";")
	sales = {}
	for line in sales_history:
		if line[2] == 'stock item':
			print
		elif line[2] not in sales:
			sales[line[2]] = int(line[3])
		else:
			sales[line[2]] += int(line[3])

	print sales