import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show_project():
    st.title("Project")
    st.write("\n")
    st.write("\n")

    with st.expander("Data Preview"):
        df = pd.read_excel("dataset_bee_cycle.xlsx")
        st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        st.write("Gender Distribution")
        gender_count = df['gender'].value_counts()
        st.bar_chart(gender_count)

    with col2:
        st.write("Area")
        area_count = df['customer_country'].value_counts()
        st.line_chart(area_count)
    
    st.title("Total Revenue per Bulan Berdasarkan Negara")

    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.strftime('%B')
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)

    # Ambil semua pilihan yang tersedia
    all_months = month_order
    all_countries = sorted(df['customer_country'].unique().tolist())

    # Checkbox multiselect dengan default kosong
    selected_months = st.multiselect("Pilih Bulan (biarkan kosong untuk semua)", all_months)
    selected_countries = st.multiselect("Pilih Negara (biarkan kosong untuk semua)", all_countries)

    # Logika: jika tidak memilih apapun, maka tampilkan semua
    if selected_months:
        df = df[df['month'].isin(selected_months)]
    if selected_countries:
        df = df[df['customer_country'].isin(selected_countries)]

    # Grouping
    revenue_by_country = df.groupby(['month', 'customer_country'])['totalprice_rupiah'].sum().reset_index()

    # Chart
    chart = alt.Chart(revenue_by_country).mark_line(point=True).encode(
        x=alt.X('month:N', sort=month_order, title="Bulan"),
        y=alt.Y('totalprice_rupiah:Q', title="Total Revenue"),
        color='customer_country:N',
        tooltip=['month', 'customer_country', 'totalprice_rupiah']
    ).properties(
        width=800
    )

    st.altair_chart(chart, use_container_width=True)