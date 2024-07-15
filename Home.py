import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/info.py",
    title="Informacion",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "views/regresion.py",
    title="Modelo de Regresion",
    icon=":material/timeline:",
)
project_2_page = st.Page(
    "views/clasificacion.py",
    title="Modelo de Clasificacion",
    icon=":material/event_list:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Proyectos": [project_1_page, project_2_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/logo_blanco.png")
st.sidebar.markdown("Made with ❤️ by [Pungo](https://www.pungoapp.com/)")


# --- RUN NAVIGATION ---
pg.run()
