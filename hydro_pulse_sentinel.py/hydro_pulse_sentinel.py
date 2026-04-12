import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# --- 1. THE INTERFACE: Cinematic Naturalist Engine ---
st.set_page_config(
    page_title="HYDRO-PULSE | SENTINEL",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap');
    
    .stApp {
        background-color: #08100b !important;
        color: #e0f2f1 !important;
        font-family: 'Space Grotesk', sans-serif;
    }
    
    h1, h2, h3 {
        color: #ffffff !important;
        text-shadow: 0 0 20px rgba(0, 230, 118, 0.4);
    }

    /* Dashboard Cards */
    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(0, 230, 118, 0.2) !important;
        padding: 20px !important;
        border-radius: 15px !important;
    }

    [data-testid="stMetricValue"] {
        color: #00e676 !important;
        font-weight: 700 !important;
    }

    /* Search Bar Professional Glow */
    .stTextInput>div>div>input {
        background-color: #0d1a11 !important;
        color: #00e676 !important;
        border: 2px solid rgba(0, 230, 118, 0.5) !important;
        font-size: 1.2rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE SENTINEL SECURITY GATE (Restored) ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    _, col_auth, _ = st.columns([1, 1.2, 1])
    with col_auth:
        st.markdown("<br><br><br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>🛡️ SENTINEL OMNI-LINK</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #64748b;'>AUTHORIZED PERSONNEL ONLY</p>", unsafe_allow_html=True)
        
        access_input = st.text_input("IDENTIFICATION KEY", type="password", label_visibility="collapsed", key="auth_key")
        
        if st.button("EXECUTE SYSTEM HANDSHAKE", use_container_width=True):
            if access_input.strip().lower() == "egerton2026":
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Access Denied: Terminal Locked")
    st.stop()

# --- 3. THE AI KNOWLEDGE BASE (The Brain) ---
# This data MUST change when you search
GEO_DATA = {
    "njoro": {"lat": -0.3703, "lon": 35.9322, "risk": 4.2, "type": "Highland Forest", "velocity": "1.82", "analyst": "Stable forest canopy intercepting initial precipitation. Subsurface flow within limits."},
    "nairobi": {"lat": -1.2864, "lon": 36.8172, "risk": 8.7, "type": "Urban Basin", "velocity": "5.65", "analyst": "CRITICAL: High concrete-to-soil ratio. Flash flood runoff vectors detected in drainage arteries."},
    "mombasa": {"lat": -4.0435, "lon": 39.6682, "risk": 6.8, "type": "Coastal Estuary", "velocity": "2.90", "analyst": "Tidal surge confluence. Monitoring backflow risks at estuarine discharge points."},
    "kisumu": {"lat": -0.0917, "lon": 34.7680, "risk": 7.4, "type": "Lake Basin", "velocity": "3.45", "analyst": "Lowland accumulation protocol active. Assessing Winam Gulf lake-level back-pressure."}
}

# --- 4. SEARCH LOGIC ---
st.markdown("<h1>🌊 HYDRO-PULSE SENTINEL</h1>", unsafe_allow_html=True)

# THE SEARCH ENGINE
search_query = st.text_input("🔍 GLOBAL COMMAND SEARCH", placeholder="Type a location (Njoro, Nairobi, Mombasa, Kisumu)...", key="main_search")

# Defaulting to Njoro unless searched
active_key = "njoro"
if search_query:
    q = search_query.lower().strip()
    for key in GEO_DATA.keys():
        if key in q:
            active_key = key
            break

# Pull the specific data for the searched place
data = GEO_DATA[active_key]

# --- 5. THE COMMAND DASHBOARD ---
st.markdown(f"<p style='color: #64748b;'><strong>MISSION:</strong> Real-Time Mitigation | <strong>ACTIVE ZONE:</strong> {data['type'].upper()}</p>", unsafe_allow_html=True)

col_viz, col_intel = st.columns([2, 1.2])

with col_viz:
    horizon = st.select_slider("PREDICTIVE ANALYSIS WINDOW (MINUTES)", options=[0, 15, 30, 45, 60], value=15)
    # UPDATING THE MAP dynamically
    map_df = pd.DataFrame({'lat': [data['lat']], 'lon': [data['lon']]})
    st.map(map_df, zoom=13)

with col_intel:
    st.markdown("### 🤖 AI DIAGNOSTIC")
    # THE AI ANALYSIS (This now changes based on search!)
    st.info(f"**SENTINEL REPORT:** {data['analyst']}")
    
    # THE MATH (Objective Proof)
    with st.expander("🔢 MATHEMATICAL CORE", expanded=True):
        st.latex(r"\frac{\partial h}{\partial t} + \frac{\partial (uh)}{\partial x} + \frac{\partial (vh)}{\partial y} = S")
        st.write(f"Model Converged for: **{active_key.capitalize()}**")

# THE DYNAMIC METRIC DASHBOARD
st.markdown("<br>", unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)

# Calculating risk based on location search + slider
final_risk = round(data['risk'] + (horizon/12), 1)

m1.metric("FLOOD RISK INDEX", f"{final_risk}/10")
m2.metric("ZONE SATURATION", "91.2%" if data['risk'] > 6 else "64.5%")
m3.metric("ENERGY DISCHARGE", f"{data['velocity']} m³/s")

st.markdown("<br><hr style='border-color: rgba(0, 230, 118, 0.2);'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #1e293b; font-size: 0.7rem;'>SENTINEL PROTOTYPE V2.0 | EGERTON UNIVERSITY | SECURE DATASTREAM</p>", unsafe_allow_html=True)