import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.title("Generador de Campo Vectorial 2D")
st.write("Ingrese los componentes de la función vectorial F(x,y) = (U(x,y), V(x,y)).")

# Solicitar el correo electrónico
email = st.text_input("Correo electrónico:")

# Entradas de usuario para el campo vectorial
u_function = st.text_input("Componente U(x, y):", value="-y")  # Por defecto, U(x, y) = -y
v_function = st.text_input("Componente V(x, y):", value="x")   # Por defecto, V(x, y) = x

# Rango de la cuadrícula
range_val = st.slider("Rango del eje X y Y:", 1, 10, 5)

# Generar el campo vectorial
try:
    # Crear cuadrícula
    x = np.linspace(-range_val, range_val, 20)
    y = np.linspace(-range_val, range_val, 20)
    X, Y = np.meshgrid(x, y)

    # Definir funciones vectorizadas de U y V en términos de X y Y
    U = np.vectorize(lambda x, y: eval(u_function, {'x': x, 'y': y}))(X, Y)
    V = np.vectorize(lambda x, y: eval(v_function, {'x': x, 'y': y}))(X, Y)

    # Graficar
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.quiver(X, Y, U, V, color='b')
    ax.set_title(rf'Campo Vectorial $\mathbf{{F}}(x, y) = ({u_function}, {v_function})$')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

    # Si el correo es "polanco@unam.mx", permitir descarga del gráfico
    if email == "polanco@unam.mx":
        # Guardar la figura en un archivo
        fig_path = "/tmp/campo_vectorial.png"
        fig.savefig(fig_path)
        
        # Agregar botón de descarga
        with open(fig_path, "rb") as file:
            btn = st.download_button(
                label="Descargar Gráfico",
                data=file,
                file_name="campo_vectorial.png",
                mime="image/png"
            )

except Exception as e:
    st.write("Ocurrió un error al evaluar la función:", e)

