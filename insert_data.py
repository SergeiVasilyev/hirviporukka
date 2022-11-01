# FOR TESTING DATA INSERTS TO TABLE

# LIBRARIES AND MODULES
import psycopg2

# DB CONNECTION PARAMETERS

# Try to establish a connection to the server
try:
    dbconnection = psycopg2.connect(database="psycotesti", user="sovellus", password="Q2werty",
                                    host="localhost", port="5432")

    # Create a cursor to execute commands on the connection
    cursor = dbconnection.cursor()

    # Execute a command to insert a new record into person table -> transaction
    cursor.execute("INSERT INTO person (etunimi, sukunimi, tehopisteet) VALUES ('Mikko', 'Viljanen',70)")
    
    # Commit the transaction
    dbconnection.commit()
   
# Handle possible errors using the psycopg2 Error class
except (Exception, psycopg2.Error) as error:
    print("Virhe muodostettaess yhteyttä tietokantaan", error)

# Close the connection if estabilished
finally:
    
    if (dbconnection):

        # Close the cursor
        cursor.close()

        # Close the connection
        dbconnection.close()
        print("Yhteys tietokantaan suljettiin")