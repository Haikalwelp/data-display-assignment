from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def show_tables():
    with open('Table_Input.csv', mode='r') as infile:
        reader = csv.reader(infile)
        headers = next(reader)  
        data_list = list(reader)  

    try:
        alpha = int(data_list[4][1]) + int(data_list[19][1]) 
        beta = int(round(float(data_list[14][1]) / float(data_list[6][1])))
        charlie = int(data_list[12][1]) * int(data_list[11][1])  
    except ValueError as e:
        return f"Error converting CSV values to integers or floats: {e}"

    return render_template('tables.html', headers=headers, data_list=data_list, alpha=alpha, beta=beta, charlie=charlie)

if __name__ == '__main__':
    app.run(debug=True)
