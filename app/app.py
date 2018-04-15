from godutch import *


TOKEN_AMOUNT = 13

@app.route("/")
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        result = query_db('select name from account where name=?', [request.form['name']])

        if not result:
            error = 'User not found'
        else:
            session['user'] = result
            return redirect(url_for('group'))

    return render_template('login.html', error=error)


@app.route("/group")
def group():
    accounts = query_db('select name, tokens from account')
    return render_template('group.html', accounts=accounts)


@app.route("/overview")
def overview():
    amount = min([TOKEN_AMOUNT, 36])
    return render_template('overview.html', tokens=TOKEN_AMOUNT, amount=amount)


@app.route("/order")
def order():
    items = query_db('select name, price from menu')

    return render_template('order.html', items=items)
