import MySQLdb

class DatabaseConnector:
    def __init__(self):
        self.mySQLquery  = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Epf#31032",
            auth_plugin="mysql_native_password",
            database="mypantry"
        )
        self.mySQLcursor = self.mySQLquery.cursor()

    def query(self,QRY):
        self.mySQLcursor.execute(QRY)

    def return_response(self, num_to_return=1):
        return self.mySQLcursor.fetchmany(num_to_return)

    def save_changes(self):
        self.mySQLquery.commit()
