import streamlit as st
import pandas as pd
import plotly.express as px
# Page configuration
st.set_page_config(
    page_title="Books Analytics Dashboard",
    page_icon="📚",
    layout="wide"
)
# Load cleaned dataset
@st.cache_data
def load_data():
    df = pd.read_csv("C:/Users/HP - Vicus/OneDrive/Desktop/web scraping/books_cleaned.csv")

    return df
df = load_data()
# Title
st.title("Books Analytics Dashboard")
st.markdown("""Interactive dashboard for exploring book prices, ratings,
    stock availability, categories and reviews.
    """
)

# SIDEBAR FILTERS
st.sidebar.header("Filters")
# Rating filter
ratings = sorted(df["rating"].dropna().unique())
selected_rating = st.sidebar.multiselect(
    "Select Rating",
    ratings,default= ratings )
# Category filter
categories = sorted(df["Category"].dropna().unique())

selected_categories = st.sidebar.multiselect(
    "Select Category",
    categories,
    default=categories
)
# Apply Filters
filtered_df = df[
    (df['rating'].isin(selected_rating)) & (df['Category'].isin(selected_categories))

]
# KPI Section
total_books = len(filtered_df)

average_price = filtered_df["price"].mean()

average_rating = filtered_df["rating"].mean()

total_reviews = filtered_df["Number_of_Reviews"].sum()


col1, col2, col3, col4 = st.columns(4)
col1.metric(
    "Total Books",
    total_books
)

col2.metric(
    " Average Price",
    f"£{average_price:.2f}"
)

col3.metric(
    " Average Rating",
    f"{average_rating:.2f}"
)

col4.metric(
    " Total Reviews",
    int(total_reviews)
)
# Charts
st.divider()

col1, col2 = st.columns(2)
# Average Price by Rating
with col1:

    price_rating = (
        filtered_df
        .groupby("rating")["price"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        price_rating,
        x="rating",
        y="price",
        title="Average Price by Rating",
        labels={
            "rating": "Rating",
            "price": "Average Price (£)"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )



# Books by Rating

with col2:

    rating_counts = (
        filtered_df["rating"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    rating_counts.columns = [
        "rating",
        "count"
    ]

    fig = px.bar(
        rating_counts,
        x="rating",
        y="count",
        title="Number of Books by Rating",
        labels={
            "rating": "Rating",
            "count": "Number of Books"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )



# Price Distribution


st.subheader("💷 Price Distribution")

fig = px.histogram(
    filtered_df,
    x="price",
    nbins=30,
    title="Distribution of Book Prices",
    labels={
        "price": "Price (£)"
    }
)

st.plotly_chart(
    fig,
    use_container_width=True
)



# Category Analysis


st.subheader(" Category Analysis")

category_data = (
    filtered_df
    .groupby("Category")
    .agg(
        Books=("title", "count"),
        Average_Price=("price", "mean"),
        Average_Rating=("rating", "mean")
    )
    .reset_index()
    .sort_values(
        "Books",
        ascending=False
    )
)


fig = px.bar(
    category_data.head(15),
    x="Books",
    y="Category",
    orientation="h",
    title="Top 15 Categories by Number of Books"
)

st.plotly_chart(
    fig,
    use_container_width=True
)



# Price vs Rating

st.subheader(" Price vs Rating")

fig = px.scatter(
    filtered_df,
    x="rating",
    y="price",
    hover_name="title",
    title="Relationship Between Rating and Price",
    labels={
        "rating": "Rating",
        "price": "Price (£)"
    }
)

st.plotly_chart(
    fig,
    use_container_width=True
)



# Top Expensive Books

st.subheader(" Most Expensive Books")

expensive_books = (
    filtered_df[
        [
            "title",
            "price",
            "rating",
            "Category"
        ]
    ]
    .sort_values(
        "price",
        ascending=False
    )
    .head(10)
)


st.dataframe(
    expensive_books,
    use_container_width=True,
    hide_index=True
)


# Top Rated Books

st.subheader(" Top Rated Books")

top_rated = (
    filtered_df[
        [
            "title",
            "rating",
            "price",
            "Category"
        ]
    ]
    .sort_values(
        ["rating", "price"],
        ascending=[False, False]
    )
    .head(10)
)


st.dataframe(
    top_rated,
    use_container_width=True,
    hide_index=True
)


# Raw Data

with st.expander("🔎 View Dataset"):

    st.dataframe(
        filtered_df,
        use_container_width=True
    )