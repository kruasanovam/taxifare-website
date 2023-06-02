import streamlit as st
import datetime as dt
import requests
import base64

st.markdown("""#:white[Welcome to this amazing TaxiFareModel]
##:white[Let's do some fancy prediction]""")

'''
:white[Please specify the details of your imaginary ride]
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

url = 'https://masha-qjpoayquoq-ew.a.run.app/predict'

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
    fare = "{:.2f}".format(prediction["fare_amount"])
    st.title("YOUR IMAGINARY FAIR PRICE IS")
    st.write({fare})




    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True
        )

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('taxi.jpg')
