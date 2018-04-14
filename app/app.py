from godutch import *


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        print(request.form['name'])
        result = query_db('select name from account where name=?', [request.form['name']])

        print(result)

        if not result:
            error = 'User not found'
        else:
            session['user'] = result
            return redirect(url_for('group'))

    return render_template('login.html', error=error)


@app.route("/group")
def group():
    db = get_db()
    cur = db.execute('select name from account')
    accounts = cur.fetchall()
    print(accounts)

    return render_template('group.html', accounts=accounts)


@app.route("/overview")
def overview():
    return render_template('overview.html')
