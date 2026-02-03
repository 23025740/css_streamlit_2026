import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(page_title="Tshivhase Ritshidze Portfolio", layout="wide")

# Sidebar Menu (Original Structure)
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "STEM Data Explorer", "Contact"],
)

# --- DUMMY STEM DATA: FinTech & Inclusion Research ---
# Data simulating SA financial trends 2021-2026
inclusion_data = pd.DataFrame({
    "Year": [2021, 2022, 2023, 2024, 2025, 2026],
    "Unbanked Population (%)": [19.0, 18.2, 16.5, 15.0, 13.5, 12.1],
    "Mobile Wallet Usage (%)": [35, 42, 58, 72, 81, 89],
    "PayShap Volume (Millions)": [0, 0, 0.4, 74.2, 185.0, 390.0]
})

# --- SECTIONS ---

if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Undergraduate Profile Information
    name = "Tshivhase Ritshidze"
    field = "BSc Computer Science & Mathematics"
    institution = "University of Venda"
    internship = "Software Engineering Intern | InterBoot"

    st.write(f"**Name:** {name}")
    st.write(f"**Academic Field:** {field}")
    st.write(f"**Institution:** {institution}")
    st.write(f"**Current Role:** {internship}")
    
    st.info("""
    **Research Overview:** Exploring how real-time, alias-based payment systems 
    (like PayShap) impact financial inclusion for unbanked communities in South Africa.
    """)

    # Tech-focused profile image
    st.image(
        "https://cdn.pixabay.com/photo/2016/11/19/14/00/code-1839406_1280.jpg",
        caption="Bridging Mathematical Theory with Financial Technology"
    )

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    # Your original upload and filter logic
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
    else:
        st.write("#### Ongoing Research Works (2025-2026)")
        st.write("- *The Digital Leap: PayShap's Role in Rural Formalization*")
        st.write("- *Predicting Mobile Money Adoption using Stochastic Models*")

elif menu == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    st.sidebar.header("Data Selection")
    
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Mobile Payment Adoption", "Financial Inclusion Metrics"]
    )

    if data_option == "Mobile Payment Adoption":
        st.write("### National Mobile Wallet Growth vs. Unbanked Rates")
        st.dataframe(inclusion_data)
        
        # Original Filtering Logic (Modified for Year Range)
        year_filter = st.slider("Filter by Year Range", 2021, 2026, (2023, 2026))
        filtered_data = inclusion_data[inclusion_data["Year"].between(year_filter[0], year_filter[1])]
        
        st.write(f"Displaying Trends for {year_filter[0]} - {year_filter[1]}:")
        st.line_chart(filtered_data.set_index("Year")[["Unbanked Population (%)", "Mobile Wallet Usage (%)"]])

    elif data_option == "Financial Inclusion Metrics":
        st.write("### PayShap Transaction Growth (Millions)")
        st.bar_chart(inclusion_data.set_index("Year")["PayShap Volume (Millions)"])
        st.success("**Research Finding:** A 500% surge in volume correlates with the 2024 proxy-ID rollout.")

elif menu == "Contact":
    st.header("Contact Information")
    email = "tshivhaseritshidze03@gmail.com"
    st.write(f"You can reach me at: **{email}**")
    st.write("---")
    st.write("📍 **Department of Computer Science & Mathematics | University of Venda**")
