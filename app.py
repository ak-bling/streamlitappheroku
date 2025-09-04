# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 10:57:07 2025

@author: user
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loding the saved models

diabetes_model=pickle.load(open('diabetes_model.sav','rb'))

heart_disease_model=pickle.load(open('heart_disease_model.sav','rb'))

parkinsons_model=pickle.load(open('parkinsons_model.sav','rb'))



# sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction Sytem',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           
                           icons=['activity','heart','person'],  # just search icons on bootsrap icons
                           
                           default_index=0)   #index=0-- just giving the starting page click in the side bar whixh is the diabetes predicton on side bar
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from user
    # columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose=st.text_input('Glucose Level')  
    
    with col3:
        BloodPressure=st.text_input('BloodPressure Value') 
    
    with col1:
        SkinThickness=st.text_input('Skin Thickness Value')
    
    with col2:
        Insulin=st.text_input('Insulin Level')
        
    with col3:
        BMI=st.text_input('BMI Value')
    
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
        
    with col2:
        Age=st.text_input('Age of the Person')
        
        
    
    # the code for prediction
    diab_diagnosis=''
    
    # creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis = 'The Person is Diabetic'
            
        else:
            diab_diagnosis = 'The Person is Not Diabetic'
            
        
    st.success(diab_diagnosis)
    

# Heart Disease Prediction Page    
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    
# Parkinsons Prediction Page    
if (selected == 'Parkinsons Prediction'):
    
    # page title
    st.title('Parkinsons Prediction using ML')