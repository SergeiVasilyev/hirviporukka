# APPLICATION FOR SHOWING SUMMARY DATA ABOUT MEAT GIVEN TO SHARE GROUP
# ====================================================================

# LIBRARIES AND MODULES 
# ---------------------

import sys
import psycopg2
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

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

        # Database connection params
        self.database = "metsastys"
        self.username = "sovellus"
        self.userPassword = "Q2werty"
        self.server = "127.0.0.1"
        self.port = "5432"

        # Signals

        # Emit a signal when refresh push button is pressed
        self.refreshBtn.clicked.connect(self.refreshData)
    
    # SLOTS
    # Load data to table Widgets
    # Try to establish a connection to DB server
    def refreshData(self):

        # To avoid Fatal error crashing the app uses try-except-finaly structure
        try:
            # Create a connection object
            dbaseconnection = psycopg2.connect(database=self.database, user=self.username, password=self.userPassword,
                                            host=self.server, port=self.port)
            
            # Create a cursor to execute commands and retrieve result set
            cursor = dbaseconnection.cursor()
            
            # Execute a SQL command to get hunters (jasen)
            command = "SELECT * FROM public.jaetut_lihat;"
            cursor.execute(command)
            result_set = cursor.fetchall()
            print("Jäsentiedot ovat:", result_set)

        # Throw an error if connection or cursor creation fails                                     
        except(Exception, psycopg2.Error) as e:
            print("Tietokantayhteydessä tapahtui virhe", e)

        # If or if not successfull close the cursor and the connection   
        finally:
            if dbaseconnection:
                cursor.close()
                dbaseconnection.close()
                print("Yhteys tietokantaan katkaistiin")

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



