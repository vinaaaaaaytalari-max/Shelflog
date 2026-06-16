import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
import pandas as pd
import plotly.express as px
from i18n import t

st.set_page_config(layout="wide")

st.title(t("analytics_title"))
st.caption(t("analytics_caption"))

# ------------------------
# KPI CARDS
# ------------------------
c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Revenue", "₹2,45,000", "+15%")
c2.metric("🛒 Orders", "1,520", "+8%")
c3.metric("🧾 Invoices", "1,245", "+11%")
c4.metric("⚠️ Low Stock Items", "12", "-3")

st.divider()

# ------------------------
# REVENUE TREND
# ------------------------
sales = pd.DataFrame({
    "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
    "Revenue": [120000,145000,170000,190000,220000,245000]
})

fig1 = px.line(
    sales,
    x="Month",
    y="Revenue",
    markers=True,
    title="Monthly Revenue Trend"
)

# ------------------------
# CATEGORY SALES
# ------------------------
category = pd.DataFrame({
    "Category":["Groceries","Electronics","Stationery","Fashion"],
    "Sales":[40,30,20,10]
})

fig2 = px.pie(
    category,
    values="Sales",
    names="Category",
    hole=0.55,
    title="Sales Distribution"
)

left, right = st.columns(2)

with left:
    st.plotly_chart(fig1, use_container_width=True)

with right:
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ------------------------
# TOP PRODUCTS
# ------------------------
st.subheader("🔥 Top Selling Products")

products = pd.DataFrame({
    "Product":["Rice","Milk","Laptop","Mouse","Soap"],
    "Units Sold":[320,290,160,140,100]
})

fig3 = px.bar(
    products,
    x="Product",
    y="Units Sold",
    color="Units Sold",
    text_auto=True
)

st.plotly_chart(fig3, use_container_width=True)

# ------------------------
# FEATURE PERFORMANCE
# ------------------------
st.subheader("🚀 Feature Usage")

a, b, c = st.columns(3)

with a:
    st.info("🛒 POS Billing")
    st.metric("Transactions", "3,120")
    st.progress(92)

with b:
    st.info("🧾 Invoice Generation")
    st.metric("Invoices", "1,245")
    st.progress(85)

with c:
    st.info("🎙 Voice Search")
    st.metric("Voice Searches", "458")
    st.progress(68)

st.divider()

# ------------------------
# LOW STOCK ALERTS
# ------------------------
st.subheader("⚠️ Low Stock Alerts")

low_stock = pd.DataFrame({
    "Product":["Milk","Bread","Mouse","Soap"],
    "Stock":[8,6,4,9]
})

st.dataframe(low_stock, use_container_width=True)

# ------------------------
# REPORT SUMMARY
# ------------------------
st.subheader("📑 Report Summary")

col1, col2 = st.columns(2)

with col1:
    st.success("""
### Inventory

✅ 345 Products

✅ 27 Restocked

⚠️ 12 Low Stock
""")

with col2:
    st.success("""
### Sales

💰 Revenue +15%

🛒 1,520 Orders

📈 Growth Trend Positive
""")

st.divider()

# ------------------------
# AI INSIGHTS
# ------------------------
st.subheader("🤖 Smart Insights")

st.success("""
✅ Revenue increased by 15%.

✅ Groceries are the best-selling category.

✅ Milk and Bread require immediate restocking.

✅ POS billing activity is strong.

✅ Voice search usage continues to rise.

✅ Inventory turnover remains healthy.
""")