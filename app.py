
import os
import gdown
import tensorflow as tf
import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from PIL import Image

# Load trained model
MODEL_PATH = "tb_cnn_model.keras"

if not os.path.exists(MODEL_PATH):
    url = "https://drive.google.com/uc?id=1szP-fOXMJh70e0Di8f7-ea1x8cx8T9ix"
    gdown.download(url, MODEL_PATH, quiet=False)

model = tf.keras.models.load_model(MODEL_PATH)


IMG_SIZE = 224

st.set_page_config(page_title="TB Detection App", layout="centered")

st.title("🩺 AI-based Tuberculosis Screening")
st.write("Upload a chest X-ray image to assess TB risk.")

st.warning(
    "⚠️ This application is for educational and screening purposes only. "
    "It does NOT provide a medical diagnosis."
)

uploaded_file = st.file_uploader(
    "Upload Chest X-ray Image",
    type=["png", "jpg", "jpeg"]
)

def preprocess_image(image):
    image = np.array(image.convert("L"))  # convert to grayscale
    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
    image = image / 255.0
    image = np.expand_dims(image, axis=(0, -1))
    return image

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded X-ray", use_column_width=True)

    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)[0][0]

    st.subheader("Prediction Result")

    if prediction > 0.5:
        st.error(f"⚠️ High TB Risk Detected (Probability: {prediction:.2f})")
    else:
        st.success(f"✅ Low TB Risk (Probability: {prediction:.2f})")
