import godutch
import os


def populate():
    if os.path.isfile('./godutch.db'):
        os.remove('./godutch.db')

    godutch.init_db()
    generate_accounts()
    godutch.get_db().commit()


def generate_accounts():
    godutch.query_db('insert into account (name) values (?)', ['Anna Ida'])
    godutch.query_db('insert into account (name) values (?)', ['Claire'])
    godutch.query_db('insert into account (name) values (?)', ['Youri'])


def generate_menu():
    godutch.query_db('insert into menu (name, price) values (?)', ['Beer', 1.0])
    godutch.query_db('insert into menu (name, price) values (?)', ['Coke', 1.0])
    godutch.query_db('insert into menu (name, price) values (?)', ['Water', 1.5])
