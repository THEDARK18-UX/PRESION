import streamlit as st

st.set_page_config(page_title="Calculadora Ley General de los Gases", page_icon="🌡️", layout="centered")

st.title("🌡️ Calculadora Ley General de los Gases")
st.markdown("""
Esta aplicación te permite trabajar con la ley general de los gases, que establece que:

$$ \frac{P_1 \cdot V_1}{T_1} = \frac{P_2 \cdot V_2}{T_2} $$

Donde:
- **P**: presión (atmósferas, atm)
- **V**: volumen (litros, L)
- **T**: temperatura (Kelvin, K)

Selecciona qué variable deseas calcular.
""")

st.header("📌 ¿Qué variable deseas calcular?")

opcion = st.radio(
    "Selecciona la incógnita:",
    ["Presión final (P2)", "Volumen final (V2)", "Temperatura final (T2)", "Presión inicial (P1)", "Volumen inicial (V1)", "Temperatura inicial (T1)"]
)

st.subheader("🔢 Ingresa los datos conocidos")

P1 = st.number_input("Presión inicial (P1) [atm]:", min_value=0.001, format="%0.3f") if opcion != "Presión inicial (P1)" else None
V1 = st.number_input("Volumen inicial (V1) [L]:", min_value=0.001, format="%0.3f") if opcion != "Volumen inicial (V1)" else None
T1 = st.number_input("Temperatura inicial (T1) [K]:", min_value=0.01, format="%0.2f") if opcion != "Temperatura inicial (T1)" else None
P2 = st.number_input("Presión final (P2) [atm]:", min_value=0.001, format="%0.3f") if opcion != "Presión final (P2)" else None
V2 = st.number_input("Volumen final (V2) [L]:", min_value=0.001, format="%0.3f") if opcion != "Volumen final (V2)" else None
T2 = st.number_input("Temperatura final (T2) [K]:", min_value=0.01, format="%0.2f") if opcion != "Temperatura final (T2)" else None

if st.button("Calcular"):
    try:
        if opcion == "Presión final (P2)":
            resultado = (P1 * V1 * T2) / (T1 * V2)
            st.success(f"Presión final (P2) = {resultado:.3f} atm")

        elif opcion == "Volumen final (V2)":
            resultado = (P1 * V1 * T2) / (T1 * P2)
            st.success(f"Volumen final (V2) = {resultado:.3f} L")

        elif opcion == "Temperatura final (T2)":
            resultado = (T1 * P2 * V2) / (P1 * V1)
            st.success(f"Temperatura final (T2) = {resultado:.2f} K")

        elif opcion == "Presión inicial (P1)":
            resultado = (P2 * V2 * T1) / (T2 * V1)
            st.success(f"Presión inicial (P1) = {resultado:.3f} atm")

        elif opcion == "Volumen inicial (V1)":
            resultado = (P2 * V2 * T1) / (T2 * P1)
            st.success(f"Volumen inicial (V1) = {resultado:.3f} L")

        elif opcion == "Temperatura inicial (T1)":
            resultado = (T2 * P1 * V1) / (P2 * V2)
            st.success(f"Temperatura inicial (T1) = {resultado:.2f} K")

    except Exception as e:
        st.error("Hubo un error al calcular. Verifica que todos los valores sean correctos y diferentes de cero.")

st.markdown("""
---
🧪 Aplicación creada por Huma Supay con la ley general de los gases.
""")
