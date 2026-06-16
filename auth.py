import streamlit as st
from i18n import t


def login_page():
    st.markdown(
        """
        <style>
        #MainMenu, footer, header {visibility: hidden;}

        body {
            background-color: #f5f7fb;
        }

        .login-box {
            max-width: 420px;
            margin: auto;
            margin-top: 10vh;
            padding: 30px;
            background: white;
            border-radius: 14px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        }

        .title {
            text-align: center;
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 5px;
        }

        .subtitle {
            text-align: center;
            color: gray;
            font-size: 14px;
            margin-bottom: 20px;
        }

        .demo-text {
            text-align: center;
            color: #64748b;
            font-size: 12px;
            margin-bottom: 20px;
        }

        .stButton>button {
            width: 100%;
            background: #2563eb;
            color: white;
            border-radius: 10px;
            padding: 10px;
            font-weight: 600;
        }

        .stButton>button:hover {
            background: #1d4ed8;
        }

        /* Mobile */
        @media (max-width: 600px) {
            .login-box {
                margin-top: 6vh;
                padding: 20px;
            }

            .title {
                font-size: 22px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown(f'<div class="title">📦 {t("page_title")}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="subtitle">{t("login_description")}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="demo-text">{t("login_demo")}</div>',
        unsafe_allow_html=True,
    )

    username = st.text_input(t("username"), max_chars=10, placeholder=t("username"))
    password = st.text_input(
        t("password"),
        type="password",
        placeholder=t("password"),
    )

    if st.button(t("sign_in")):
        if username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error(t("invalid_credentials"))

    st.markdown("</div>", unsafe_allow_html=True)
