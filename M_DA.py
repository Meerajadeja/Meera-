import pandas as pd
import streamlit as st
st.title ("First Analytics App")
Df = pd.read_csv("melbourne (1).csv")
st.dataframe(Df)
import pandas as pd
