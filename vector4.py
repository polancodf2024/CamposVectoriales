import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.title("Generador de Campo Vectorial")
st.write("Seleccione si desea generar un campo vectorial en R2 o R3.")

# Pregunta inicial: ¿R2 o R3?
dimension = st.selectbox("¿En qué espacio desea el campo vectorial?", ("R2", "R3"))

# Solicitar el correo electrónico
email = st.text_input("Correo electrónico:")

# Entrada de componentes en función de la selección
if dimension == "R2":
    st.write("Ingrese los componentes de la función vectorial F(x, y) = (U(x, y), V(x, y)).")
    u_function = st.text_input("Componente U(x, y):", value="-y")
    v_function = st.text_input("Componente V(x, y):", value="x")
else:
    st.write("Ingrese los componentes de la función vectorial F(x, y, z) = (U(x, y, z), V(x, y, z), W(x, y, z)).")
    u_function = st.text_input("Componente U(x, y, z):", value="-y")
    v_function = st.text_input("Componente V(x, y, z):", value="x")
    w_function = st.text_input("Componente W(x, y, z):", value="z")

# Rango de la cuadrícula
range_val = st.slider("Rango del eje", 1, 10, 5)

try:
    if dimension == "R2":
        # Crear cuadrícula para R2
        x = np.linspace(-range_val, range_val, 20)
        y = np.linspace(-range_val, range_val, 20)
        X, Y = np.meshgrid(x, y)

        # Definir y graficar U y V en términos de X y Y
        U = np.vectorize(lambda x, y: eval(u_function, {'x': x, 'y': y}))(X, Y)
        V = np.vectorize(lambda x, y: eval(v_function, {'x': x, 'y': y}))(X, Y)

        fig, ax = plt.subplots(figsize=(7, 7))
        ax.quiver(X, Y, U, V, color='b')
        ax.set_title(rf'Campo Vectorial $\mathbf{{F}}(x, y) = ({u_function}, {v_function})$')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.grid()
    else:
        # Crear cuadrícula para R3
        x = np.linspace(-range_val, range_val, 10)
        y = np.linspace(-range_val, range_val, 10)
        z = np.linspace(-range_val, range_val, 10)
        X, Y, Z = np.meshgrid(x, y, z)

        # Definir y graficar U, V y W en términos de X, Y y Z
        U = np.vectorize(lambda x, y, z: eval(u_function, {'x': x, 'y': y, 'z': z}))(X, Y, Z)
        V = np.vectorize(lambda x, y, z: eval(v_function, {'x': x, 'y': y, 'z': z}))(X, Y, Z)
        W = np.vectorize(lambda x, y, z: eval(w_function, {'x': x, 'y': y, 'z': z}))(X, Y, Z)

        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.quiver(X, Y, Z, U, V, W, length=0.5, color='b')
        ax.set_title(rf'Campo Vectorial $\mathbf{{F}}(x, y, z) = ({u_function}, {v_function}, {w_function})$')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.grid()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

    # Si el correo es "polanco@unam.mx", permitir descarga del gráfico
    if email == "polanco@unam.mx":
        fig_path = f"/tmp/campo_vectorial_{dimension.lower()}.png"
        fig.savefig(fig_path)
        
        with open(fig_path, "rb") as file:
            btn = st.download_button(
                label="Descargar Gráfico",
                data=file,
                file_name=f"campo_vectorial_{dimension.lower()}.png",
                mime="image/png"
            )

except Exception as e:
    st.write("Ocurrió un error al evaluar la función:", e)

