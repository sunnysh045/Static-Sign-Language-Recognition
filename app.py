import streamlit as st
import tensorflow as tf
import streamlit.components.v1 as components

st.set_option('deprecation.showfileUploaderEncoding',False)
st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('C:\\static_sign\\sign_lang_model_first.h5')
    return model
model = load_model()
st.write(
    """
     Static Sign Langauge to Text Image Classification
    """
)
file = st.file_uploader("Please Upload an image of sign", type=["jpg","png"])
import cv2 as cv
from PIL import Image,ImageOps
import numpy as np

def import_and_predict(image_data, model):
    size = (96,96)
    image = ImageOps.fit(image_data,size,Image.ANTIALIAS)
    img = np.asarray(image)
    #img_reshape = img[...,np.newaxis]
    img_reshape = img.reshape(-1,96,96,1)
    #IMG_SIZE =  96
    #new_array = cv.resize(filepath, (IMG_SIZE, IMG_SIZE))
    #img_reshape = new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1) 
    prediction = model.predict(img_reshape)
    return prediction

if file is None:
    st.text("Please Upload an Image File")
else:
    image = Image.open(file)
    st.image(image,use_column_width=True)
    predictions = import_and_predict(image,model)
    class_names = ["A", "B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]
    string = "This Sign Gesture most likely is: " + class_names[np.argmax(predictions)]
    st.success(string)
