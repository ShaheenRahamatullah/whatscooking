import streamlit as st
import langchain_dishes

st.title("What's Cooking?")
vegetable = st.sidebar.selectbox("Pick the main ingredient", (" ", "Potato", "Egg-plant", "Beans", "Carrot", "Spinach"))
cuisine = st.sidebar.selectbox("Pick a cuisine", (" ", "American", "Arabian", "Indian", "Chinese", "Mexican"))

if vegetable and cuisine:
    response = langchain_dishes.generate_dishes(vegetable,cuisine)
    st.write("Dishes you can cook using", vegetable, " in ", cuisine, "style")
    st.header(response['dishes_name'].strip())
    receipes = response['receipe_items'].strip().split(",")
    #st.write("Dishes you can cook using",vegetable, " in ", cuisine, "style")
    for items in receipes:
            st.write("-", items)
