import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from streamlit_plotly_events import plotly_events
from streamlit_toggle import toggle
import seaborn as sns

st.set_page_config(page_title = 'Global FDI flows',
                layout='wide',
                initial_sidebar_state='expanded')


df = pd.read_csv("df_full_with_predictions.csv")
df['diff_pred_real_fdi'] = df['Predicted FDI billion USD'] - df['Foreign Direct Investment billion USD']


header_left,header_mid,header_right = st.columns([1,2,1],gap='large')

with header_mid:
    st.title('Global FDI flows')


with st.sidebar:
    Country_filter = st.multiselect(label= 'Select The Country',
                                options=df['Country'].unique(),
                                default="India")

if st.checkbox("Hide dataframe"):
    st.dataframe(df,width=1500,height=250)


toggle = toggle()

if toggle is False:
    fig1 = px.choropleth(df, locations='Country', locationmode='country names', color='Predicted FDI billion USD',
                    title='Global Map', color_continuous_scale='Purples',
                )
    fig1.update_layout(
        autosize=False,
        width=1000,
        height=800,legend=dict(
                            orientation = "h",
                            yanchor="bottom",
                            y=-.50,
                            xanchor="right",
                            x=1
                            )
    )


    st.plotly_chart(fig1,width=8000)  # to show the plot on streamlit

if toggle is True:
    fig = plt.figure(figsize=(10, 4)) 
    sns.lineplot(df[df.Country == "India"], y = "Foreign Direct Investment billion USD",x = "Year")
    sns.lineplot(df[df.Country == "India"], y = 'Predicted FDI billion USD', x= "Year")
    st.pyplot(fig)




# selected_points = plotly_events(fig1,select_event=True)
# print('plotly varibles',plotly_events)
# print('plotly length',len(selected_points))
# a=selected_points[0]
# a= pd.DataFrame.from_dict(a,orient='index')
# a



# Render the map using Streamlit
