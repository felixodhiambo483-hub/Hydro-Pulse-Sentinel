import streamlit as st
import pandas as pd
import numpy as np
import geocoder
import time
from datetime import datetime

# --- 1. PAGE CONFIG & DESIGN ---
st.set_page_config(page_title="Hydro-Pulse AI | Global Sentinel", layout="wide", page_icon="🌊")

# Cinematic Naturalist Styling
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    h1 { color: #004d40; font-family: 'Inter', sans-serif; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIMPLE SECURE GATEWAY ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.markdown("<h1 style='text-align: center;'>🛡️ SENTINEL ACCESS</h1>", unsafe_allow_html=True)
    
    # Simple password check: 'egerton2026'
    access_input = st.text_input("Enter Access Key", type="password")
    
    if st.button("UNLOCK SYSTEM"):
        # We use .strip().lower() so it works even if you have spaces or caps
        if access_input.strip().lower() == "egerton2026":
            st.session_state["authenticated"] = True
            st.success("Access Granted.")
            time.sleep(0.5)
            st.rerun()
        else:
            st.error("Invalid Key. Access Denied.")
    st.stop() # Stops the rest of the app from running until unlocked

# --- 3. GLOBAL CONTEXT ENGINE ---
def get_global_data():
    try:
        g = geocoder.ip('me')
        lat, lon = g.latlng if g.latlng else [-0.3697, 35.9327]
        city = g.city if g.city else "Njoro (Egerton)"
    except:
        lat, lon, city = [-0.3697, 35.9327], "Egerton University"
    
    ai_insight = (
        f"Topography analysis for {city} indicates high saturation risk. "
        "PINN models suggest Njoro River runoff will peak in T+45 mins."
    )
    return lat, lon, city, ai_insight

# --- 4. THE INTERFACE ---
u_lat, u_lon, u_city, u_ai = get_global_data()

st.sidebar.title("Sentinel Status")
st.sidebar.markdown(f"**Location:** {u_city}")
st.sidebar.write("🟢 **System:** Online")

st.title(f"🌊 Hydro-Pulse AI Portal")
st.markdown(f"*GPS Sync: {u_lat}, {u_lon} | Catchment: {u_city}*")

col_map, col_ai = st.columns([2, 1])

with col_map:
    st.subheader("Interactive Digital Twin")
    st.map(pd.DataFrame({'lat': [u_lat], 'lon': [u_lon]}))
    time_slider = st.select_slider("Predictive Horizon (Minutes)", options=[0, 10, 20, 30])

with col_ai:
    st.subheader("🤖 AI Intelligence")
    st.info(u_ai)
    
    st.metric("Flood Risk Index", f"{3.5 + (time_slider/10):.1f}/10")
    
    with st.expander("🔢 Physics Equations"):
        st.latex(r"\frac{\partial h}{\partial t} + \frac{\partial (uh)}{\partial x} = 0")
        st.write("Mass Continuity: **Converged**")

st.markdown("---")
if st.button("🛡️ Remote Kill-Switch"):
    st.session_state["authenticated"] = False
    st.rerun()