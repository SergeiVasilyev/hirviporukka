# APPLICATION FOR SHOWING SUMMARY DATA ABOUT MEAT GIVEN TO SHARE GROUP
# ====================================================================

# LIBRARIES AND MODULES 
# ---------------------

import sys
import psycopg2
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

import pgModule
import prepareData

# CLASS DEFINITIONS FOR THE APP
# -----------------------------

class GroupMainWindow(QMainWindow):

    # Constructor, a method for creating objects from this class
    def __init__(self):
        QMainWindow.__init__(self)

        # Create an UI from the ui file
        loadUi('GroupInfoMainWindow.ui', self)

        # Define properties for ui elements
        self.refreshBtn = self.refreshPushButton
        self.groupInfo = self.groupSummaryTableWidget
        self.sharedMeatInfo = self.meatSharedTableWidget

        # # Database connection params
        # self.database = "metsastys"
        # self.username = "sovellus"
        # self.userPassword = "Q2werty"
        # self.server = "127.0.0.1"
        # self.port = "5432"

        # Signals

        # Emit a signal when refresh push button is pressed
        self.refreshBtn.clicked.connect(self.agentRefreshData)

   # SLOTS

    # Agent method is used for receiving a signal from an UI element

    def agentRefreshData(self):
        # Read data from view jaetut_lihat
        databaseOperation1 = pgModule.DatabaseOperation()
        connectionArguments = databaseOperation1.readDatabaseSettingsFromFile('settings.dat')
        databaseOperation1.getAllRowsFromTable(connectionArguments, 'public.jaetut_lihat')
        print(databaseOperation1.detailedMessage)

        # Read data from view jakoryhma_yhteenveto, no to read connection args twice
        databaseOperation2 = pgModule.DatabaseOperation()
        databaseOperation2.getAllRowsFromTable(connectionArguments, 'public.jakoryhma_yhteenveto')
        print(databaseOperation2.detailedMessage)

        # Let's call the real method which updates the widget
        self.refreshData(databaseOperation1, self.sharedMeatInfo)
        self.refreshData(databaseOperation2, self.groupInfo)


    # This is a function that updates table widgets in the UI, becouse it does not receive signals it's not called slot
    def refreshData(self, databaseOperation, widget):
        prepareData.prepareTable(databaseOperation, widget)
    
    # # Load data to table Widgets
    # # Try to establish a connection to DB server
    # def refreshData(self):

    #     # To avoid Fatal error crashing the app uses try-except-finaly structure
    #     try:
    #         # Create a connection object
    #         dbaseconnection = psycopg2.connect(database=self.database, user=self.username, password=self.userPassword,
    #                                         host=self.server, port=self.port)
            
    #         # Create a cursor to execute commands and retrieve result set
    #         cursor = dbaseconnection.cursor()
            
    #         # Execute a SQL command to get hunters (jasen)
    #         command = "SELECT * FROM public.jaetut_lihat;"
    #         cursor.execute(command)
    #         result_set = cursor.fetchall()
    #         print("Jäsentiedot ovat:", result_set)

    #     # Throw an error if connection or cursor creation fails                                     
    #     except(Exception, psycopg2.Error) as e:
    #         print("Tietokantayhteydessä tapahtui virhe", e)

    #     # If or if not successfull close the cursor and the connection   
    #     finally:
    #         if dbaseconnection:
    #             cursor.close()
    #             dbaseconnection.close()
    #             print("Yhteys tietokantaan katkaistiin")

# APPLICATION CREATION AND STARTING
# ---------------------------------

if __name__ == "__main__":

    # Create an application object
    app = QApplication(sys.argv)
    # app.setStyle('Fusion')

    # Create the Main Window object from FormWithTable Class and show it on the screen
    appWindow = GroupMainWindow()
    appWindow.show() # Show method can also be used in the FormWithTable class
    sys.exit(app.exec_())



