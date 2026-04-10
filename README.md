# 📊 AI-Powered Exploratory Data Analysis (EDA)

An intelligent data analysis platform that automates **Exploratory Data Analysis (EDA)** using **AI-powered insights (OpenAI API)** and an interactive **Streamlit UI**.

---

## 🚀 Features

* 📊 Automated data visualization (histograms, heatmaps)
* 🔗 Correlation analysis
* ❗ Missing value detection
* 🧠 AI-generated insights (like a data scientist)
* 🖥️ Interactive Streamlit dashboard
* ⬇️ Downloadable insights report

---

## 🛠️ Tech Stack

* **Language:** Python
* **Data Analysis:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **AI Integration:** OpenAI API
* **Frontend/UI:** Streamlit

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/eda-pipeline.git
cd eda-pipeline
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Set your OpenAI API key:

```bash
set OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. Upload a CSV dataset
2. System performs automatic EDA:

   * Data visualization
   * Statistical summaries
3. OpenAI API generates insights
4. Results displayed in Streamlit UI

---

## 🏗️ System Architecture

```
             ┌───────────────┐
             │   User (UI)   │
             │  Streamlit    │
             └──────┬────────┘
                    │ Upload CSV
                    ▼
        ┌────────────────────────┐
        │   Data Processing      │
        │  (Pandas, NumPy)      │
        └────────┬──────────────┘
                 │
        ┌────────▼────────┐
        │ Visualization   │
        │ (Matplotlib,    │
        │  Seaborn)       │
        └────────┬────────┘
                 │
        ┌────────▼────────┐
        │ AI Insights     │
        │ (OpenAI API)    │
        └────────┬────────┘
                 │
        ┌────────▼────────┐
        │ Output Display  │
        │ (Streamlit UI)  │
        └─────────────────┘
