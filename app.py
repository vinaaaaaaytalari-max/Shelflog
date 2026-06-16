import streamlit as st
from auth import login_page
from database import init_db, create_default_admin
from i18n import t

# Language selector (site-wide)
if "lang" not in st.session_state:
    st.session_state.lang = "en"

lang_options = [
    ("English", "en"),
    ("हिन्दी", "hi"),
    ("తెలుగు", "te"),
    ("ਪੰਜਾਬੀ", "pa"),
]

lang_labels = [l for l, _ in lang_options]
sel_idx = 0
for i, (_, code) in enumerate(lang_options):
    if st.session_state.lang == code:
        sel_idx = i

selected_label = st.selectbox("Language", lang_labels, index=sel_idx)
st.session_state.lang = dict(lang_options)[selected_label]

st.set_page_config(
    page_title=t("page_title"),
    page_icon="📦",
    layout="wide",
)

st.markdown("""
<style>

/* Main Sidebar */
section[data-testid="stSidebar"]{
    background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
    border-right: 1px solid #334155;
}

/* Sidebar title and text */
section[data-testid="stSidebar"] *{
    color: #F8FAFC !important;
}

/* Sidebar padding */
section[data-testid="stSidebar"] .block-container{
    padding-top: 2rem;
}

/* Buttons */
.stButton > button{
    width: 100%;
    border-radius: 12px;
    border: none;
    background: #2563EB;
    color: white;
    font-weight: 600;
    padding: 0.6rem;
}

.stButton > button:hover{
    background: #3B82F6;
}

/* Metric cards */
div[data-testid="metric-container"]{
    background: white;
    border: 1px solid #E2E8F0;
    padding: 15px;
    border-radius: 18px;
}

/* Success box */
div[data-testid="stAlert"]{
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# Database
init_db()
create_default_admin()

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# Hide sidebar before login
if not st.session_state.logged_in:
    st.markdown(
        """
        <style>
        section[data-testid="stSidebar"]{
            display:none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    login_page()
    st.stop()

# Welcome message
username = st.session_state.get("username", "User")
st.success(f" {t('welcome').format(user=username)}")

# Navigation pages
dashboard = st.Page("pages/dashboard.py", title="📊 Dashboard")
inventory = st.Page("pages/inventory.py", title="📦 Inventory")
employees = st.Page("pages/staff.py", title="👥 Employees")
pos = st.Page("pages/pos.py", title="🛒 POS Billing")
analytics = st.Page("pages/analytics.py", title="📈 Analytics")
reports = st.Page("pages/reports.py", title="📑 Reports")
voice = st.Page("pages/voice_search.py", title="🎙 Voice Search")

pg = st.navigation([
    dashboard,
    inventory,
    employees,
    pos,
    analytics,
    reports,
    voice,
])

pg.run()

# Logout button in sidebar
with st.sidebar:
    st.divider()
    if st.button(t("logout")):
        st.session_state.clear()
        st.switch_page("app.py")
