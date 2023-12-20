from mysql.connector.cursor import MySQLCursor 

class Table:
    @staticmethod
    def get_one_row(cursor: MySQLCursor) -> tuple:
        return cursor.fetchone()
    
    @staticmethod
    def get_all_rows(cursor: MySQLCursor) -> list:
        return cursor.fetchall()