import streamlit as st

st.title("Interactive Streamlit App")

# Text input
comment = st.text_input("Enter your comment:")

# Radio button group
option = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])

# Slider
value = st.slider("Select a value:", min_value=0, max_value=100, value=50)

# Checkbox to show/hide a message
if st.checkbox("Show message"):
    st.write("TE AMOOOOOOOOOOOOOOOOOO!")

# Display current values
st.subheader("Current Input Values:")
st.write(f"Comment: {comment}")
st.write(f"Selected option: {option}")
st.write(f"Slider value: {value}")

# Button to generate a message
if st.button("Generate Message"):
    st.success(f"You selected '{option}' and set the value to {value}. MENSAJE GENERADO")
