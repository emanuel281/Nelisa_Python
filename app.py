from flask import Flask, render_template, request
from flask.ext.mysql import MySQL
import spaza_shop

app = Flask(__name__)

mysql = MySQL()
app.config['DEBUG'] = True

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'MysqlServer123'
app.config['MYSQL_DATABASE_DB'] = 'spaza_shop'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

connection = mysql.connect()
cursor = connection.cursor()

# url_for('static', filename='main_page.css')
# url_for('static', filename='bootstrap.min.css')
# url_for('static', filename='bootstrap.min.js')
# url_for('static', filename='jquery.js')

@app.route('/popular_category/')
def popular_category():
	sales = spaza_shop.get_sales()
	most_pop_cat = spaza_shop.get_most_pop_cat(sales)

	cursor.execute('SELECT cat_name, SUM(no_sold) AS no_sold FROM sales_history INNER JOIN categories ON category_name=categories.cat_name GROUP BY cat_name ORDER BY no_sold DESC')
	data = cursor.fetchall()
	if len(data) is 0:
		return render_template('popular_category.html', result=most_pop_cat)

	return render_template('popular_category.html', result=data)

@app.route('/popular_product/')
def popular_product():
	sales = spaza_shop.get_sales()
	most_pop = spaza_shop.get_most_pop_item(sales)

	cursor.execute('SELECT * FROM product_sold ORDER BY no_sold DESC LIMIT 0,1')
	data = cursor.fetchall()
	if len(data) is 0:
		return render_template('popular_product.html', result=most_pop)

	return render_template('popular_product.html', result2=data)
	# print result

@app.route('/sales/')
def sales():
	sales = spaza_shop.get_sales()

	cursor.execute('SELECT * FROM product_sold ORDER BY no_sold DESC')
	data = cursor.fetchall()
	if len(data) is 0:
		return render_template('sales.html', result=sales)

	return render_template('sales.html', result2=data)

@app.route('/', defaults={'path' : ''})
@app.route('/<path:path>/')
def index(path):
    return render_template('main.html', path=path)
#Try to redirect requests to non-existent pages


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return '''
#         <form action="" method="post">
#             <p><input type=text name=username>
#             <p><input type=submit value=Login>
#         </form>
#     '''

# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))

# # set the secret key.  keep this really secret:
# app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
	app.run()