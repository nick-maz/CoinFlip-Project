import streamlit as st

st.header('Tossing a Coin')

# Adding the slider for number of trials
number_of_trials = st.slider('Number of trials?', 1, 1000, 10)

# Adding the button to start the experiment
start_button = st.button('Run')

# Action to take when the button is pressed
if start_button:
    st.write(f'Running the experiment of {number_of_trials} trials.')

# You can place this line either before or after the slider and button.
# If placed after, it will appear at the bottom of your web app.
st.write('It is not a functional application yet. Under construction.')
