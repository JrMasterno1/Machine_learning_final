import streamlit as st

st.write("""My first app""")
Image = st.file_uploader("Pick a file")
if Image is not None:
    image = Image.convert('RGB')
    st.write(image)
    # boxes = [line[0] for line in result]
    # txts = [line[1][0] for line in result]
    # scores = [line[1][1] for line in result]
    # im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/vni.common.VTIMESN.ttf')
    # im_show = Image.fromarray(im_show)
    # im_show.save('result.jpg')