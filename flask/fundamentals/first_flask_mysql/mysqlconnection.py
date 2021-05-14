# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', # change the user and password as needed
                                    password = 'romeoalpha123!', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        self.connection = connection # establish the connection to the database
    def query_db(self, query, data=None):  # the method to query the database
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0: # if the query is an insert, return the id of the last row, since that is the row we just added, # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0: # if the query is a select, return everything that is fetched from the database, # SELECT queries will return the data from the database as a LIST OF DICTIONARIES # the result will be a list of dictionaries
                    result = cursor.fetchall()
                    return result
                else: 
                    self.connection.commit() # if the query is not an insert or a select, such as an update or delete, commit the changes # return nothing
            except Exception as e:
                # in case the query fails
                print("Something went wrong", e)
                return False
            finally:
                self.connection.close() # close the connection

# this connectToMySQL function creates an instance of MySQLConnection, which will be used by server.py
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)