import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins  # This package provides the Palmer Penguins dataset
import pandas as pd
import seaborn as sns
from shiny import reactive, render, req

# Use the built-in function to load the Palmer Penguins dataset.
penguins_df = palmerpenguins.load_penguins()

# Name of Project Page
ui.page_opts(title="St_Cyr Penguin Data", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")

# Add a sidebar
with ui.sidebar(open="open"):  
    
    ui.h2("Sidebar")

    # Use ui.input_selectize() to create a dropdown input to choose a column
    ui.input_selectize(
        "Selected_Attribute",
        "Bill Length in Millimeters",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    )
    
    # Use ui.input_numeric() to create a numeric input for the number of Plotly histogram bins
    ui.input_numeric("plotly_bin_count", "Number of Plotly Bins", 20)

    # Use ui.input_slider() to create a slider input for the number of Seaborn bins
    ui.input_slider("seaborn_bin_count", "Bin Count", 1, 100, 20)

    # Use ui.input_checkbox_group() to create a checkbox group input to filter the species
    ui.input_checkbox_group("selected_species_list", "Penguin Species",  ["Adelie", "Gentoo", "Chinstrap"], selected=["Chinstrap"],
        inline=True,
    )

    # Use ui.hr() to add a horizontal rule to the sidebar
    ui.hr()
    
    # Use ui.a() to add a hyperlink to the sidebar


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
        
