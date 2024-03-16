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
    ui.a("Github", href="https://github.com/14dstcyr/cintel-02-data", target="blank")
    
# Create tables and plots displaying all data

# Create a Data Table and Grid

with ui.layout_columns(col_widths=(4,  8)):  
    with ui.card():  
        "Penguiin Table"

    @render.data_frame
    def render_Penguuin_Table():
        return penguins_df

with ui.layout_columns(col_widths=(4,  8)):
    with ui.card(full_screen=True): "Penguins Grid"

    @render.data_frame
    def penguin_data():
        return render.DataGrid(penguins_df, row_selection_mode="multiple")

# Create Histograms 
        
with ui.layout_columns(col_widths=(2, 6)):
    with ui.card(full_screen=True): "Plotly Penguin Histogram"

    @render_plotly
    def plot1():
        return px.histogram(px.data.bill_length_mm(), y="species")

with ui.layout_columns(col_widths=(2, 6)):
    with ui.card(full_screen=True): "Seaborn Penguin Histogram"

    @render.plot(alt="Seaborn Histogram", full_page="True")
    def seaborn_histogram():
        histplot = sns.hitplot(data=penguins_df, x="bill_length_mm", bins=input.seaborn_bin_count())
        histplot.set_title("Penguin Data")
        histplot.set_xlabel("Bill Length")
        histplot.set_ylabel("Count")
        return histplot





        



               


ui.page_opts(title="St_Cyr Penguin Data", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
        
