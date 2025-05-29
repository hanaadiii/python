import pandas as pd
import streamlit as st
import plotly.express as px


books_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')
st.title("Bestselling Books Analysis")
st.write("This app analyzes the Amazon Top Selling books from 2009 to 2022.")

#Sidebar
st.sidebar.header("Add new book data")
with st.sidebar.form("book_form"):
    new_name=st.text_input("Book Name")
    new_author=st.text_input("Author")
    new_user_rating=st.slider("User Rating", 0.0,5.0,0.0,0.1)
    new_reviews=st.number_input("Reviews", min_value=0, step=1)
    new_year=st.number_input("Year", min_value=2009, max_value=2022)
    new.genre=st.selectbox("Genre", books_df['Genre'].unique())
    submit_button=st.form_submit_button(label="Add Book")


if submit_button:
    new_data={
        'Name':new_name,
        'Author':new_author,
        'User Rating':new_user_rating,
        'Reviews':new_reviews,
        'Price':new_price,
        'Year':new_year,
        'Genre':new_genre
    }
    books_df=pd.contact([pd.DataFrame(new_data,index=[0]),books_df],ignore_index=True)
    books_df.to_csv('bestsellers_with_categories_2022_03_27.csv',index=False)
    st.sidebar.success("New Book added successfully")

filtered_books_df = books_df.copy()
