import streamlit as st

st.set_page_config(page_title="Calculadora Ley de Gases Ideales", page_icon="🧪", layout="centered")

st.title("💨 Calculadora Química: Ley de Gases Ideales")
st.markdown("""
Esta aplicación te permite calcular cualquiera de las variables de la ley de los gases ideales:

$$ PV = nRT $$

Donde:
- **P**: presión (atmósferas, atm)
- **V**: volumen (litros, L)
- **n**: cantidad de sustancia (mol)
- **R**: constante universal de los gases (0.0821 atm·L/mol·K)
- **T**: temperatura (Kelvin, K)
""")

st.header("🔍 ¿Qué variable deseas calcular?")

opcion = st.radio(
    "Selecciona una variable:",
    ["Presión (P)", "Volumen (V)", "Cantidad de sustancia (n)", "Temperatura (T)"]
)

R = 0.0821  # atm·L/mol·K

if opcion == "Presión (P)":
    V = st.number_input("Ingresa el volumen (L):", min_value=0.001, format="%0.3f")
    n = st.number_input("Ingresa la cantidad de sustancia (mol):", min_value=0.001, format="%0.3f")
    T = st.number_input("Ingresa la temperatura (K):", min_value=0.01, format="%0.2f")
    if st.button("Calcular presión"):
        P = (n * R * T) / V
        st.success(f"La presión es {P:.3f} atm")

elif opcion == "Volumen (V)":
    P = st.number_input("Ingresa la presión (atm):", min_value=0.001, format="%0.3f")
    n = st.number_input("Ingresa la cantidad de sustancia (mol):", min_value=0.001, format="%0.3f")
    T = st.number_input("Ingresa la temperatura (K):", min_value=0.01, format="%0.2f")
    if st.button("Calcular volumen"):
        V = (n * R * T) / P
        st.success(f"El volumen es {V:.3f} L")

elif opcion == "Cantidad de sustancia (n)":
    P = st.number_input("Ingresa la presión (atm):", min_value=0.001, format="%0.3f")
    V = st.number_input("Ingresa el volumen (L):", min_value=0.001, format="%0.3f")
    T = st.number_input("Ingresa la temperatura (K):", min_value=0.01, format="%0.2f")
    if st.button("Calcular cantidad de sustancia"):
        n = (P * V) / (R * T)
        st.success(f"La cantidad de sustancia es {n:.4f} mol")

elif opcion == "Temperatura (T)":
    P = st.number_input("Ingresa la presión (atm):", min_value=0.001, format="%0.3f")
    V = st.number_input("Ingresa el volumen (L):", min_value=0.001, format="%0.3f")
    n = st.number_input("Ingresa la cantidad de sustancia (mol):", min_value=0.001, format="%0.3f")
    if st.button("Calcular temperatura"):
        T = (P * V) / (n * R)
        st.success(f"La temperatura es {T:.2f} K")

st.markdown
