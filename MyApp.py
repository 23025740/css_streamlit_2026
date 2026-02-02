import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "STEM Data Explorer", "Contact"],
)

# Dummy STEM data
ai_data = pd.DataFrame({
    "Algorithm": ["Neural Net", "Decision Tree", "Support Vector Machine", "Random Forest", "Transformer"],
    "Accuracy (%)": [92, 85, 88, 90, 95],
    "Test Date": pd.date_range(start="2024-01-01", periods=5),
})

cybersecurity_data = pd.DataFrame({
    "Threat Type": ["Phishing", "Malware", "Ransomware", "DDoS Attack", "SQL Injection"],
    "Incidents Reported": [120, 85, 40, 60, 25],
    "Detection Date": pd.date_range(start="2024-01-01", periods=5),
})

robotics_data = pd.DataFrame({
    "Robot Model": ["Atlas", "Spot", "Pepper", "Nao", "ASIMO"],
    "Task Efficiency (%)": [80, 75, 60, 65, 70],
    "Evaluation Date": pd.date_range(start="2024-01-01", periods=5),
})

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Ritshidze Tshivhase"
    field = "Computer Science & Mathematics"
    institution = "University Of Venda"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    
    st.image(
        "https://www.cryptopolitan.com/wp-content/uploads/2024/03/1d71b9de-338f-4f9f-8a4c-3334b0b2e970.jpg",
        caption="Artificial Intelligence Concept (Pixabay)"
    )

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    st.sidebar.header("Data Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["AI Algorithms", "Cybersecurity Threats", "Robotics Performance"]
    )

    if data_option == "AI Algorithms":
        st.write("### AI Algorithm Data")
        st.dataframe(ai_data)
        # Add widget to filter by accuracy
        acc_filter = st.slider("Filter by Accuracy (%)", 0, 100, (0, 100))
        filtered_ai = ai_data[
            ai_data["Accuracy (%)"].between(acc_filter[0], acc_filter[1])
        ]
        st.write(f"Filtered Results for Accuracy Range {acc_filter}:")
        st.dataframe(filtered_ai)

    elif data_option == "Cybersecurity Threats":
        st.write("### Cybersecurity Threat Data")
        st.dataframe(cybersecurity_data)
        # Add widget to filter by incidents
        incident_filter = st.slider("Filter by Incidents Reported", 0, 200, (0, 200))
        filtered_cyber = cybersecurity_data[
            cybersecurity_data["Incidents Reported"].between(incident_filter[0], incident_filter[1])
        ]
        st.write(f"Filtered Results for Incident Range {incident_filter}:")
        st.dataframe(filtered_cyber)

    elif data_option == "Robotics Performance":
        st.write("### Robotics Performance Data")
        st.dataframe(robotics_data)
        # Add widget to filter by efficiency
        efficiency_filter = st.slider("Filter by Task Efficiency (%)", 0, 100, (0, 100))
        filtered_robotics = robotics_data[
            robotics_data["Task Efficiency (%)"].between(efficiency_filter[0], efficiency_filter[1])
        ]
        st.write(f"Filtered Results for Efficiency Range {efficiency_filter}:")
        st.dataframe(filtered_robotics)

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "ritshidzetshiv@gmail.com"
    st.write(f"You can reach me at {email}.")


