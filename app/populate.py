import godutch
import os


def populate():
    if os.path.isfile('./godutch.db'):
        os.remove('./godutch.db')

    godutch.init_db()
    generate_accounts()


def generate_accounts():
    godutch.query_db('insert into account (name) values (?)', ['Anna Ida'])
    godutch.query_db('insert into account (name) values (?)', ['Youri'])
