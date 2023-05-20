import pandas as pd
import pickle
import joblib
from sklearn.preprocessing import StandardScaler, LabelEncoder


#Load the saved models 
classifier = joblib.load('C:/Users/Keshav/Downloads/saved_model.pkl')

# format given new data
def format_input(new_data):
    arr = pd.DataFrame({"Chemotherapy_Regimen":[new_data[0]], "Drug_Dosage(mg)":[new_data[1]], "Age":[new_data[2]], "Hypertension":[new_data[3]], "Family_History":[new_data[4]]})

    return arr

def predict(new_data):
    new_data = new_data.split(',')
    if(new_data[0]=='ABVD'):
        new_data[0]=0
    elif(new_data[0]=='BEP'):
        new_data[0]=1
    elif(new_data[0]=='CMF'):
        new_data[0]=2

    arr = format_input(new_data)

    prediction = classifier.predict(arr)

    if prediction[0]==1:
        return ("Low chances of hair loss!")
    elif prediction[0]==2:
        return ("High chance of partial hair loss")
    else:
        return ("High chances of complete hair loss")

print(predict('ABVD,337,52,1,1'))
print(predict('CMF,250,21,0,0'))
