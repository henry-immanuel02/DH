import streamlit as st
import random

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
        "img": "https://img.pokemondb.net/artwork/large/pikachu.jpg",
        "evolve_name": "Raichu",
        "evolve_img": "https://img.pokemondb.net/artwork/large/raichu.jpg"
    },
    "Eevee": {
        "img": "https://img.pokemondb.net/artwork/large/eevee.jpg",
        "evolve_name": "Sylveon",
        "evolve_img": "https://img.pokemondb.net/artwork/large/sylveon.jpg"
    },
    "Charmander": {
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
# GLOBAL STYLE (STABLE CARD)
# ==============================
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #f8fbff 0%, #eaf2fb 100%);
}

/* Main Card Container */
.block-container {
    max-width: 900px;
    margin: 70px auto;
    background: rgba(255,255,255,0.90);
    backdrop-filter: blur(14px);
    padding: 70px 60px;
    border-radius: 28px;
    box-shadow: 0 25px 60px rgba(0,0,0,0.08);
    border: 1px solid rgba(255,255,255,0.6);
}

/* Typography */
.title-text {
    font-size: 40px;
    font-weight: 600;
    color: #1f2d3d;
    text-align:center;
    margin-bottom: 10px;
}

.subtitle-text {
    font-size: 19px;
    color: #6b7a90;
    text-align:center;
    margin-bottom: 40px;
}

/* HP BAR */
.hp-container {
    margin: 25px 0 35px 0;
}

.hp-bar {
    height: 22px;
    border-radius: 12px;
    background-color: #e4e9f2;
    overflow: hidden;
}

.hp-fill {
    height: 100%;
    background: linear-gradient(90deg, #1f77b4, #3aa0ff);
    transition: width 0.4s ease-in-out;
}

/* Buttons */
div[data-testid="stButton"] button {
    border-radius: 18px !important;
    font-weight: 600;
    transition: all 0.25s ease-in-out;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# BEFORE YES
# ==============================
if not st.session_state.answered_yes:

    hp_remaining = max(100 - (st.session_state.nay_count * 15), 5)

    scale = 1.2 ** st.session_state.nay_count
    yay_font = 20 + (st.session_state.nay_count * 6)
    yay_padding = 14 + (st.session_state.nay_count * 4)

    st.markdown(f"""
    <div style="text-align:center;">
        <img src="{starter_info['img']}" width="220">
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="title-text">{starter} has something important to ask…</div>
    <div class="subtitle-text">Would you like to be my Valentine?</div>
    """, unsafe_allow_html=True)

    # HP BAR
    st.markdown(f"""
    <div class="hp-container">
        <div class="hp-bar">
            <div class="hp-fill" style="width:{hp_remaining}%"></div>
        </div>
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

# ==============================
# AFTER YES
# ==============================
else:

    legend_name = random.choice(list(legendary_data.keys()))

    st.markdown(f"""
    <div class="title-text" style="color:#1f77b4;">
        {starter} is evolving...
    </div>
    """, unsafe_allow_html=True)

    st.image(starter_info["evolve_img"], width=260)

    st.markdown(f"""
    <div class="subtitle-text">
        Congratulations! It evolved into {starter_info['evolve_name']} 💙
    </div>
    """, unsafe_allow_html=True)

    st.balloons()

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align:center;">
        <img src="{legendary_data[legend_name]}" width="260">
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="subtitle-text">
        Legendary Blessing Activated: {legend_name} ✨
    </div>
    """, unsafe_allow_html=True)

    st.success("You unlocked the rarest item: Lifetime Commitment Badge.")

    if st.button("Reset Game"):
        st.session_state.answered_yes = False
        st.session_state.nay_count = 0
        st.session_state.starter = random.choice(["Pikachu", "Eevee", "Charmander"])
        st.rerun()
