import streamlit as st

# --- 1. ÁREA PRINCIPAL (MAIN) ---
st.title("Mi primera aplicación de Streamlit")
st.header("¡Hola, Streamlit!")
st.text("Esta es una aplicación simple")

st.image("logo_uss.png")

# Entrada de texto principal
texto_principal = st.text_input("Escribe algo:")
if texto_principal:
  st.write(f"Escribiste: {texto_principal}")

# Botón principal
if st.button("Haz clic"):
  st.success("¡Acción realizada con éxito en el área principal!")


# --- 2. BARRA LATERAL (SIDEBAR) ---
st.sidebar.title("Mi primera barra lateral de Streamlit")
st.sidebar.header("¡Hola, Barra Lateral!")
st.sidebar.text("Esto es una barra lateral")

# Mostramos también el logo en la barra lateral (opcional pero queda genial)
st.sidebar.image("logo_uss.png")

# Entrada de texto en la barra lateral
texto_sidebar = st.sidebar.text_input("Escribe algo en la barra:")
if texto_sidebar:
  st.sidebar.write(f"Escribiste en la barra: {texto_sidebar}")

# Botón en la barra lateral
if st.sidebar.button("Haz clic pero en la barra lateral"):
  st.sidebar.success("¡Botón lateral presionado con éxito!")
