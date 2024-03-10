import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins  # This package provides the Palmer Penguins dataset

# --------------------------
# Get the Data
# --------------------------

# ALWAYS familiarize yourself with the dataset you are working with first.
# Column names for the penguins dataset include:
# - species: penguin species (Chinstrap, Adelie, or Gentoo)
# - island: island name (Dream, Torgersen, or Biscoe) in the Palmer Archipelago
# - bill_length_mm: length of the bill in millimeters
# - bill_depth_mm: depth of the bill in millimeters
#- flipper_length_mm: length of the flipper in millimeters
# - body_mass_g: body mass in grams
# - sex: MALE or FEMALE

# Load the dataset into a pandas data frame.
# Use the built-in function to load the Palmer Penguins dataset.
penguins_df = palmerpenguins.load_penguins()

# --------------------------
# Define User Interface (ul)
# --------------------------

ui.page_opts(title="St_Cyr Penguin Data", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
        
