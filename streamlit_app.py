import streamlit as st

from src.pipeline.predict_pipeline import Predictpipeline, CustomData

# Route to home page
def index():
    st.title('Student Performance Prediction')
    st.write('Please fill in the following details:')
    gender = st.selectbox('Gender', ['male', 'female'])
    race_ethnicity = st.selectbox('Ethnicity', ['group A', 'group B', 'group C', 'group D', 'group E'])
    parental_education = st.selectbox('Parental Education', ['some high school', 'high school', 'some college', "associate's degree", "bachelor's degree", "master's degree"])
    lunch = st.selectbox('Lunch Type', ['standard', 'free/reduced'])
    test_prep = st.selectbox('Test Preparation Course', ['none', 'completed'])
    reading_score = st.number_input('Reading Score', min_value=0, max_value=100)
    writing_score = st.number_input('Writing Score', min_value=0, max_value=100)
    
    if st.button('Predict'):
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_education,
            lunch=lunch,
            test_preparation_course=test_prep,
            reading_score=float(reading_score),
            writing_score=float(writing_score)
        )
        pred_df = data.get_data_as_data_frame()
        
        predict_pipeline = Predictpipeline()
        results = predict_pipeline.predict(pred_df)
        
        if results >= 100 or results >= 90:
            st.success('Results: 100')
            st.write('Keep up the good work!')
        elif results <= 90 and results >= 70:
            st.success(f'Results: {results}')
            st.write('Good work!')
        elif results <= 70 and results >= 35:
            st.warning(f'Results: {results}')
            st.write('You must work hard.')
        elif results < 35:
            st.error(f'Results: {results}')
            st.write('You failed.')
        else:
            st.write(f'Results: {results}')

if __name__ == '__main__':
    index()
