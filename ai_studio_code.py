import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go
import feedparser
from datetime import datetime

# --- CONFIG ---
st.set_page_config(page_title="AI Industry Intelligence", layout="wide", initial_sidebar_state="expanded")

# --- STYLE ---
st.markdown("""
    <style>
    .metric-card { background-color: #1e2130; padding: 20px; border-radius: 10px; border: 1px solid #30363d; }
    .stMetric { background-color: #1e2130; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- DATA FETCHING (REAL-TIME) ---
@st.cache_data(ttl=600)
def get_ai_news():
    # Pulling from high-quality AI news feeds
    feeds = [
        "https://www.technologyreview.com/topic/artificial-intelligence/feed/",
        "https://openai.com/news/rss.xml"
    ]
    news_items = []
    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            news_items.append({"title": entry.title, "link": entry.link, "date": entry.published})
    return news_items

@st.cache_data(ttl=3600)
def get_stock_data():
    tickers = ["NVDA", "MSFT", "GOOGL", "AMZN", "TSM"]
    data = yf.download(tickers, period="1mo")['Close']
    return data

# --- UI LAYOUT ---
st.title("🚀 AI Industry Intelligence Command Center")
st.caption(f"Live Intelligence Feed | Last Update: {datetime.now().strftime('%H:%M:%S')} UTC")

# --- SIDEBAR (AGENTIC CONTROLS) ---
with st.sidebar:
    st.header("🤖 Agentic Actions")
    st.info("Agent Status: **Monitoring**")
    
    analysis_type = st.radio("Intelligence Focus", ["Market Cap", "Compute Scarcity", "Job Displacement"])
    
    if st.button("Generate Executive Summary"):
        st.write("---")
        st.subheader("Strategic Briefing")
        st.write(f"**Analysis:** AI stocks are showing a high correlation with energy infrastructure. **Action:** Recommend hedging GPU hardware long-positions with nuclear energy small-caps.")
    
    st.divider()
    st.subheader("Model Router")
    st.metric("Optimal Model", "GPT-4o-mini", "-$0.12/1M tokens")
    st.button("Reroute Traffic")

# --- MAIN DASHBOARD ---

# Row 1: Market Performance (Real Data)
st.subheader("📈 AI Market Pulse (Real-Time)")
stocks = get_stock_data()
fig_stocks = px.line(stocks, labels={'value': 'Price (USD)', 'Date': ''}, template="plotly_dark")
fig_stocks.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_stocks, use_container_width=True)

# Row 2: Sentiment and News
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📰 Frontier News Feed")
    news = get_ai_news()
    for item in news:
        st.markdown(f"**[{item['title']}]({item['link']})**")
        st.caption(f"Source: Tech Review | {item['date']}")
        st.write("---")

with col2:
    st.subheader("🧠 Sentiment & Compute")
    # Simulated Sentiment Gauge
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 82,
        title = {'text': "AI Hype Index"},
        gauge = {'axis': {'range': [0, 100]},
                 'bar': {'color': "#00ffcc"},
                 'steps': [
                     {'range': [0, 50], 'color': "#333"},
                     {'range': [50, 80], 'color': "#555"},
                     {'range': [80, 100], 'color': "#777"}]}
    ))
    fig_gauge.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"})
    st.plotly_chart(fig_gauge, use_container_width=True)
    
    st.metric("NVIDIA H100 Availability", "12 Weeks", "-2 Weeks")
    st.metric("Open Source Model Velocity", "+14.2%", "vs Last Month")

# Row 3: Workforce Impact Module
st.divider()
st.subheader("🏢 Labor Market Transformation")
impact_data = pd.DataFrame({
    'Industry': ['Software', 'Legal', 'Healthcare', 'Finance', 'Manufacturing'],
    'AI-Augmented': [88, 45, 30, 65, 20],
    'Automated': [12, 25, 5, 15, 40]
})
fig_impact = px.bar(impact_data, x='Industry', y=['AI-Augmented', 'Automated'], 
                    title="Sector Exposure (2025-2026 Projection)",
                    color_discrete_manual=['#00ccff', '#ff3300'], template="plotly_dark")
st.plotly_chart(fig_impact, use_container_width=True)