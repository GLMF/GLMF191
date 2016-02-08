"""
    Connexion à la base de données

    Author: Tristan Colombo <tristan@gnulinuxmag.com>
                            (@TristanColombo)

    Date: 25-09-2014

    Last modification: 25-09-2014

    Licence: GNU GPL v3 (voir fichier gpl_v3.txt joint)
"""

import sqlite3

def create_db():
    base = sqlite3.connect('base.db')
    cursor = base.cursor()

    try:
        cursor.execute("""create table Contact
                       (idContact integer primary key,
                       name text,
                       forename text,
                       mail text)""")
        base.commit()
    except sqlite3.OperationalError:
        pass

    return (base, cursor)


def close_db(base, cursor):
    cursor.close()
    base.close()
