import streamlit as st
import datetime as dt
import requests
from PIL import Image
import base64

st.markdown("""# Welcome to this amazing TaxiFareModel front
## Let's do some fancy prediction""")

'''
Please specify the details of your imaginary ride
'''

with st.form(key='my_form'):
    date = st.date_input("Please provide pick-up date")
    time = st.time_input('Please provide pick-up time')
    pickup_longitude = st.number_input('Please provide pickup longitude')
    pickup_latitude = st.number_input('Please provide pickup latitude')
    dropoff_longitude = st.number_input('Please provide dropoff longitude')
    dropoff_latitude = st.number_input('Please provide dropoff latitude')
    passenger_count = st.number_input('Please provide number of passengers')
    submit_button = st.form_submit_button(label='Submit')
    datetime = dt.datetime.combine(date, time)

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

##Let's build a dictionary containing the parameters for our API...
data = {
        "pickup_datetime": str(datetime),
        "pickup_longitude": float(pickup_longitude),
        "pickup_latitude": float(pickup_latitude),
        "dropoff_longitude": float(dropoff_longitude),
        "dropoff_latitude": float(dropoff_latitude),
        "passenger_count": int(passenger_count)
}

#Let's call our API using the `requests` package...
#Let's retrieve the prediction from the **JSON** returned by the API...
#Finally, we can display the prediction to the user

### gif from local file
file_ = open("spongebob-magic.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()


if submit_button:
    resp = requests.get(url, params=data)
    prediction = resp.json()
    fare = prediction["fare"]
    st.write(f"YOUR IMAGINARY FAIR PRICE IS {fare}")
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True
        )