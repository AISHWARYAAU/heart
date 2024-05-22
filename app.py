import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))




# loading the saved models



heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))




# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Machine Learning Diseases Prediction System',
                           [
                            'Heart Disease Prediction',
                            
                          
                           ],
                           menu_icon='hospital-fill',
                           icons=['heart'],
                           default_index=0)



# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by fluoroscopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        try:
            user_input = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
                          float(restecg), float(thalach), float(exang), float(oldpeak), float(slope),
                          float(ca), float(thal)]
            heart_prediction = heart_disease_model.predict([user_input])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
            st.success(heart_diagnosis)
        except ValueError:
            st.error('Please enter valid numbers for all fields.')


           



# Running the app
if __name__ == '__main__':
    st.success('Welcome to the Health Assistant application!')

