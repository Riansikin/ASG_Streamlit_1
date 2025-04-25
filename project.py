import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

def show_project():
    st.title("Sales & Customer Analysis")
    st.write("\n")
    st.write("\n")

    with st.expander("Data Preview"):
        df = pd.read_excel("dataset_bee_cycle.xlsx")
        st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Gender Distribution")
        gender_count = df['gender'].value_counts()
        st.bar_chart(gender_count)

    with col2:
        st.subheader("Area")
        area_count = df['customer_country'].value_counts()
        st.line_chart(area_count)
    
    st.subheader("Total Monthly Revenue by Country")

    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.strftime('%B')
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)

    all_months = month_order
    all_countries = sorted(df['customer_country'].unique().tolist())

    selected_months = st.multiselect("Choose Month", all_months)
    selected_countries = st.multiselect("Choose Country", all_countries)

    if selected_months:
        df = df[df['month'].isin(selected_months)]
    if selected_countries:
        df = df[df['customer_country'].isin(selected_countries)]

    revenue_by_country = df.groupby(['month', 'customer_country'])['totalprice_rupiah'].sum().reset_index()

    chart = alt.Chart(revenue_by_country).mark_line(point=True).encode(
        x=alt.X('month:N', sort=month_order, title="Month"),
        y=alt.Y('totalprice_rupiah:Q', title="Total Revenue"),
        color='customer_country:N',
        tooltip=['month', 'customer_country', 'totalprice_rupiah']
    ).properties(
        width=800
    )
    st.altair_chart(chart, use_container_width=True)

    df['year_month'] = df['order_date'].dt.to_period('M').astype(str)

    all_customer = sorted(df['customer_id'].unique().tolist())
    price = sorted(df['totalprice_rupiah'].unique().tolist())

    filtered_df = df[
    (df['customer_id'].isin(all_customer)) &
    (df['totalprice_rupiah'].isin(price))
]

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Top 10 Customer")
        top_customers = (
            filtered_df.groupby('customer_id')['totalprice_rupiah']
            .sum()
            .reset_index()
            .sort_values(by='totalprice_rupiah', ascending=False)
            .head(10)
        )

        fig4, ax4 = plt.subplots()
        ax4.bar(top_customers['customer_id'].astype(str), top_customers['totalprice_rupiah'], color='green')
        ax4.set_xlabel("Customer ID")
        ax4.set_ylabel("Total Sales")
        plt.xticks(rotation=45)
        st.pyplot(fig4)
    
    with col4:
        st.subheader("Top 3 Product Category")
        top_products = filtered_df.groupby('category')['quantity'].sum().reset_index().sort_values(by='category', ascending=False).head(10)
    
        fig2, ax2 = plt.subplots()
        ax2.bar(top_products['category'].astype(str), top_products['category'], color='orange')
        ax2.set_xlabel("Product ID")
        ax2.set_ylabel("Qty Terjual")
        st.pyplot(fig2)