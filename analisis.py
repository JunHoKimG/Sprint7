import pandas as pd
import plotly as plot
import streamlit as st


 
data = pd.read_csv("vehicles_us.csv")


data.info()