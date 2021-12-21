import streamlit as st
import tensorflow as tf
import numpy as np
from paddleocr import PaddleOCR, draw_ocr
ocr = PaddleOCR(use_angle_cls=True, lang='en')



st.write("""My first app""")
image = st.file_uploader("Pick a file")
if image is not None:
    image = Image.read()
    image = tf.image.decode_image(Image, channels=3).numpy()    
    st.write(Image)
    st.image(Image)
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/vni.common.VTIMESN.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save('result.jpg')