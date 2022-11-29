# MODULE FOR PREPARING DATA TO DISPLAY IT ON QT WIDGETS
# =====================================================


# LIBRARIES AND MODULES
# ---------------------

import pgModule
# from PyQt5.QtWidgets import * # remove this line when ready

from PyQt5.QtWidgets import QTableWidgetItem # For handling a single table cell

# Temporary object to get help about object properties
# resultObject = pgModule.DatabaseOperation()
# testConnectionArgs = resultObject.readDatabaseSettingsFromFile('settings.dat')
# resultObject = resultObject.getAllRowsFromTable(testConnectionArgs, 'public.jakoryhma_yhteenveto')

# testTableWidget = QTableWidget()

# Data preparation functions
# --------------------------

def prepareTable(resultObject, tableWidget):
    """ Updates an existing TableWidget using an instance of DatabeseOperation class defined in the pgModule

    Args:
        resultObject (DatabaseOperstion): Instance of DatabaseOperstion class -> errors and results
        tableWidget (QTableWidget): Table widget to be updated
    
    """
    if resultObject.errorCode == 0:
        tableWidget.setRowCount(resultObject.rows)
        tableWidget.setColumnCount(resultObject.columns)
        tableWidget.setHorizontalHeaderLabels(resultObject.columnHeaders)

        rowIndex = 0
        for tupleIx in resultObject.resultSet:
            columnIndex = 0
            for cell in tupleIx:
                cellData = QTableWidgetItem(str(cell))
                tableWidget.setItem(rowIndex, columnIndex, cellData)
                columnIndex += 1
            rowIndex += 1







