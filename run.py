import pandas as pd
from flask import Flask, render_template, request
app = Flask(__name__)

#need pip install pandas & xlrd for this to work



@app.route('/')
def hello():
   df = pd.read_excel("/home/admin/Desktop/FlaskExcel/SampleData.xlsx")
   return df.to_html()


if __name__ == '__main__':
   app.run(debug = True)
