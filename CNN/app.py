import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.models.load_model('cnn_model.h5')


class_names = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]


st.title("CNN Image Classification App")

st.write("Upload an image and the CNN model will predict the class.")
uploaded_file = st.file_uploader(
    "Choose an image...",
    type=['jpg', 'jpeg', 'png']
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

   
    st.image(image, caption='Uploaded Image', use_container_width=True)

    
    image = image.resize((32, 32))
    image_array = np.array(image)

   
    image_array = image_array / 255.0

  
    image_array = np.expand_dims(image_array, axis=0)

   
    prediction = model.predict(image_array)

    predicted_class = class_names[np.argmax(prediction)]

    confidence = np.max(prediction) * 100

    st.subheader("Prediction")
    st.write(f"Predicted Class: {predicted_class}")
    st.write(f"Confidence: {confidence:.2f}%")
