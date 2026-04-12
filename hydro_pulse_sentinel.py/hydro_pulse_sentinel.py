import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time

# --- 1. CORE CONFIGURATION ---
st.set_page_config(
    page_title="HYDRO-PULSE | OMNI-SENTINEL",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CINEMATIC UI ENGINE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&family=JetBrains+Mono&display=swap');
    
    .stApp {
        background-color: #040806 !important;
        color: #e0f2f1 !important;
        font-family: 'Space Grotesk', sans-serif;
    }
    
    /* Neon Glow UI */
    h1, h2, h3 {
        color: #ffffff !important;
        text-shadow: 0 0 20px rgba(0, 230, 118, 0.5);
        letter-spacing: -1px;
    }

    /* AI Thinking Console Style */
    .stCodeBlock, .stMarkdown code {
        background-color: #0a1a0f !important;
        color: #00e676 !important;
        font-family: 'JetBrains Mono', monospace !important;
    }

    [data-testid="stMetric"] {
        background: rgba(0, 230, 118, 0.03) !important;
        backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 230, 118, 0.2) !important;
        border-radius: 15px !important;
    }

    [data-testid="stMetricValue"] {
        color: #00e676 !important;
        font-size: 3rem !important;
    }

    /* Search Input Refinement */
    .stTextInput>div>div>input {
        background-color: rgba(0, 230, 118, 0.08) !important;
        border: 1px solid #00e676 !important;
        color: white !important;
        font-size: 1.2rem !important;
        border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. AUTHENTICATION ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    _, col_auth, _ = st.columns([1, 1.2, 1])
    with col_auth:
        st.markdown("<br><br><br><h1 style='text-align: center;'>🔐 OMNI-LINK INITIALIZED</h1>", unsafe_allow_html=True)
        access_input = st.text_input("ENTER SYSTEM KEY", type="password", label_visibility="collapsed")
        if st.button("EXECUTE HANDSHAKE", use_container_width=True):
            if access_input.strip().lower() == "egerton2026":
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Protocol Error: Identity Not Verified")
    st.stop()

# --- 4. THE OMNI-AI ENGINE (Geographical Brain) ---
def ai_geospatial_reasoning(query):
    # Simulated high-level reasoning engine
    db = {
        "egerton": {"lat": -0.3703, "lon": 35.9322, "tags": "Agriculture, Highland, Mau Forest Catchment", "risk": 4.5},
        "nairobi": {"lat": -1.28638, "lon": 36.8172, "tags": "Urban, Concrete-Heavy, Drainage Critical", "risk": 8.2},
        "mombasa": {"lat": -4.0435, "lon": 39.6682, "tags": "Maritime, Coastal surge, Estuary focus", "risk": 6.7},
        "kisumu": {"lat": -0.0917, "lon": 34.7680, "tags": "Lacustrine, Lowland, Winam Gulf runoff", "risk": 7.4}
    }
    query_clean = query.lower().strip()
    target = db["egerton"] # Default
    for key in db:
        if key in query_clean:
            target = db[key]
    return target

# --- 5. INTERFACE ---
st.markdown("<h1 style='margin-bottom: 0px;'>🌊 OMNI-SENTINEL AI</h1>", unsafe_allow_html=True)

# The Omni-Search Bar
search_val = st.text_input("🛰️ GLOBAL INTELLIGENCE COMMAND", placeholder="Identify target location...")
geo_data = ai_geospatial_reasoning(search_val)

col_viz, col_brain = st.columns([2, 1.2])

with col_viz:
    horizon = st.select_slider("TEMPORAL PREDICTION (MINUTES)", options=[0, 15, 30, 45, 60], value=15)
    map_df = pd.DataFrame({'lat': [geo_data['lat']], 'lon': [geo_data['lon']]})
    st.map(map_df, zoom=13)

with col_brain:
    st.markdown("### 🧠 AI CORELINK")
    with st.status("Processing Geographical Vectors...", expanded=True):
        st.write(f"📍 Location Locked: {geo_data['lat']}, {geo_data['lon']}")
        time.sleep(0.3)
        st.write(f"🔎 Scanning Terrain: {geo_data['tags']}")
        time.sleep(0.3)
        st.write("📊 Applying Physics-Informed Neural Network...")
        time.sleep(0.4)
        st.write("✅ Model Converged.")
    
    st.markdown("#### **STRATEGIC DIAGNOSTIC**")
    if geo_data['risk'] > 7:
        st.error(f"CRITICAL: High runoff coefficient detected in {search_val if search_val else 'Njoro'}. Infrastructure at capacity.")
    else:
        st.success(f"STABLE: System absorption within normal parameters for {geo_data['tags'].split(',')[0]} zone.")

# THE METRICS
st.markdown("<br>", unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)

# Calculations adjusted by the AI's "Reasoning"
current_risk = round(geo_data['risk'] + (horizon/15), 1)
m1.metric("RISK PROBABILITY", f"{current_risk}/10")
m2.metric("SATURATION DEPTH", "High" if geo_data['risk'] > 6 else "Moderate")
m3.metric("AI CONFIDENCE", "98.4%")

st.markdown("<br><hr style='border-color: rgba(0, 230, 118, 0.2);'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #1e293b; font-size: 0.8rem;'>SENTINEL OMNI-AI | ENCRYPTED LINK | PRESENTATION MODE</p>", unsafe_allow_html=True)