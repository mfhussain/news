# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 11:23:00 2022

@author: fhussain_adm
"""

import requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
import streamlit as st

##BBC

urlbc='https://www.bbc.com/news'

responsebc = requests.get(urlbc)

soupbc = BeautifulSoup(responsebc.text, 'html.parser')
headlinesbc = soupbc.find('body').find_all('h3')
headlinesbc_list = [x.text.strip() for x in headlinesbc]

todaybc = date.today()

dfbc = pd.DataFrame(headlinesbc_list)

dfbc['date'] = todaybc

txtbc = str(todaybc) + '_headlinesbc.csv'

dfbc.to_csv(txtbc,index=False)

#dfbc


### CNN

urlcn='https://edition.cnn.com/world'
responsecn = requests.get(urlcn)

soupcn = BeautifulSoup(responsecn.text, 'html.parser')

headlinescn = soupcn.find('body').find_all("div", {'class':'container__headline container_lead-plus-headlines__headline'})    
headlinescn_list = [x.text.strip() for x in headlinescn]

todaycn = date.today()

dfcn = pd.DataFrame(headlinescn_list)

dfcn['date'] = todaycn

txtcn = str(todaycn) + '_headlinescn.csv'

dfcn.to_csv(txtcn,index=False)

#dfcn

### NDTV

urlnd='https://www.ndtv.com/'
responsend = requests.get(urlnd)

soupnd = BeautifulSoup(responsend.text, 'html.parser')

headlinesnd = soupnd.find('body').find_all('h3')    
headlinesnd_list = [x.text.strip() for x in headlinesnd]

todaynd = date.today()

dfnd = pd.DataFrame(headlinesnd_list)

dfnd['date'] = todaynd

txtnd = str(todaynd) + '_headlinesnd.csv'

dfnd.to_csv(txtnd,index=False)

#dfnd.head(10)
st.header('Top 10 MSM Headlines Today ')
genre = st.radio((""),
    ('BBC', 'CNN', 'NDTV'))

if genre == 'BBC':
    st.dataframe(dfbc.head(10))
    
if genre == 'CNN':
    st.table(dfcn.head(10))

if genre == 'NDTV':
    st.dataframe(dfnd.head(10))    

# else:
#     st.write("You didn't select any.")


