import streamlit as st

st.set_page_config(page_title="Calculadora de Presión", page_icon="🧪", layout="centered")

st.title("🧪 Calculadora de Presión")
st.markdown("""
Esta aplicación interactiva te ayudará a calcular la presión usando la fórmula general:

$$ P = \frac{F}{A} $$

Donde:
- **P** es la presión (en pascales, Pa)
- **F** es la fuerza (en newtons, N)
- **A** es el área (en metros cuadrados, m²)
""")

st.header("🔢 Selecciona el tipo de cálculo")

calculo_tipo = st.radio(
    "¿Qué deseas calcular?",
    ["Presión (P)", "Fuerza (F)", "Área (A)"]
)

if calculo_tipo == "Presión (P)":
    st.subheader("Calcular Presión")
    fuerza = st.number_input("Ingresa la fuerza (N):", min_value=0.0, format="%0.2f")
    area = st.number_input("Ingresa el área (m²):", min_value=0.0001, format="%0.4f")
    if st.button("Calcular presión"):
        presion = fuerza / area
        st.success(f"La presión es {presion:.2f} Pa")

elif calculo_tipo == "Fuerza (F)":
    st.subheader("Calcular Fuerza")
    presion = st.number_input("Ingresa la presión (Pa):", min_value=0.0, format="%0.2f")
    area = st.number_input("Ingresa el área (m²):", min_value=0.0001, format="%0.4f")
    if st.button("Calcular fuerza"):
        fuerza = presion * area
        st.success(f"La fuerza es {fuerza:.2f} N")

elif calculo_tipo == "Área (A)":
    st.subheader("Calcular Área")
    presion = st.number_input("Ingresa la presión (Pa):", min_value=0.0, format="%0.2f")
    fuerza = st.number_input("Ingresa la fuerza (N):", min_value=0.0, format="%0.2f")
    if st.button("Calcular área"):
        area = fuerza / presion if presion != 0 else 0
        if presion != 0:
            st.success(f"El área es {area:.4f} m²")
        else:
            st.error("La presión no puede ser cero para este cálculo.")

st.markdown("""
---
✅ Aplicación creada con ❤️ por Huma Supay
""")
