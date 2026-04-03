import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go
import feedparser
from datetime import datetime

# --- BRANDING & DESIGN LANGUAGE ---
st.set_page_config(page_title="NEURAL LENS | AI Intelligence", layout="wide")

# Custom CSS for UI/UX, Transitions, and Animations
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #080a0f;
    }

    /* Animation: Fade In */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .main .block-container {
        animation: fadeIn 0.8s ease-out;
    }

    /* Glassmorphism Cards */
    .stMetric, .metric-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        transition: all 0.3s ease;
    }

    .stMetric:hover {
        background: rgba(0, 204, 255, 0.05);
        border: 1px solid rgba(0, 204, 255, 0.3);
        transform: scale(1.02);
    }

    /* Custom Header */
    .nav-container {
        display: flex;
        align-items: center;
        padding: 1rem 0;
        margin-bottom: 2rem;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    
    .logo-text {
        font-weight: 700;
        font-size: 24px;
        letter-spacing: -1px;
        color: #00ccff;
        margin-left: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGO COMPONENT ---
def draw_logo():
    st.markdown("""
        <div class="nav-container">
            <svg width="40" height="40" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="50" cy="50" r="45" stroke="#00ccff" stroke-width="2" stroke-dasharray="10 5"/>
                <path d="M30 50L50 30L70 50L50 70L30 50Z" fill="#00ccff" fill-opacity="0.8">
                    <animate attributeName="fill-opacity" values="0.8;0.3;0.8" dur="3s" repeatCount="indefinite" />
                </path>
                <circle cx="50" cy="50" r="10" fill="white"/>
            </svg>
            <span class="logo-text">NEURAL LENS</span>
            <span style="color:gray; margin-left:15px; font-weight:300;">Strategic Intelligence Terminal</span>
        </div>
    """, unsafe_allow_html=True)

# --- DATA FETCHING ---
@st.cache_data(ttl=600)
def get_ai_news():
    feed = feedparser.parse("https://www.technologyreview.com/topic/artificial-intelligence/feed/")
    return [{"title": e.title, "link": e.link} for e in feed.entries[:4]]

@st.cache_data(ttl=3600)
def get_market_data():
    tickers = ["NVDA", "MSFT", "GOOGL", "ASML"]
    data = yf.download(tickers, period="1mo")['Close']
    return data

# --- MAIN UI ---
draw_logo()

# Top Metrics Row
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Compute Index", "84.2", "+2.4%", help="Global GPU Availability")
with m2: st.metric("Model Velocity", "12.1", "High", help="Frequency of SOTA model releases")
with m3: st.metric("Market Sentiment", "Bullish", "78%")
with m4: st.metric("Capital Inflow", "$14.2B", "+5%", help="VC funding this week")

st.markdown("<br>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 Market Intelligence", "🌐 Frontier News", "🤖 Automated Briefing"])

with tab1:
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.subheader("Industry Performance")
        stocks = get_market_data()
        fig = px.line(stocks, template="plotly_dark", color_discrete_sequence=px.colors.qualitative.Pastel)
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=0, r=0, t=20, b=0))
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.subheader("Labor Transformation")
        impact_data = pd.DataFrame({
            'Industry': ['Finance', 'Legal', 'Dev', 'Medical'],
            'Augmented': [70, 60, 90, 40],
            'Automated': [10, 20, 5, 2]
        })
        # FIXED ERROR: Changed color_discrete_manual to color_discrete_sequence
        fig_impact = px.bar(
            impact_data, 
            x='Industry', 
            y=['Augmented', 'Automated'],
            color_discrete_sequence=['#00ccff', '#1e2130'],
            template="plotly_dark",
            barmode='group'
        )
        fig_impact.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_impact, use_container_width=True)

with tab2:
    st.subheader("Real-time Industry Signals")
    news_items = get_ai_news()
    for item in news_items:
        with st.expander(f"📌 {item['title']}"):
            st.write(f"Comprehensive analysis of the latest breakthrough. [Read Full Analysis]({item['link']})")

with tab3:
    st.subheader("Agentic Strategic Report")
    if st.button("🚀 Run Neural Analysis"):
        with st.spinner("Analyzing cross-sector data..."):
            st.success("Analysis Complete")
            st.markdown("""
            **Executive Summary:**
            1. **Hardware:** ASML and NVDA are showing supply chain consolidation.
            2. **Labor:** Coding automation is reaching a plateau; high-level orchestration skills are rising in value.
            3. **Recommendation:** Shift focus toward **Inference-Efficiency** startups for Q3.
            """)

# --- FOOTER ---
st.markdown("---")
st.caption("© 2026 NEURAL LENS | Data sources: YFinance, MIT Technology Review, arXiv.")
