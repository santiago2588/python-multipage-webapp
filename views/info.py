import streamlit as st

from forms.contact import contact_form


@st.experimental_dialog("Contacto")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/logo_original.png", width=230)

with col2:
    st.title("Soluciones digitales", anchor=False)
    st.write(
        "Ciencia de datos aplicada a la Industria."
    )
    if st.button("✉️ Contactanos"):
        show_contact_form()


# --- SERVICES ---
st.write("\n")
st.subheader("Servicios", anchor=False)
st.write(
    """
    - Desarrollo de modelos de Inteligencia Artificial
    - Estudios de eficiencia energetica en procesos industriales
    - Analisis de Ciclo de Vida de productos y procesos industriales
    - Desarrollo de plataformas digitales para la industria 4.0
    """
)

# --- PRODUCTS ---
st.write("\n")
st.subheader("Productos", anchor=False)
st.write(
    """
    - AutoAI-Regresion
    - AutoAI-Clasificacion
    """
)
