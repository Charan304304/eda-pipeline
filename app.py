import streamlit as st
import pandas as pd
import os
from eda_pipeline import generate_plots, generate_insights

st.set_page_config(page_title="AI EDA Tool", layout="wide")

# 🔥 Sidebar
st.sidebar.title("⚙️ Settings")
st.sidebar.write("Upload your dataset and run AI analysis")

st.title("📊 AI-Powered EDA Analyzer")
st.markdown("### Upload your CSV and get instant insights 🚀")

uploaded_file = st.file_uploader("📂 Upload CSV file", type=["csv"])

if uploaded_file:
    # Encoding handling
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8')
    except:
        df = pd.read_csv(uploaded_file, encoding='latin1')

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📄 Data Preview")
        st.dataframe(df.head())

    with col2:
        st.subheader("📊 Basic Info")
        st.write(f"Rows: {df.shape[0]}")
        st.write(f"Columns: {df.shape[1]}")

    if st.button("🚀 Run Full Analysis"):
        output_dir = "eda_reports"
        os.makedirs(output_dir, exist_ok=True)

        with st.spinner("Generating plots..."):
            generate_plots(df, output_dir)

        st.success("Plots generated!")

        # Show plots nicely
        st.subheader("📊 Visualizations")
        images = [f for f in os.listdir(output_dir) if f.endswith(".png")]

        for i in range(0, len(images), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(images):
                    cols[j].image(os.path.join(output_dir, images[i + j]))

        # AI insights
        st.subheader("🧠 AI Insights")
        with st.spinner("Thinking like a data scientist..."):
            
            insights = generate_insights( df)

        st.markdown(insights)
        # Save insights
insights_path = os.path.join(output_dir, "insights.txt")
with open(insights_path, "w") as f:
    f.write(insights)

# Download button
with open(insights_path, "rb") as file:
    st.download_button(
        label="⬇️ Download Insights Report",
        data=file,
        file_name="eda_insights.txt",
        mime="text/plain"
    )