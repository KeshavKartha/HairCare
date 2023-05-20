from flask import Flask, render_template, request
from flask import redirect, url_for
import predictor2

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/input_page', methods=['GET'])
def input_page():
    return render_template('input_page.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    input1 = request.form.get('age')
    input2 = 'CMF'
    input3 = '0'
    input4 = '0'
    input5 = '150'
    data_string = ','.join([input2,input5,input1,input3,input4])
    
    
    print(data_string)
    prediction = (predictor2.predict(data_string))
    print(prediction)
    #Prediction: 0->Complete, 1->None, 2->Partial

    if(prediction==0):
        return render_template('output_hairloss.html')
    elif(prediction==1):
        return render_template('output_nohairloss.html')
    else:
        return render_template('output_partialloss.html')

