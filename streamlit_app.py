import streamlit as st
import pickle
import requests

# URL to the raw pickle file on GitHub
PICKLE_URL = 'https://raw.githubusercontent.com/kushalasn/Streamlit_Nascent/main/mlr.pkl'

def load_model_from_github(url):
    try:
        # Fetch the pickle file from the GitHub raw URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for failed requests
        
        # Load the model using pickle
        model = pickle.loads(response.content)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def main():

    # giving the webpage a title
    st.title('Car fuel Efficiency')

    # the following code creates text boxes in which the user can enter
    # the data reqd to make the predictions

    c=st.number_input("Cylinder range")
    d=st.number_input("Displacement range")
    h=st.number_input("Horsepower range")
    w=st.number_input("Weight range")
    a=st.number_input("accelaration range")
    m=st.number_input("model year range")
    result=''

    if st.button('Predict'):
        result=mlr_prediction(c,d,h,w,a,m)
    if result is not None:
        st.success(result)
    else:
        st.error('prediction not valid')


if __name__=='__main__':
    main()
