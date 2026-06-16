import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
import pandas as pd
from i18n import t

# ---------------- PAGE ----------------
st.set_page_config(
    page_title="Reports",
    page_icon="📑",
    layout="wide"
)

st.title("📑 Reports")
st.caption("View sales, inventory, and performance reports")

# ---------------- SUMMARY CARDS ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Revenue", "₹2,45,000", "+15%")

with col2:
    st.metric("🛒 Orders", "1,520", "+8%")

with col3:
    st.metric("🧾 Invoices", "1,245", "+11%")

with col4:
    st.metric("📦 Products", "345", "+12")

st.divider()

# ---------------- SALES REPORT ----------------
st.subheader("🛒 Sales Report")

sales_df = pd.DataFrame({
    "Invoice ID":[1001,1002,1003,1004,1005],
    "Customer":["Rahul","Priya","Arjun","Sneha","Vikram"],
    "Amount":[850,1250,3499,560,2400],
    "Payment":["UPI","Cash","Card","UPI","Cash"]
})

st.dataframe(
    sales_df,
    use_container_width=True
)

st.divider()

# ---------------- INVENTORY REPORT ----------------
st.subheader("📦 Inventory Report")

inventory_df = pd.DataFrame({
    "Product":["Rice","Milk","Laptop","Mouse","Headphones"],
    "Stock":[120,8,15,4,9],
    "Status":[
        "In Stock",
        "Critical",
        "Running Low",
        "Critical",
        "Critical"
    ]
})

st.dataframe(
    inventory_df,
    use_container_width=True
)

st.divider()

# ---------------- LOW STOCK REPORT ----------------
st.subheader("⚠️ Low Stock Products")

st.error("🥛 Milk - 8 units left")
st.error("🖱 Mouse - 4 units left")
st.warning("🎧 Headphones - 9 units left")

st.divider()

# ---------------- EMPLOYEE REPORT ----------------
st.subheader("👥 Employee Report")

employee_df = pd.DataFrame({
    "Employee ID":[101,102,103,104],
    "Name":["Rahul Sharma","Priya Reddy","Arjun Kumar","Sneha Patel"],
    "Role":["Manager","Cashier","Inventory Staff","Sales Executive"]
})

st.dataframe(
    employee_df,
    use_container_width=True
)

st.divider()

# ---------------- TOP PRODUCTS ----------------
st.subheader("🔥 Top Selling Products")

top_products = pd.DataFrame({
    "Product":["Rice","Milk","Coffee","Laptop","Soap"],
    "Units Sold":[320,290,180,95,150]
})

st.bar_chart(
    top_products.set_index("Product")
)

st.divider()

# ---------------- DOWNLOAD REPORT ----------------
st.subheader("⬇ Download Reports")

csv = sales_df.to_csv(index=False)

st.download_button(
    label=t("download_sales_report"),
    data=csv,
    file_name="sales_report.csv",
    mime="text/csv"
)

st.success(t("reports_generated"))