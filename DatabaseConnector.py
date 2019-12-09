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

    def query(self,QRY):
        self.mySQLquery.query(QRY)
        self.results = self.mySQLquery.use_result()

    def return_response(self, num_to_return=1):
        return self.results.fetch_row(num_to_return,1)