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
    input1 = str(request.form.get('age'))
    # if(request.form.get('option')=='option2'):
    #     input2 = 'ABVD'
    # elif(request.form.get('option')=='option3'):
    #     input2 = 'BEP'
    # else: input2 = 'CMF'
    input2 = request.form.get('regimen')
    if(request.form.get('hairloss')=='on'):
        input4 = '1'
    else: input4 = '0'
    if(request.form.get('hypertension')=='on'):
        input3 = '1'
    else: input3 = '0'
    input5 = str(request.form.get('drug'))
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

@app.route('/output_nohairloss', methods=['GET'])
def output_nohairloss():
    return render_template('output_nohairloss.html')
