import sqlite3
from sqlalchemy import *


def main():

    conn = sqlite3.connect('database/gazprom_data.db')
    cur = conn.cursor()



if __name__ == '__main__':
    main()

