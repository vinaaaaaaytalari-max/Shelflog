import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
from i18n import t

st.set_page_config(
    page_title=t("dashboard_title"),
    page_icon="📊",
    layout="wide"
)

st.title(t("dashboard_title"))
st.caption(t("dashboard_caption"))

st.success(t("dashboard_welcome"))

# ---------- KPIs ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📦 Products",
        "345",
        "+12"
    )

with col2:
    st.metric(
        "👥 Employees",
        "18",
        "+2"
    )

with col3:
    st.metric(
        "🛒 Orders",
        "1,520",
        "+8%"
    )

with col4:
    st.metric(
        "💰 Revenue",
        "₹2,45,000",
        "+15%"
    )

st.divider()

# ---------- Feature Cards ----------
left, right = st.columns(2)

with left:

    st.info("""
### 📦 Inventory Management

✅ Product Management

✅ Stock Tracking

✅ Low Stock Alerts

✅ Product Search
""")

    st.info("""
### 🛒 POS Billing

✅ Quick Billing

✅ Receipt Generation

✅ Transaction History
""")

with right:

    st.info("""
### 📈 Analytics

✅ Revenue Analysis

✅ Top Products

✅ Sales Trends

✅ Business Insights
""")

    st.info("""
### 📑 Reports

✅ Daily Reports

✅ Monthly Reports

✅ Export Reports

✅ Invoice History
""")

st.divider()

# ---------- Alerts ----------
st.subheader("⚠️ Low Stock Alerts")

col1, col2, col3 = st.columns(3)

with col1:
    st.error("""
🥛 Milk

Stock Left: 8
""")

with col2:
    st.error("""
🖱 Mouse

Stock Left: 4
""")

with col3:
    st.warning("""
🎧 Headphones

Stock Left: 9
""")

st.divider()

# ---------- Quick Access ----------
st.subheader("🚀 Quick Access")

c1, c2, c3, c4 = st.columns(4)

with c1:
    if st.button(t("quick_access_inventory")):
        st.switch_page("pages/inventory.py")

with c2:
    if st.button(t("quick_access_employees")):
        st.switch_page("pages/staff.py")

with c3:
    if st.button(t("quick_access_analytics")):
        st.switch_page("pages/analytics.py")

with c4:
    if st.button(t("quick_access_voice")):
        st.switch_page("pages/voice_search.py")

st.divider()

# ---------- Recent Activity ----------
st.subheader("📋 Recent Activity")

st.success("✅ Invoice #1254 generated successfully")

st.success("✅ Rice stock updated (+50 units)")

st.warning("⚠️ Milk stock running low")

st.info("🎙 Voice search used: 'Search Laptop'")

st.success("✅ New employee added")

st.divider()

# ---------- Summary ----------
st.subheader("📌 Today's Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Invoices Generated",
        "125"
    )

with col2:
    st.metric(
        "Transactions",
        "302"
    )

with col3:
    st.metric(
        "Voice Searches",
        "47"
    )

st.caption("© 2026 Shelflog • Smart Inventory & POS Management")