import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
import pandas as pd
from i18n import t

# ---------------- PAGE ----------------
st.set_page_config(
    page_title="POS Billing",
    page_icon="🛒",
    layout="wide"
)

st.title(t("pos_title"))
st.caption(t("pos_caption"))

# ---------------- PRODUCTS ----------------
products = {
    "Rice": 60,
    "Milk": 35,
    "Bread": 40,
    "Eggs": 90,
    "Coffee": 350,
    "Tea": 220,
    "Soap": 50,
    "Shampoo": 180,
    "Toothpaste": 95,
    "Laptop": 55000,
    "Mouse": 799,
    "Keyboard": 1499,
    "Headphones": 2499,
    "Smartphone": 25000,
    "USB Cable": 299
}

# ---------------- CUSTOMER DETAILS ----------------
st.subheader(t("customer_details"))

col1, col2 = st.columns(2)

with col1:
    customer_name = st.text_input(t("customer_name_label"))

with col2:
    customer_phone = st.text_input(t("phone_number_label"))

st.divider()

# ---------------- BILL ITEMS ----------------
st.subheader(t("add_products"))

num_items = st.number_input(
    t("number_of_products"),
    min_value=1,
    max_value=20,
    value=1
)

bill_items = []
subtotal = 0

for i in range(num_items):

    c1, c2 = st.columns([3, 1])

    with c1:
            product = st.selectbox(
                f"{t('product_label')} {i+1}",
                list(products.keys()),
                key=i
            )

    with c2:
        qty = st.number_input(
            t("qty_label"),
            min_value=1,
            value=1,
            key=f"qty{i}"
        )

    amount = products[product] * qty

    bill_items.append(
        [
            product,
            qty,
            products[product],
            amount
        ]
    )

    subtotal += amount

# ---------------- INVOICE ----------------
st.subheader(t("invoice_label"))

df = pd.DataFrame(
    bill_items,
    columns=[
        "Product",
        "Quantity",
        "Price",
        "Amount"
    ]
)

st.dataframe(df, use_container_width=True)

gst = subtotal * 0.18
grand_total = subtotal + gst

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Subtotal",
        f"₹{subtotal:.2f}"
    )

with col2:
    st.metric(
        "GST (18%)",
        f"₹{gst:.2f}"
    )

with col3:
    st.metric(
        "Grand Total",
        f"₹{grand_total:.2f}"
    )

st.divider()

# ---------------- PAYMENT ----------------
payment = st.selectbox(
    "💳 Payment Method",
    [
        "Cash",
        "UPI",
        "Card"
    ]
)

if st.button("✅ Generate Invoice"):

    st.success("Invoice generated successfully!")

    st.info(f"""
Customer: {customer_name}

Phone: {customer_phone}

Payment Method: {payment}

Grand Total: ₹{grand_total:.2f}
""")

    st.balloons()

st.divider()

# ---------------- RECENT TRANSACTIONS ----------------
st.subheader(t("recent_transactions"))

transactions = pd.DataFrame({
    "Invoice ID": [1001, 1002, 1003, 1004],
    "Customer": ["Rahul", "Priya", "Arjun", "Sneha"],
    "Amount": [850, 1250, 3500, 650],
    "Payment": ["UPI", "Cash", "Card", "UPI"]
})

st.dataframe(transactions, use_container_width=True)