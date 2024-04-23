from flask import Flask, render_template
import csv

# Starting a Flask web app
app = Flask(__name__)

# Setting up a route at the homepage URL
@app.route('/')
def show_tables():
    try:
        # Trying to open and read the CSV file with our data
        with open('Table_Input.csv', mode='r') as infile:
            reader = csv.reader(infile)  # Using the csv module to read the file
            headers = next(reader)  # Getting the headers from the first row
            data_list = list(reader)  # Reading the rest of the data into a list

        # Performing some calculations from the data we just read
        # We're using specific rows and making sure to convert strings to integers or floats as necessary
        alpha = int(data_list[4][1]) + int(data_list[19][1])  # Summing values from the specified rows for Alpha
        beta = int(round(float(data_list[14][1]) / float(data_list[6][1])))  # Calculating Beta and rounding it
        charlie = int(data_list[12][1]) * int(data_list[11][1])  # Multiplying values for Charlie
    
    except FileNotFoundError:
        # If the CSV file isn't found, let the user know
        return "Error: The data file was not found.", 404
    
    except IOError:
        # Catch any input/output errors that might occur
        return "Error: Unable to read the data file.", 500

    except ValueError as e:
        # If there's an error converting data types, let's catch it and tell the user
        return f"Error converting CSV values to integers or floats: {e}", 500

    # If all goes well, render the webpage with the tables and calculated values
    return render_template('tables.html', headers=headers, data_list=data_list, alpha=alpha, beta=beta, charlie=charlie)