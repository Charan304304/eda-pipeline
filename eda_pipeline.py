import os
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from openai import OpenAI

import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_plots(df, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Histograms
    df.hist(figsize=(10, 8))
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "histograms.png"))
    plt.close()

    # Correlation heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig(os.path.join(output_dir, "correlation.png"))
    plt.close()

    # Missing values heatmap
    plt.figure(figsize=(8, 4))
    sns.heatmap(df.isnull(), cbar=False)
    plt.title("Missing Values")
    plt.savefig(os.path.join(output_dir, "missing_values.png"))
    plt.close()

    print("✅ Plots generated successfully")

# -------------------------------
# Generate insights using LLM
# -------------------------------
def generate_insights(df):
    summary = df.describe().to_string()

    prompt = f"""
You are a senior data scientist.

Analyze this dataset:
{summary}

Provide:
- Key patterns
- Data issues
- Correlations
- ML suggestions
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# -------------------------------
# Main
# -------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True, help="Path to CSV file")
    parser.add_argument("--output-dir", default="eda_reports")

    args = parser.parse_args()

    print("📂 Loading dataset...")
    df = pd.read_csv(args.csv)

    print("📊 Generating plots...")
    generate_plots(df, args.output_dir)

    

    print("📈 Generating insights...")
    insights = generate_insights( df)

    with open(os.path.join(args.output_dir, "insights.txt"), "w") as f:
        f.write(insights)

    print("✅ Done! Check 'eda_reports' folder.")

# -------------------------------
if __name__ == "__main__":
    main()