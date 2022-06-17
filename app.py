import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu



# Ubah icon dan nama page tab
img = Image.open('Bendera_Indonesia.jpg')
st.set_page_config(page_title='Bathik.Id', page_icon=img, layout="wide")


st.set_option('deprecation.showfileUploaderEncoding', False)

@st.cache(allow_output_mutation=True)

# load modelling
def load_model():
	model = tf.keras.models.load_model('model_percobaan_v5.h5')
	return model


def predict_class(image, model):

	image = tf.cast(image, tf.float32)
	image = tf.image.resize(image, [180, 180])

	image = np.expand_dims(image, axis = 0)

	prediction = model.predict(image)

	return prediction

model = load_model()
# with st.sidebar:
#         selector = st.selectbox(
#         label = "Menu",
#         options = ["Beranda", "Gambar", "Kamera", "Tentang Kami"],
#         )

# Buat UX page horizontal
selector = option_menu(None, ["Beranda", "Gambar",  "Kamera", 'Tentang Kami'], 
    icons=['house', 'cloud-upload', "camera", 'people'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#2eb9c3" },
        "icon": {"color": "#7fdf28", "font-size": "14px"}, 
        "nav-link": {"font-size": "20px", "text-align": "center", "margin":"8px", "--hover-color": "#eee"},
         "nav-link-selected": {"background-color": "#f9a930"},
    }
)

if selector == "Beranda":
        st.header("Halo! Ini adalah aplikasi Bathik")
        # st.write("Batik merupakan...")

elif selector == "Gambar":
        data = st.file_uploader("Silakan Unggah Gambar Batik Anda", type=["jpg", "jpeg", "png"])

elif selector == "Kamera":
        # st.markdown("<h2 styke='text-align: center; color; white; '>PINDAI</h2>", unsafe_allow_html=True)
        # with selector :
        #  agree = 
        nyalakan = st.checkbox('Buka Kamera')
        # if agree == True
        if nyalakan:
                data = st.camera_input("Ambil sebuah gambar batik")

elif selector == "Tentang Kami":
        st.header("Kelompok 5 dari Kelas Ibnu Sina")
        st.markdown("""
        Kasih Lidiya Br Nadeak,
        Nyanyang Rian,
        Rahayu Adha Putri,
        Ramolo Berutu,
        Walid Miftahuddin.
        """)
try:
        st.image(data)
        
except:
       # st.warning("No image uploaded!")
        st.stop()


if data is not None:
    # else:
    #     slot = st.empty()
    #     slot.text('Running inference....')
    # test_image = Image.open(data)

    # st.image(test_image, caption="Input Image", width = 400)

    pred = predict_class(np.asarray(Image.open(data)), model)

        #class_names = ['Bali', 'Cirebon', 'Pekalongan', 'Jogja', 'Surabaya']

    result = np.argmax(pred)
    if result == 0:
            st.subheader(" Ini adalah Batik Bali")
    elif result == 1:
            st.subheader(" Ini adalah Batik Betawi")
    elif result == 2:
            st.subheader(" Ini adalah Batik Cendrawasih")
    elif result == 3:
            st.subheader(" Ini adalah Batik Dayak")
    elif result == 4:
            st.subheader(" Ini adalah Batik Geblek Renteng")
    elif result == 5:
            st.subheader(" Ini adalah Batik Ikat Celup")
    elif result == 6:
            st.subheader(" Ini adalah Batik Insang")
    elif result == 7:
            st.subheader(" Ini adalah Batik Kawung")
    elif result == 8:
            st.subheader(" Ini adalah Batik Lasem")
    elif result == 9:
            st.subheader(" Ini adalah Batik Megamendung")
    elif result == 10:
            st.subheader(" Ini adalah Batik Pala")
    elif result == 11:
            st.subheader(" Ini adalah Batik Parang")
    elif result == 12:
            st.subheader(" Ini adalah Batik Poleng")
    elif result == 13:
            st.subheader(" Ini adalah Batik Sekar Jagad")
    elif result == 14:
            st.subheader(" Ini adalah Batik Tambal")
    else:
        result >=15
        st.write(" Batik ini tidak ada dalam basis data ")

st.balloons()

	#output = 'The image is a ', result

# slot.text('Done')

	#st.success(output)
