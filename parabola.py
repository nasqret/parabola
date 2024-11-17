import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set up sliders for values of a and b
a = st.slider('Coefficient a', -1.0, 1.0, 0.0, step=0.01)
b = st.slider('Coefficient b', -2.0, 2.0, 0.0, step=0.01)

# Generate x values from -3 to 3
x = np.linspace(-3, 3, 500)
# Calculate y values for the parabola and cubic function
y_parabola = a * x ** 2 + b
y_cubic = a * x ** 3 + b

# Create the plot
fig, ax = plt.subplots()
ax.plot(x, y_parabola, label=f'y = {a}x² + {b}')
ax.plot(x, y_cubic, label=f'y = {a}x³ + {b}', linestyle='--')
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

