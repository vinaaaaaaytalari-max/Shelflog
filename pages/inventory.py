import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
import pandas as pd
from i18n import t

st.title(t("inventory_title"))
st.caption(t("inventory_caption"))

if "products" not in st.session_state:
    st.session_state.products = []

# Search
search = st.text_input(t("search_products"))

# Products
products = [
    {"name":"Rice","price":60,"stock":120,"image":"https://images.unsplash.com/photo-1586201375761-83865001e31c?w=500"},
    {"name":"Milk","price":35,"stock":8,"image":"https://images.unsplash.com/photo-1550583724-b2692b85b150?w=500"},
    {"name":"Bread","price":40,"stock":15,"image":"https://images.unsplash.com/photo-1509440159596-0249088772ff?w=500"},
    {"name":"Eggs","price":90,"stock":30,"image":"https://images.unsplash.com/photo-1518569656558-1f25e69d93d7?w=500"},
    {"name":"Coffee","price":350,"stock":20,"image":"https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=500"},
    {"name":"Tea","price":220,"stock":28,"image":"https://images.unsplash.com/photo-1544787219-7f47ccb76574?w=500"},
    {"name":"Soap","price":50,"stock":25,"image":"https://images.unsplash.com/photo-1584305574647-acf8069a3d3d?w=500"},
    {"name":"Laptop","price":55000,"stock":15,"image":"https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500"},
    {"name":"Mouse","price":799,"stock":4,"image":"https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500"},
    {"name":"Keyboard","price":1499,"stock":18,"image":"https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?w=500"},
    {"name":"Headphones","price":2499,"stock":9,"image":"https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"},
    {"name":"Smartphone","price":25000,"stock":11,"image":"https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500"},
    
]

# Search filter
if search:
    products = [
        p for p in products
        if search.lower() in p["name"].lower()
    ]

cols = st.columns(3)

for i, product in enumerate(products):

    with cols[i % 3]:

        st.image(product["image"])

        st.subheader(product["name"])

        st.write(f"💰 ₹{product['price']}")
        st.write(f"📦 Stock: {product['stock']}")

        # Stock status
        if product["stock"] > 50:
            st.success(t("in_stock"))

        elif product["stock"] > 10:
            st.warning(t("running_low"))

        else:
            st.error(t("critical_stock"))

        st.progress(min(product["stock"]/100,1.0))

        c1, c2 = st.columns(2)

        with c1:
            if st.button(t("edit"), key=f"edit{i}"):
                st.session_state.edit_index = i

        with c2:
            if st.button(t("delete"), key=f"delete{i}"):
                products.pop(i)
                st.rerun()

        st.divider()

# Edit Product Section
if "edit_index" in st.session_state:
    idx = st.session_state.edit_index

    with st.expander("✏️ " + t("edit"), expanded=True):
        new_name = st.text_input(
            t("product_name"),
            value=products[idx]["name"]
        )
        new_price = st.number_input(
            t("price"),
            value=products[idx]["price"]
        )
        new_stock = st.number_input(
            t("stock_quantity"),
            value=products[idx]["stock"]
        )

        if st.button("💾 " + t("add_product_button")):
            products[idx]["name"] = new_name
            products[idx]["price"] = new_price
            products[idx]["stock"] = new_stock

            del st.session_state.edit_index
            st.success("✅ " + t("product_added").format(name=new_name))
            st.rerun()

# Add Product Section
st.markdown("---")

st.subheader(t("add_product"))

col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input(t("product_name"), placeholder=t("product_name"))

with col2:
    price = st.number_input(
        t("price"),
        min_value=0
    )

with col3:
    stock = st.number_input(
        t("stock_quantity"),
        min_value=0
    )
if st.button(t("add_product_button")):
    st.session_state.products.append({
        "Name": name,
        "Price": price,
        "Stock": stock
    })
    st.success(t("product_added").format(name=name))

st.markdown("---")

st.subheader("Current Products")

if st.session_state.products:
    st.dataframe(pd.DataFrame(st.session_state.products), width='stretch')
else:
    st.info(t("no_products"))