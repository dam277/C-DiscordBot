import mysql.connector

class Database:
    db_instance = mysql.connector.connect(
        host='localhost', user="root", password="Root@1q2w3e4"
    )

    def __init__(self):
        print(self.db_instance)
        mycursor = self.db_instance.cursor()
        mycursor.execute("SHOW DATABASES")
        for x in mycursor:
            print(x)

if __name__ == '__main__':
    db = Database()



class Car:
    def __init__(self, engine):
        self.engine = engine
        self.engine2 = Engine()

class Engine:
    def __init__(self):
        pass

e = Engine()
c = Car(e)

c = None