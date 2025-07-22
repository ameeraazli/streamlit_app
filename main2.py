#Testing this out, if it works: passed ✅
import streamlit as st

st.write("Hello World")
st.header("Hello World!")
st.subheader("Hello World!")
st.caption("Hello Wrld!")

st.markdown("*Streamlit* is **fire** 🔥")
st.success("good")
st.warning("bad")
st.info("info")
st.error("Error!")

location = st.selectbox("Kuala Lumpur is located at", ["Malaysia", "Thailand", "UK"])

st.write("Country is", location)

location = st.multiselect("Select 2 states",["Selangor", "Johor", "Kedah"])

st.write("States are", location)

st.write("States are", ",".join(location))

st.button("Click this.")
day = st.slider("Select the length if stay", 1, 10, value = 3)

st.write("Day=", day)

number = st.number_input("Insert a number",
                         value = 3, placeholder = "Type a number: ")

st.write("The current number is", int(number))

# path= r"./file/intel.png"
# from PIL import Image

# im = Image.open(path)
# st.image(im, width = 150)

# col1, col2, col3 = st.columns(3)
# with col1:
#   im = Image.open(path)
#   st.image(im, width = 150)
#   st.slider("day",
#             1, 10, value = 3
#     )

# with col2:
#   #

# with col3:
#   #

tab1, tab2, tab3 = st.tabs(["Button", "Slider", "Logo"])
with tab1:
  st.button("Click this button")
with tab2:
  st.slider("E: ", 1, 10)
# with tab3:
#   im = Image.open(path)
#   st.image(im, width = 150)



####-------------------------------------------------------------####