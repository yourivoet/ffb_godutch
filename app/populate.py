import godutch
import os


def populate():
    if os.path.isfile('./godutch.db'):
        os.remove('./godutch.db')

    godutch.init_db()
    generate_accounts()
    godutch.get_db().commit()


def generate_accounts():
    godutch.query_db('insert into account (name, tokens) values (?, ?)', ['Anna Ida', 3])
    godutch.query_db('insert into account (name, tokens) values (?, ?)', ['Claire', 7.5])
    godutch.query_db('insert into account (name, tokens) values (?, ?)', ['Youri', 6.5])
