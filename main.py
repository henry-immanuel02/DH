import streamlit as st
import random
import base64

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Pokémon Valentine",
    page_icon="⚡",
    layout="wide"
)

# ==============================
# SESSION STATE
# ==============================
if "answered_yes" not in st.session_state:
    st.session_state.answered_yes = False

if "nay_count" not in st.session_state:
    st.session_state.nay_count = 0

if "starter" not in st.session_state:
    st.session_state.starter = random.choice(["Pikachu", "Eevee", "Charmander"])

# ==============================
# POKEMON DATA
# ==============================
pokemon_data = {
    "Pikachu": {
        "hp": 100,
        "img": "https://img.pokemondb.net/artwork/large/pikachu.jpg",
        "evolve_name": "Raichu",
        "evolve_img": "https://img.pokemondb.net/artwork/large/raichu.jpg"
    },
    "Eevee": {
        "hp": 100,
        "img": "https://img.pokemondb.net/artwork/large/eevee.jpg",
        "evolve_name": "Sylveon",
        "evolve_img": "https://img.pokemondb.net/artwork/large/sylveon.jpg"
    },
    "Charmander": {
        "hp": 100,
        "img": "https://img.pokemondb.net/artwork/large/charmander.jpg",
        "evolve_name": "Charizard",
        "evolve_img": "https://img.pokemondb.net/artwork/large/charizard.jpg"
    }
}

legendary_data = {
    "Mew": "https://img.pokemondb.net/artwork/large/mew.jpg",
    "Lugia": "https://img.pokemondb.net/artwork/large/lugia.jpg",
    "Rayquaza": "https://img.pokemondb.net/artwork/large/rayquaza.jpg"
}

starter = st.session_state.starter
starter_info = pokemon_data[starter]

# ==============================
# STYLE
# ==============================
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #f8fbff 0%, #eaf2fb 100%);
}

.center-wrapper {
    max-width: 900px;
    margin: 0 auto;
}

.main-card {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(14px);
    border-radius: 28px;
    padding: 70px 60px;
    box-shadow: 0 25px 60px rgba(0,0,0,0.08);
    border: 1px solid rgba(255,255,255,0.6);
    text-align: center;
    margin-top: 70px;
}

.title-text {
    font-size: 40px;
    font-weight: 600;
    color: #1f2d3d;
    margin-bottom: 12px;
}

.subtitle-text {
    font-size: 19px;
    color: #6b7a90;
    margin-bottom: 40px;
}

.hp-bar {
    height: 20px;
    border-radius: 10px;
    background-color: #e0e6f0;
    margin: 15px 0 30px 0;
    overflow: hidden;
}

.hp-fill {
    height: 100%;
    background-color: #1f77b4;
    transition: width 0.3s ease;
}

div[data-testid="stButton"] button {
    transition: all 0.25s ease-in-out;
    border-radius: 18px !important;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# BEFORE YES
# ==============================
if not st.session_state.answered_yes:

    hp_remaining = max(100 - (st.session_state.nay_count * 15), 5)

    scale = 1.25 ** st.session_state.nay_count
    yay_font = 22 + (st.session_state.nay_count * 8)
    yay_padding = 16 + (st.session_state.nay_count * 5)

    st.markdown("""
    <div class="center-wrapper">
        <div class="main-card">
    """, unsafe_allow_html=True)

    # Pokemon image
    st.markdown(f"""
    <img src="{starter_info['img']}" width="200">
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="title-text">{starter} wants to ask you something...</div>
    <div class="subtitle-text">Would you like to be my Valentine?</div>
    """, unsafe_allow_html=True)

    # HP BAR
    st.markdown(f"""
    <div class="hp-bar">
        <div class="hp-fill" style="width:{hp_remaining}%"></div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.nay_count > 0:
        st.caption(f"{starter}'s Heart HP: {hp_remaining}% 💔")

    col1, col2 = st.columns([2,1])

    with col1:
        st.markdown(f"""
        <style>
        div[data-testid="stButton"] button[kind="primary"] {{
            font-size: {yay_font}px !important;
            padding: {yay_padding}px {yay_padding*2}px !important;
            transform: scale({scale});
            background-color: #1f77b4 !important;
            color: white !important;
        }}
        </style>
        """, unsafe_allow_html=True)

        if st.button("YES 💙", type="primary"):
            st.session_state.answered_yes = True
            st.rerun()

    with col2:
        if st.button("No"):
            st.session_state.nay_count += 1
            st.rerun()

    st.markdown("</div></div>", unsafe_allow_html=True)

# ==============================
# AFTER YES
# ==============================
else:

    legend_name = random.choice(list(legendary_data.keys()))

    st.markdown("""
    <div class="center-wrapper">
        <div class="main-card">
    """, unsafe_allow_html=True)

    # Evolution
    st.markdown(f"""
    <div class="title-text" style="color:#1f77b4;">
        {starter} is evolving...
    </div>
    """, unsafe_allow_html=True)

    st.image(starter_info["evolve_img"], width=250)

    st.markdown(f"""
    <div class="subtitle-text">
        Congratulations! It evolved into {starter_info['evolve_name']} 💙
    </div>
    """, unsafe_allow_html=True)

    st.balloons()

    st.markdown(f"""
    <hr style="margin:40px 0;">
    <img src="{legendary_data[legend_name]}" width="250">
    <div class="subtitle-text">
        Legendary Blessing Unlocked: {legend_name} ✨
    </div>
    """, unsafe_allow_html=True)

    st.success("You unlocked the rarest item: Lifetime Commitment Badge.")

    if st.button("Reset Game"):
        st.session_state.answered_yes = False
        st.session_state.nay_count = 0
        st.session_state.starter = random.choice(["Pikachu", "Eevee", "Charmander"])
        st.rerun()

    st.markdown("</div></div>", unsafe_allow_html=True)
