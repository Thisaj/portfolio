# import random
#
# lower_bound = int(input("Enter the lower bound: "))
#
# upper_bound = int(input("Enter the upper bound: "))
#
# random_number = random.randint(lower_bound, upper_bound)
#
# print(random_number)

# -----------------------------------------------------------

# import streamlit as st
# from PIL import Image
#
# st.subheader("color to grayscale converer")
#
# with st.expander("start camera"):
#     camera_image = st.camera_input("camera")
#     if camera_image:
#         img = image.open(camera_image)
#         gray_camera_img = img.convert('L')
#         st.image(gray_camera_img, caption='grayscale from camera', use_column_width=True)
#
# uploaded_image = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])
# if uploaded_image:
#     img = Image.open(uploaded_image)
#     gray_uploaded_img = img.convert('L')
#     st.image(gray_uploaded_img, caption='grayscale from uploaded image', use_column_width=True)

# ------------------------------------------------------------------------------

import PySimpleGUI as sg

label = sg.Text('converter')

window = sg.Window("converter",
                   layout=[label])

feet_inches = input("Enter feet and inches: ")
def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}
def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters
parsed = parse(feet_inches)
result = convert(parsed["feet"], parsed["inches"])
print(f"{parsed['feet']} feet and {parsed['inches']} is a qual to {result}")