```

---

## 📸 Application Screenshots

### 📂 File Upload & Preview

![Image](https://images.openai.com/static-rsc-4/n10qLQ-O-pZrFtgjyS3vE669JUySRmotUpBdfvvxAqZYlLkMTSL2B6BSrZQhKY6XgG2fe8xmelP1HJRMePidfeEN8dSwFxdvKpsTSbCA5wO4eKSvyACci7V9mH5zReOWOZE73W0BahaoXSb-oTqOx9E4zrDKSNFZiYg0KrvY5w9bzZ6HraKP3f2V5pjf4x57?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/FP22CJ68hQc_dnwqmJZ-5wkgl2HoKjPZaa2lk4FqXtZhPnM-7FoR4yZyeQbs1BX-0yBmuJVN_YaUqgwmdxn1FQK6BXA9MThwKsMn0ZkaUoFdHdtu6QAOaoim3rgqarosKXfOntdtdPepKiNXMrIEBXMtvQ1MrtFPWW-CjKt1Y8o1ny6GmuHV50S1VvErOYrX?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/oESyKjxLnPJOsq_SgjA1eFAxPR3tTF_jGksqj1VygRxGlWfT2YNwtZd6pBJnYI-SOfsoQZYGz0TxhBhMPDBOhjONhUyux3TYegeZyZQzLDVubDfoD9fBRCxzwlMEB4Q18BHm_7zhfCPDeJdgDLzF8Z-pRh9ko2XDInoSJM7fi7NCLJwdw3s5O07ilWmdgMmO?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/wtcHO4BMYft8ZhEwV7cwqAxo2q8UTUnYbXjo6JHDDZh7a63sbjQWdfnFAEF1oYUQsBNSs7JqiyFc-V4p_kZZ2UAEh8FAt1t5baEq_AxIjM0KnCDPO0KPJDcKcTeIWMss4lLpL9v1NVHnHbfE5j3qXT4YDximXsWC1NNcDd3OIWp8lqOAqfFDKO1bVcGXT07J?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/xZxOa3IKu6lmUTJIdKEp4wM-n_hAWg7CWsDL9wNGlFAiR336OJ0YcEo4jGTyseZgWHsIXOLzTX5DPMUlXlEEwGiqeuqnRZvE6JNWjNodVF5dcWyHtvBL0_5-vTBDBWn7CQVrEDE35NNB2aNoc954yUlnZBFhzS-_926dWNRQS_jPY4156YjyOl7P2gpcI5-k?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/PR6xGuFLtlP42XS9Tg_uzwFcHk6EtKT1fABUtx3bSlE3jbW9EAY-MWSTngIa0H4JE0pyLlbtPf0hxTD4Ty1ocacbub-Yt5e0IawTuw17loGZvwy-xKdk5LOFXQ3fkQ0LOSE7CpNqUhvZjEPqyiLFgVrDEMCFiXAM8x0HTG9GZKrhRN2_5X2EZeZiaHCAcJ28?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/OdAcDgVBB-EDhaDbAsiL8HTwEPqJBwxPZbtOkSf062EyPACSA6WSRk1Q52MIhI0VPX4kfYHBRTFyDdDcRokPyNzCsXn6w0d23Jx2ZlbDk6ODzENpZL3MmHL9ISQE1LHnSzG8aYIgby37qnxyjbR9QU4VgOPyebWo7OOVpIB8A0lZJTLIMPblQh__DETsaz4B?purpose=fullsize)

---

### 📊 Data Visualizations

![Image](https://images.openai.com/static-rsc-4/hYmkE7fvuTtGne_Da2EgMONRo_njFvAdSLNF58oYDndmSYy7FcqxhXQAh_gsVu0b9AfgV3T0MiaRnt4oifb11YZSU6SDMPiZjRH8VIc6qLoi0Wo6DDpZk6WIGJEsKRaVatE1w1Se6gw4wY_ClxEaoaMNIM960RTbJoI_7-0y-bIAF9r_lojhtPRU8_aAYpv3?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/0LNc3G2hjT2d8jLr5j6GSbLgf-JfvwuTwlFWjhdB66xRY2Z96PE4IU8CFfKGQodLOnmKYO5RvHzj09wJVADDIVYL1YIPKnoncgE9aNNX90xJ9b3f84A03NBKoCWuNta2ZGI4qq5x6LKZwOSSe6tV-C6pq6T9v6-te43uBDEIieEUtiAVDe6NVKlxhJW1jAgn?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/O6JFLx7fownxCFE272-mCTZXclm2CUaLMXcXrYw7ARfgrvGZBg2zdauCwOvpE8rm_7lOWFqnG43f5Tap5SGwpm4P0Piu9vvO1t2NgCcaHlv3kLBzjbgSvSFiDQkSersMDreaNESnUCvfeeN0jgVOMHyZFCO-WImK5YJJQeC7yybKkRxmyEFiwwZb4UaSp7sI?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/6CV_7G2qg4ukhAxdEXjENsS0K29zV474VKDY4ujCvhV7OoB4ILc5addHj9at8XW5x-4UZoO5lqEgZF2sa2xLVrHYwf3QzVrHsEq38Hywgdt2OU3VXDaPMCNbqkeU5uhZQ1xQzfDlpWVmLQZDEz2_5LUQUJwS1tQVls4pnZ0RSszgoW-B_aXdUDh4paauf0w1?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/vC_8cEP7QEwi7eKhUGxtMUnVsSUo0Ky2HNaCOc8uQ-DdehgsEs78XsNaR_DYDY6QRART-7YdAsGQ_49ZVE9RDa4VOI85OJqVIXEa7_GPQ8JLA55Q0zdZBWMnhaNSLBYugjBb82eRNHzhIdhYfS3vyomrKtL_v_llzD0eqguHra2XqdtZhXbZhNjGTnEx65tF?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/9M4oYhPnmCV3MEL4YAs0e3uUXj6KvYObIS39CAXihb0t24rOR1ydP3lmHE5mMovcBDvoLDnyK3gSL69fmvYBw95LQIaL61Lkp64GAz_vIGG550DtEFm9bKQneGjpsLI1DR-tvTxoGq4r36EfXduKMo9Oft7fF6iq7sHGOCxVXGmf7aQOuk-O-Hj-BtkbDQFK?purpose=fullsize)

---

### 🧠 AI Insights Output

![Image](https://images.openai.com/static-rsc-4/yOwFaXcUSjJxylDqljQ3G3Nj0WDQb0j_eylW7igXtQhM4EqJHvImRLAk7WGpMUdO-DewTlZPKSPPLx-TTsLfTvRF4O2ktmAQsc01100NU9e6Yz5SqK00Sklu9Hugblmd7pXd6uOW7lvdzUfwYUUSkd9XW79caCR2e4v2L7nxnKzsLINTNpMXfzsmy9b9MUG1?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ZkY1NooG9zWbm-BEKOYKFLe5mWyLCkcLBTE5ugl8d_d3kpeDaHGau2aTCYRRQeXWl4sEgNfa9E03YeIkt4SZj7vhvZ2FhqKCZKjjK-Bp390isNRytKkf2QVIebGnSC1YEBdBqSdVrPoNZOIku0tXLep0xPuhcreG4Afo356O33Z6nWiGdbYx3b25u8oT0slk?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/9i3X12N7-qEADsLAAK-v6Vm1Pj43w_DbW9qgv26INGqk6Uyk9K0ON8GkNvEOLNfhvl2PYlIi6xZPlc5mFZI8ka-6l091zBlUoA6FqFyvx_4e6jj3S-yBsn4z8b-4JsGgByEk9YRZPHzYMD8lXvSb9689a6f4655QJfi7N3DX99Hs3WfGx64_p5ZpQbCcTZMB?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/V5RZZ__OhS3pMDqjN3H6A5LIi261Y8U6OIU8yW-g88bDfx7N1IgkiWSMDWtjBMPy17iju5cO9P-faqzSg8pYPl6ki76R7SOOBlQIHpLx3JfbEMrDBPyhijSyw-hWSvn_KwBoe8-BXlfUclacOvLz7eghuKgbWvuOhR6-nz8nwzvr9DHtLO5bpgHymgLgn2go?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/pr1iqJo4H7hrenWSsuANBTumgxUlTo245PqKL_zb6iD66HZAeKjMugqmWnlGOVSBo2IZY6ExuBOFflEWw0ylB4lTBIRWM8wvY500YCkM8xjrqO0Ade-iWRHl4ZtRghDG1X1RvWNFaOVItXmG2zDP91RM0XmPO4n2BIUIbz28bV1lA9Pig7hMAZqiElVJRbI7?purpose=fullsize)

---

## 🌍 Deployment

This project is deployed using **Streamlit Cloud**.

🔗 Live Demo: eda-pipeline-flczztsjkdfdczxgzgyw3n.streamlit.app

---

## 🎯 Use Cases

* Data Analysis Automation
* Business Intelligence
* Machine Learning Preprocessing
* Academic Projects

---

## 🔒 Security

* API keys are managed via environment variables
* `.gitignore` prevents sensitive data leaks

---

## ⭐ Future Improvements

* 📊 Interactive charts (Plotly)
* 🤖 ML model integration
* 📥 PDF report generation
* 🔍 Advanced filtering options

---

## 👨‍💻 Author

**Charan Simhadri**

---

## 📌 License

This project is open-source and available under the MIT License.
