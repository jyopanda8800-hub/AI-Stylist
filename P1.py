import streamlit as st
from PIL import Image
import cv2
import numpy as np

# ------------------- SETTINGS -------------------
DRESS_FOLDER = "./dresses"  # Optional: keep images organized
# ------------------------------------------------

# ------------------- SKIN TONE DETECTION -------------------
def detect_skin_tone(image: Image.Image):
    """Detect skin tone (Fair, Wheatish, Dusky) from uploaded face image."""
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 30, 60], dtype=np.uint8)
    upper = np.array([20, 150, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower, upper)

    skin = cv2.bitwise_and(img, img, mask=mask)
    skin_pixels = skin[np.where(mask != 0)]
    if len(skin_pixels) == 0:
        return "Unknown"

    avg_color = np.mean(skin_pixels, axis=0)  # BGR
    r, g, b = avg_color[::-1]

    brightness = (r + g + b) / 3
    if brightness > 180:
        return "Fair"
    elif brightness > 100:
        return "Wheatish"
    else:
        return "Dusky"

# ------------------- PRODUCT DATA -------------------
male_products = {
    "Dusky": [
        {
            "name": "Blue Patterned Johnny Polo T-Shirt",
            "image": "dusky_livid.jpg",
            "link": "https://www.pantaloons.com/p/blue-patterned-johnny-polo-t-shirt-1138432.html"
        },
        {
            "name": "Grey Contrast Detailed Johnny Polo T-Shirt",
            "image": "dusky_olive.jpg",
            "link": "https://www.pantaloons.com/p/grey-contrast-detailed-johnny-polo-t-shirt-1137917.html"
        },
        {
            "name": "Wine Solid Formal Half Sleeves Polo T-Shirt",
            "image": "dusky_burgundy.jpg",
            "link": "https://www.pantaloons.com/p/wine-solid-formal-half-sleeves-polo-collar-men-slim-fit-t-shirt-1140378.html"
        },
    ],
    "FairCool": [
        {
            "name": "Blue Acid Washed Typographic T-Shirt",
            "image": "faircool_darkblue.jpg",
            "link": "https://www.pantaloons.com/p/blue-acid-washed-t-shirt-with-typographic-prints-1138164.html"
        },
        {
            "name": "Light Blue Striped Casual T-Shirt",
            "image": "faircool_lightblue.jpg",
            "link": "https://www.pantaloons.com/p/aqua-striped-oversized-t-shirt-1144289.html"
        },
    ],
    "Wheatish": [
        {
            "name": "Green Solid Formal Polo T-Shirt",
            "image": "wheatish_darkolive.jpg",
            "link": "https://www.pantaloons.com/p/green-solid-formal-half-sleeves-polo-collar-men-slim-fit-t-shirt-1140377.html"
        },
        {
            "name": "Off-White Solid Johnny Polo T-Shirt",
            "image": "wheatish_beige.jpg",
            "link": "https://www.pantaloons.com/p/off-white-solid-johnny-polo-t-shirt-1136818.html"
        },
        {
            "name": "Off White Striped Relaxed Fit T-Shirt",
            "image": "wheatish_offwhite.jpg",
            "link": "https://www.pantaloons.com/p/off-white-striped-relaxed-fit-t-shirt-1141348.html"
        },
    ],
    "FairWarm": [
        {
            "name": "Red Solid Slim Fit T-Shirt",
            "image": "fairwarm_red.jpg",
            "link": "https://www.pantaloons.com/p/red-solid-slim-fit-t-shirt-1138505.html"
        },
        {
            "name": "Off-White Striped Polo T-Shirt",
            "image": "fairwarm_ivory.jpg",
            "link": "https://www.pantaloons.com/p/off-white-striped-polo-t-shirt-1141568.html"
        },
        {
            "name": "Mauve Statement Graphic T-Shirt",
            "image": "fairwarm_coral.jpg",
            "link": "https://www.pantaloons.com/p/mauve-statement-graphic-t-shirt-1136797.html"
        },
    ],
}

female_products = {
    "FairWarm": [
        {"name": "Coral Dress", "image": "fairwarm_coral_female.jpg", "link": "https://www.pantaloons.com/p/coral-dress-785374.html?utm_source=chatgpt.com"},
        {"name": "Beige Solid Top", "image": "fairwarm_beige_female.jpg", "link": "https://www.pantaloons.com/p/beige-solid-top-628876.html?utm_source=chatgpt.com"},
        {"name": "Peach Printed Dress", "image": "fairwarm_peach_female.jpg", "link": "https://www.pantaloons.com/p/peach-printed-dress-686256.html?utm_source=chatgpt.com"},
        {"name": "Warm Brown Top", "image": "fairwarm_warmbrown_female.jpg", "link": "https://www.pantaloons.com/p/brown-top-39781983.html?utm_source=chatgpt.com"},
    ],
    "Wheatish": [
        {"name": "Teal Dress", "image": "wheatish_teal_female.jpg", "link": "https://www.pantaloons.com/p/teal-dress-792368.html?utm_source=chatgpt.com"},
        {"name": "Plum Top", "image": "wheatish_plum_female.jpg", "link": "https://www.pantaloons.com/p/plum-top-766698.html?utm_source=chatgpt.com"},
        {"name": "Turquoise Dress", "image": "wheatish_turquoise_female.jpg", "link": "https://www.pantaloons.com/p/turquoise-dress-861734.html?utm_source=chatgpt.com"},
        {"name": "Grey Dress", "image": "wheatish_grey_female.jpg", "link": "https://www.pantaloons.com/p/grey-dress-803985.html?utm_source=chatgpt.com"},
    ],
    "FairCool": [
        {"name": "Navy Dress", "image": "faircool_navy_female.jpg", "link": "https://www.pantaloons.com/p/navy-print-ankle-length-ethnic-women-straight-fit-dress-910561.html?utm_source=chatgpt.com"},
        {"name": "Lavender Dress", "image": "faircool_lavender_female.jpg", "link": "https://www.pantaloons.com/p/lavender-blue-dress-761846.html?utm_source=chatgpt.com"},
        {"name": "Ice Blue Top", "image": "faircool_iceblue_female.jpg", "link": "https://www.pantaloons.com/p/lavender-blue-top-767994.html?utm_source=chatgpt.com"},
        {"name": "Charcoal Dress", "image": "faircool_charcoal_female.jpg", "link": "https://www.pantaloons.com/p/charcoal-dress-699056.html?utm_source=chatgpt.com"},
    ],
    "Dusky": [
        {"name": "Maroon Dress", "image": "dusky_maroon_female.jpg", "link": "https://www.pantaloons.com/p/annabelle-maroon-dress-312293.html?utm_source=chatgpt.com"},
        {"name": "Mustard Dress", "image": "dusky_mustard_female.jpg", "link": "https://www.pantaloons.com/p/mustard-dress-544096.html?utm_source=chatgpt.com"},
        {"name": "Olive Dress", "image": "dusky_olive_female.jpg", "link": "https://www.pantaloons.com/p/olive-regular-fit-casual-women-dresses-1012698.html?utm_source=chatgpt.com"},
        {"name": "Gold Dress", "image": "dusky_gold_female.jpg", "link": "https://www.pantaloons.com/p/poly-silk-evening-wear-dress-285374.html?utm_source=chatgpt.com"},
    ],
}



# ------------------- PAGE CONFIG -------------------
st.set_page_config(page_title="AI Specialist", page_icon="🤖", layout="centered")

# ------------------- GLOBAL CSS -------------------
st.markdown(
    """
    <style>
    body { background-color: #E6F7F7; }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #006400;
        margin-bottom: 20px;
    }
    .subtitle {
        text-align: center;
        font-size: 24px;
        font-weight: 600;
        color: #00AA8A;
        margin-bottom: 20px;
    }
    .card {
        border: 2px solid #00AA8A;
        border-radius: 20px;
        padding: 15px;
        background-color: #ffffff;
        box-shadow: 2px 4px 10px rgba(0,0,0,0.15);
        text-align: center;
        transition: transform 0.2s;
        cursor: pointer;
        margin-bottom: 20px;
    }
    .card:hover {
        transform: scale(1.05);
        border: 2px solid #006400;
        background-color: #F8FFFE;
    }
    .card-title {
        font-size: 18px;
        font-weight: bold;
        color: #003333;
        margin-bottom: 10px;
    }
    .offer-box {
        background-color: #00AA8A40;
        border-radius: 10px;
        padding: 8px;
        margin-top: 10px;
    }
    .offer-text {
        color: #006400;
        font-weight: bold;
        font-size: 14px;
        text-align: center;
    }
    a {
        text-decoration: none !important;
        color: inherit !important;
    }
    /* Big Gender Buttons */
    .gender-btn {
        width: 180px;
        height: 180px;
        font-size: 50px;
        font-weight: bold;
        color: white;
        background-color: #00AA8A;
        border: 3px solid white;
        border-radius: 20px;
        margin: 20px auto;
        text-align: center;
        cursor: pointer;
        transition: transform 0.2s, background-color 0.2s;
    }
    .gender-btn:hover {
        transform: scale(1.1);
        background-color: #008070;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------- STATE -------------------
if "gender" not in st.session_state:
    st.session_state.gender = None

# ------------------- APP FLOW -------------------
st.markdown('<div class="title">AI Stylist</div>', unsafe_allow_html=True)

if st.session_state.gender is None:
    st.markdown('<div class="subtitle">Choose your Gender</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("👨 Male", use_container_width=True):
            st.session_state.gender = "Male"
            st.rerun()
    with col2:
        if st.button("👩 Female", use_container_width=True):
            st.session_state.gender = "Female"
            st.rerun()

else:
    if st.button("⬅️ Back"):
        st.session_state.gender = None
        st.rerun()

    if st.session_state.gender == "Male":
        st.markdown("<div class='subtitle'>📸 Take a photo to get recommendations</div>", unsafe_allow_html=True)
        photo = st.camera_input("")

        if photo:
            img = Image.open(photo)
            skin_tone = detect_skin_tone(img)
            

            if skin_tone in male_products:
                st.markdown("### ✨ Here are some Smart AI picks we think you'll rock")
                cols = st.columns(3)
                for i, item in enumerate(male_products[skin_tone]):
                    with cols[i % 3]:
                        st.markdown(
                            f"""
                            <a href="{item['link']}" target="_blank">
                                <div class="card">
                                    <div class="card-title">{item['name']}</div>
                                    <div class="offer-box">
                                        <div class="offer-text">Get it exclusively in Pantaloons</div>
                                    </div>
                                </div>
                            </a>
                            """,
                            unsafe_allow_html=True,
                        )
            else:
                st.warning("Sorry, no recommendations for this skin tone yet.")

    elif st.session_state.gender == "Female":
        st.markdown("<div class='subtitle'>📸 Take a photo to get recommendations</div>", unsafe_allow_html=True)
        photo = st.camera_input("")

        if photo:
            img = Image.open(photo)
            skin_tone = detect_skin_tone(img)

            # map brightness-based tones into female keys
            tone_key = "Dusky" if skin_tone == "Dusky" else "Fair (Warm)"  # fallback mapping
            if tone_key in female_products:
                st.markdown("### 👗 Here are some Smart AI picks for you")
                cols = st.columns(3)
                for i, item in enumerate(female_products[tone_key]):
                    with cols[i % 3]:
                        st.markdown(
                            f"""
                            <a href="{item['link']}" target="_blank">
                                <div class="card">
                                    <div class="card-title">{item['name']}</div>
                                    <div class="offer-box">
                                        <div class="offer-text">Pantaloons Exclusive</div>
                                    </div>
                                </div>
                            </a>
                            """,
                            unsafe_allow_html=True,
                        )
            else:
                st.warning("Sorry, no recommendations for this skin tone yet.")
