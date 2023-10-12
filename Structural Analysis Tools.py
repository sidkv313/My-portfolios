import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to visualize the beam
def visualize_beam(beam_length, load_position, load_magnitude):
    # Example code for visualizing the beam
    x = np.linspace(0, beam_length, 100)
    y = np.zeros_like(x)
    load_x = load_position * beam_length
    load_y = -load_magnitude * 0.2
    plt.plot(x, y, color='blue', linewidth=10)
    plt.plot([load_x, load_x], [0, load_y], color='red', linewidth=2)
    plt.xlabel('Position')
    plt.ylabel('Load')
    plt.title('Beam and Applied Load')
    return plt

# Function to visualize Shear Force Diagram (SFD)
def visualize_sfd(beam_length, load_position, load_magnitude):
    # Example code for visualizing the Shear Force Diagram
    x = np.linspace(0, beam_length, 100)
    shear_force = np.zeros_like(x)
    shear_force[x > load_position * beam_length] = -load_magnitude
    plt.plot(x, shear_force, color='green', linewidth=2)
    plt.xlabel('Position')
    plt.ylabel('Shear Force')
    plt.title('Shear Force Diagram (SFD)')
    return plt

# Function to visualize Bending Moment Diagram (BMD)
def visualize_bmd(beam_length, load_position, load_magnitude):
    # Example code for visualizing the Bending Moment Diagram
    x = np.linspace(0, beam_length, 100)
    bending_moment = np.zeros_like(x)
    
    load_x = load_position * beam_length
    load_y = -load_magnitude * 0.2

    # Calculate bending moment
    for i in range(len(x)):
        if x[i] <= load_x:
            bending_moment[i] = -load_magnitude * x[i]
        else:
            bending_moment[i] = -load_magnitude * load_x

    plt.plot(x, bending_moment, color='purple', linewidth=2)
    plt.xlabel('Position')
    plt.ylabel('Bending Moment')
    plt.title('Bending Moment Diagram (BMD)')
    return plt

# Function to visualize Deflected Shape Diagram (DSD)
def visualize_dsd(beam_length, load_position, load_magnitude, elastic_modulus, moment_of_inertia):
    # Example code for visualizing the Deflected Shape Diagram
    x = np.linspace(0, beam_length, 100)
    deflection = (load_magnitude * (x - load_position * beam_length) ** 2) / (6 * elastic_modulus * moment_of_inertia)
    plt.plot(x, deflection, color='orange', linewidth=2)
    plt.xlabel('Position')
    plt.ylabel('Deflection')
    plt.title('Deflected Shape Diagram (DSD)')
    return plt


# Function to visualize Axial Force Diagram (AFD)
def visualize_afd(beam_length, load_position, load_magnitude):
    # Example code for visualizing the Axial Force Diagram
    x = np.linspace(0, beam_length, 100)
    axial_force = np.zeros_like(x)
    axial_force[x > load_position * beam_length] = load_magnitude
    plt.plot(x, axial_force, color='blue', linewidth=2)
    plt.xlabel('Position')
    plt.ylabel('Axial Force')
    plt.title('Axial Force Diagram (AFD)')
    return plt

# Streamlit app
st.title('Structural Analysis Tool')

# Project Description
st.header('Project Description')
st.markdown("""
This structural analysis tool provides engineers and students with the ability to visualize and analyze the behavior of beams subjected to various loads. The tool includes the following diagrams:

- **Beam Visualization:** Visualize the beam and the applied load.
- **Shear Force Diagram (SFD):** Understand the distribution of shear forces along the beam.
- **Bending Moment Diagram (BMD):** Visualize the bending moments acting on the beam.
- **Deflected Shape Diagram (DSD):** See the deflected shape of the beam under the applied load.
- **Axial Force Diagram (AFD):** Understand the distribution of axial forces in columns.

The tool is designed to assist with structural engineering analysis and design, offering insights into structural behavior and design decisions.

To use the tool, adjust the input parameters in the sidebar and visualize how the beam and its various properties change in response to different loads and materials.
""")

# Input parameters
st.sidebar.header('Input Parameters')
beam_length = st.sidebar.number_input('Beam Length (m)', value=5.0, step=1.0)
load_position = st.sidebar.number_input('Load Position (0-1)', value=0.5, step=0.1)
load_magnitude = st.sidebar.number_input('Load Magnitude (N)', value=10000, step=1000)
elastic_modulus = st.sidebar.number_input('Elastic Modulus (Pa)', value=2.1e11, step=1e10)
moment_of_inertia = st.sidebar.number_input('Moment of Inertia (m^4)', value=4.5e-4, step=1e-5)

# Visualize the beam and load
beam_plot = visualize_beam(beam_length, load_position, load_magnitude)
st.pyplot(beam_plot)

# Visualize Bending Moment Diagram (BMD)
bmd_plot = visualize_bmd(beam_length, load_position, load_magnitude)
st.pyplot(bmd_plot)

# Visualize Shear Force Diagram (SFD)
sfd_plot = visualize_sfd(beam_length, load_position, load_magnitude)
st.pyplot(sfd_plot)


# Visualize Deflected Shape Diagram (DSD)
dsd_plot = visualize_dsd(beam_length, load_position, load_magnitude, elastic_modulus, moment_of_inertia)
st.pyplot(dsd_plot)

# Visualize Axial Force Diagram (AFD)
afd_plot = visualize_afd(beam_length, load_position, load_magnitude)
st.pyplot(afd_plot)

# Conclusive Results
st.header('Conclusive Results')
st.markdown('Based on the input parameters, we can conclude the following:')

# Calculate the bending moment based on the input parameters
max_bending_moment = -load_magnitude * (beam_length / 2 - load_position * beam_length)

# Display the conclusion
conclusion = f"The structural analysis indicates that the beam, with the specified parameters, has a maximum bending moment of {max_bending_moment:.2f} Nm at the center of the beam (position {beam_length / 2:.2f} meters from the left support). This implies that..."
st.write(conclusion)

# Solved Example
st.header('Solved Example')
st.markdown("""
Let's work through a solved example to illustrate how to use this tool for structural analysis:

**Problem Statement:**
Consider a simply supported beam with a length of 8 meters. A point load of 10 kN is applied at the center of the beam.

**Solution:**
1. Input Parameters:
   - Beam Length: 8 meters
   - Load Position: 0.5 (center of the beam)
   - Load Magnitude: 10000 N (10 kN)

2. Visualizations:
   - The "Beam Visualization" will show the beam and the applied load.
   - The "Bending Moment Diagram (BMD)" will illustrate the distribution of bending moments along the beam.

3. Observations:
   - In the Bending Moment Diagram, you will notice a maximum bending moment at the center of the beam due to the applied load.

This tool allows you to quickly analyze and visualize the behavior of the beam under different conditions, helping you make informed design decisions.
""")
# Footer
st.markdown("By Siddharth K")
