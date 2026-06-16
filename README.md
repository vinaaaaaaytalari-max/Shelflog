# Smart Inventory Prototype

Lightweight Streamlit app for inventory, POS, invoices, and analytics.

## Deploy to Streamlit Community Cloud

1. Go to https://share.streamlit.io/new and connect your GitHub account.
2. Select the repository `vinaytalari101-beep/prototype`, branch `main` and set the entrypoint to `app.py`.
3. Ensure the `requirements.txt` file is present (the repo already contains one).
4. (Optional) Configure any repo secrets via the Streamlit app settings if you add cloud DB credentials later.

Notes:
- This prototype uses a local SQLite file (`inventory.db`). Streamlit Community Cloud filesystem is ephemeral — data will not persist across deploys or restarts. For production, use an external database (Postgres, MySQL) and store credentials in `st.secrets`.

## Run locally

Create and activate a venv, install dependencies, then run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Notes & Troubleshooting
- If `fpdf` font warnings appear, `fpdf2` is used and fonts are set to core fonts in `invoice.py`.
- If audio features require `pyaudio`, additional system libs may be needed on your machine.

## Files of interest
- `app.py` — main Streamlit app entrypoint
- `database.py` — DB helpers and migrations
- `pages/` — page modules (Inventory, POS, Reports, Dashboard)
# prototype