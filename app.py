import os
from urllib.parse import quote

import streamlit as st

# ---------- PAGE CONFIG (must be the first Streamlit call) ----------
st.set_page_config(page_title="Mama V Raw Food Ilorin", page_icon="🍚", layout="wide")

# ---------- SETTINGS ----------
PHONE_LOCAL = "09113579070"
PHONE_INTL = "2349113579070"
AREAS = "Sango, Fate, Basin, Oyun, Gaakanbi, Eleko, Oke Oyi, Post Office, Maraba, Oja, Ganmo"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def wa_link(message: str = "Hello Mama V, I want to order foodstuff") -> str:
    return f"https://wa.me/{PHONE_INTL}?text={quote(message)}"


def show_image(filename: str, caption: str) -> None:
    """Show an image; show a friendly note instead of crashing if it's missing."""
    path = os.path.join(BASE_DIR, filename)
    if os.path.exists(path):
        st.image(path, caption=caption, use_container_width=True)
    else:
        st.info(f"📷 Image not found: {filename}")


def product_card(image: str, caption: str, name: str, description: str) -> None:
    show_image(image, caption)
    st.markdown(f"**{name}** - {description}")
    st.link_button(f"Order {name}", wa_link(f"Hello Mama V, I want to order {name}"))


# ---------- HEADER ----------
st.markdown(
    f"""
    <h1 style='text-align: center; color: green;'>MAMA V RAW FOOD ILORIN</h1>
    <h3 style='text-align: center; color: orange;'>Fresh, Clean & Correctly Measured Foodstuff</h3>
    <p style='text-align: center;'>Same-Day Delivery in Ilorin | {AREAS}</p>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# ---------- WHATSAPP BUTTON ----------
st.markdown(
    f"""
    <div style='text-align: center;'>
        <a href='{wa_link()}' target='_blank'
           style='background-color: green; color: white; padding: 15px 30px;
                  text-decoration: none; font-size: 20px; border-radius: 10px;'>
            📱 Order on WhatsApp: {PHONE_LOCAL}
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")
st.subheader("Our Products - Quality & Trusted")

# ---------- PRODUCTS (2 per row) ----------
col1, col2 = st.columns(2)
with col1:
    product_card(
        "soybeans.jpg",
        "Premium Soybeans - Clean, Dry & High Quality",
        "Soybeans",
        "Clean, dry, premium quality. Available in Bags & Paints.",
    )
with col2:
    product_card(
        "rice.jpg",
        "Parboiled Rice - Pride of Africa, Ultimate Gold",
        "Rice",
        "Quality parboiled & long grain. Pride of Africa, Ultimate Gold, Original Tomatoes Rice.",
    )

col3, col4 = st.columns(2)
with col3:
    product_card(
        "garri.jpg",
        "Pure Garri - Fresh, Dry, Finely Processed",
        "Garri",
        "Clean, dry, properly processed. Ijebu & White Garri available.",
    )
with col4:
    product_card(
        "yam_elubo.jpg",
        "Yam / Elubo - Sun-Dried, Ready for Poundo",
        "Yam / Elubo",
        "Traditional, sundried & hygienic. Ready for Poundo.",
    )

col5, col6 = st.columns(2)
with col5:
    product_card(
        "groundnut.jpg",
        "Groundnut - Raw, Clean & Ready for Use",
        "Groundnut",
        "Raw, clean, fresh groundnut.",
    )
with col6:
    product_card(
        "elubo_bags.jpg",
        "Elubo Bags - Wholesale & Retail",
        "Elubo Bags",
        "Available in wholesale & retail quantities.",
    )

# ---------- WHY CHOOSE US ----------
st.markdown("---")
st.subheader("Why Choose Mama V?")
st.markdown(
    """
✅ Measured Correctly & Fair  
✅ Clean & Hygienic Packaging  
✅ Wholesale & Retail Available  
✅ 100% SAFE, Locally Sourced, Affordable  
✅ Same-Day Delivery in Ilorin
"""
)

# ---------- FOOTER ----------
st.markdown("---")
st.markdown(
    f"""
    <div style='background-color: orange; color: black; padding: 20px;
                border-radius: 10px; text-align: center;'>
        <h2>📍 Delivery Areas: {AREAS}</h2>
        <h2>📞 Call/WhatsApp: {PHONE_LOCAL}</h2>
        <p>Available 8am to 7pm Daily | Location: Ilorin, Kwara State</p>
    </div>
    """,
    unsafe_allow_html=True,
)
