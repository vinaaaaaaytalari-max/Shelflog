import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
import pandas as pd
from i18n import t

st.title(t("employees_title"))

if "employees" not in st.session_state:
    st.session_state.employees = []

employees = pd.DataFrame({
    "Employee ID":[1,2,3,4],
    "Name":["Rahul Sharma","Priya Reddy","Arjun Kumar","Sneha Patel"],
    "Role":["Manager","Cashier","Inventory Staff","Sales Executive"],
    "Salary":[50000,25000,30000,28000]
})

st.dataframe(employees, use_container_width=True)

st.subheader(t("add_employee"))

name = st.text_input(t("employee_name"), placeholder=t("employee_name"))

role = st.selectbox(
    t("role"),
    [
        "Manager",
        "Cashier",
        "Inventory Staff",
        "Sales Executive"
    ]
)

salary = st.number_input(
    t("salary"),
    min_value=0
)

if st.button(t("add_employee_button")):
    st.session_state.employees.append({
        "Name": name,
        "Role": role,
        "Salary": salary
    })
    st.success(t("employee_added"))

st.markdown("---")

st.subheader("Current Employees")

if st.session_state.employees:
    st.dataframe(pd.DataFrame(st.session_state.employees), use_container_width=True)
else:
    st.info(t("no_employees"))
