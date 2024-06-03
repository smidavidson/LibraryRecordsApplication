from TextUI import *
from DatabaseManager import *

import sqlite3
from sqlite3 import Error

def main():

    db_file = "library.db"


    databaseManager = DatabaseManager()
    databaseManager.create_connection(db_file)
    ui = TextUI(databaseManager)
    ui.start()

    databaseManager.close_connection()


if __name__ == "__main__":
    main()
