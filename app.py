import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Education Inequality Dashboard", layout="wide")

# Title and description
st.title("📊 Education Inequality Dashboard")
st.markdown("""
Welcome to the interactive dashboard for exploring education inequality data.
Upload your dataset or use the default one to visualize patterns and prepare for model predictions.
""")

# Upload CSV or use default
uploaded_file = st.file_uploader("Upload your dataset", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Data uploaded successfully!")
else:
    try:
        df = pd.read_csv("education_inequality_data.csv")
        st.info("Using default dataset: `education_inequality.csv`")
    except FileNotFoundError:
        st.error("No dataset uploaded and default file not found.")
        st.stop()

# Show basic info
st.subheader("🔍 Dataset Preview")
st.dataframe(df.head())

# Summary stats
st.subheader("📈 Summary Statistics")
st.write(df.describe())

# Column selection for visualization
st.subheader("📊 Feature Visualization")
column = st.selectbox("Choose a column to visualize", df.columns)
if df[column].dtype == 'object':
    st.bar_chart(df[column].value_counts())
else:
    fig, ax = plt.subplots()
    sns.histplot(df[column], kde=True, ax=ax)
    st.pyplot(fig)

# Optional filters (e.g., region, gender)
st.subheader("🎯 Filter by Region or Gender")
if 'region' in df.columns:
    region = st.selectbox("Select region", df['region'].unique())
    df_filtered = df[df['region'] == region]
    st.write(f"Filtered data for region: {region}")
    st.dataframe(df_filtered.head())
else:
    df_filtered = df

# Placeholder for model prediction
st.subheader("🤖 Dropout Risk Prediction (Coming Soon)")
st.info("This section will show model outputs once integrated.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ by Kendi for the Capstone Project")