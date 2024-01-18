import numpy as np
import pandas as pd
import streamlit as st
import pickle


model = pickle.load(open('model.pkl','rb'))
cols = ['Age', 'Income', 'LoanAmount', 'CreditScore', 'MonthsEmployed',
          'InterestRate', 'DTIRatio']


def main():
    st.title('Predicting Loan Defaults')
    st.markdown('ML model to predict if loan will default or not')
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Default Prediction App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    Age = st.text_input("Age", "Type Here") 
    Income = st.text_input("Income", "Type Here")
    LoanAmount = st.text_input("Loan Amount", "Type Here")
    CreditScore = st.text_input("Credit Score (0-1000)", "Type Here")
    MonthsEmployed = st.text_input("Months Employed", "Type Here") 
    InterestRate = st.text_input("Interest Rate (0 - 30)", "Type Here")
    DTIRatio = st.text_input("DTIRatio (0 - 1)", "Type Here")

    if st.button("Predict"):
        features = [Age, Income, LoanAmount, CreditScore, MonthsEmployed, InterestRate, DTIRatio]
        data = {'Age': int(Age), 'Income': int(Income), 'LoanAmount': int(LoanAmount), 'CreditScore': int(CreditScore),'MonthsEmployed': int(MonthsEmployed),'InterestRate': int(InterestRate),'DTIRatio': float(DTIRatio)}
        print(data)
        df=pd.DataFrame([list(data.values())], columns=['Age', 'Income', 'LoanAmount', 'CreditScore', 'MonthsEmployed',
          'InterestRate', 'DTIRatio'])
            
        features_list = df.values.tolist()      
        prediction = model.predict(features_list)
    
        output = int(prediction[0])
        if output == 1:
            text = "DEFAULT"
        else:
            text = "NOT DEFAULT"

        st.success('This loan is likely to {}'.format(text))
      
if __name__=='__main__': 
    main()
