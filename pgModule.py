# MODULE FOR CREATING DATABASE CONNECTION AND OPERATIONS
# ======================================================


# LIBRARIES AND MODULES
# ---------------------


import psycopg2
import datetime
import decimal
import json

# CLASS DEFINITIONS
# -----------------


class DatabaseOperation():
    """Create a connection to postgreSQL database
    and executes various SQL commands"""

    # Constructor method: create a new object and set initial properties
    def __init__(self):
        self.errorCode = 0
        self.errorMessage = 'OK'
        self.detailedMessage = 'No errors'
        self.resultSet = []
        self.columnHeaders = []
        self.rows = 0
        self.columns = 0

    # Method for creating connection arguments
    def createConnectionArgumentDict(self, database, role, pwd,
                                    host='localhost',
                                    port='5432'):
        """ Creates a dictionary from connection arguments 

        Args:
            database (str): Database name
            role (str): Role id username
            pwd (str): Password
            host (str, optional): Server name or IP adress. Default to 'localhost'
            port (str, optional): Server's TCP port. Default to '5432'

        Returns:
            dict: Connection args as key-value pairs

        """
        connectionArgumentsList = {}
        connectionArgumentsList['server'] = host
        connectionArgumentsList['port'] = port
        connectionArgumentsList['database'] = database
        connectionArgumentsList['user'] = role
        connectionArgumentsList['password'] = pwd
        return connectionArgumentsList

    # Method for saving connection args to settings file
    def saveDatabaseSettingsToFile(self, file, connectionArgs):
        """Saves connection arguments to JSON based settings file

        Args:
            file (str): Name of the JSON settings file
            connectionArgs (str): Connection args in key-value pairs     
        """
        settingsFile = open(file, 'w')
        json.dump(connectionArgs, settingsFile)
        settingsFile.close()

    # Method for reading connection args from the settings file
    def readDatabaseSettingsFromFile(self, file):
        """Reads connection arguments from JSON based settings file

        Args:
            file (str): Name of the settings file

        Returns:
            dict: Connection arguments in key-value pairs
        """
        
        settingsFile = open(file, 'r')
        connectionArgumentsList = json.load(settingsFile)
        settingsFile.close()
        return connectionArgumentsList


    # Method for get all rows from a given table
    def getAllRowsFromTable(self, connectionArgs, table):
        """Select all rows from the table

        Args:
            connectionArgs (dict): Connection args in key-value pairs
            table (str): Name of the table to read from 

        """
        server = connectionArgs['server']
        port = connectionArgs['port']
        database = connectionArgs['database']
        user = connectionArgs['user']
        password = connectionArgs['password']

        try:
            # Connect to the database and set error parameters
            dbconnection = psycopg2.connect(
                database=database, user=user, password=password, host=server, port=port)
            self.errorCode = 0
            self.errorMessage = 'Yhdestettiin tietokantaan'
            self.detailedMessage = 'Connected to database successfully'

            # Create a cursor to retrieve data from the table
            with dbconnection.cursor() as cursor:
                sqlClause = 'SELECT * FROM ' + table + ';'
                cursor.execute(sqlClause)

                # Set object properties
                self.rows = cursor.rowcount
                self.resultSet = cursor.fetchall()
                self.columnHeaders = [cname[0] for cname in cursor.description]
                self.columns = len(self.columnHeaders)

                # Set error values
                self.errorCode = 0
                self.errorMessage = 'Luettiin taule onnistuneesti'
                self.detailedMessage = 'Read all data from the table'

        except (Exception, psycopg2.Error) as error:
            # Set error values
            self.errorCode = 1
            self.errorMessage = 'Tietokannan käsittely ei onnistunut'
            self.detailedMessage = str(error)
        finally:
            if not self.errorCode:
                dbconnection.close()


    # Method to insert a row to a given table
    def insertRowToTable(self, connectionArgs, sqlClause):
        """Insert a row to table according to a SQL clause

        Args:
            connectionArgs (dict): Connection args in key-value pairs
            sqlClause (str): Insert clause
        """
        pass

    # Method to update a table
    def updateTable(self, connectionArgs, table, column, limit):
        """Insert a row to table according to a SQL clause

        Args:
            connectionArgs (dict): Connection args in key-value pairs
            table (str): Table name
            column (str): Column to be updated
            limit (_type_): WHERE SQL statment 
        """
        pass

    # Method to delete a row from table
    def deleteFromTable(self, connectionArgs, table, limit):
        """Delete a rows to table using limiting SQL statment

        Args:
            connectionArgs (dict): Connection args in key-value pairs
            table (str): Table name
            limit (_type_): WHERE SQL statment 
        """
        pass


# LOCAL TESTS, REMOVE WHEN FINISHED DESIGNING THE MODULE

if __name__ == "__main__":
    # Lets create a DatabaseOperation object
    testOperation = DatabaseOperation()
    # Create a dictionary for connection settings using defaults
    dictionary = testOperation.createConnectionArgumentDict(
        'metsastys', 'sovellus', 'Q2werty')
    '''
    print(dictionary)
    '''
    # Save those settings to file
    testOperation.saveDatabaseSettingsToFile('settings.dat', dictionary)

    # Read settings back from the file
    readedSettings = testOperation.readDatabaseSettingsFromFile('settings.dat')

    # print(readedSettings)
    testOperation.getAllRowsFromTable(readedSettings, 'public.jasen')

    print(testOperation.resultSet)


    