import streamlit as st
import random

# ==============================
# PAGE CONFIG (WIDE MODE)
# ==============================
st.set_page_config(
    page_title="A Question For You",
    page_icon="💙",
    layout="wide"
)

# ==============================
# SESSION STATE
# ==============================
if "answered_yes" not in st.session_state:
    st.session_state.answered_yes = False

if "nay_count" not in st.session_state:
    st.session_state.nay_count = 0


# ==============================
# GLOBAL STYLE – ELEGANT WIDE
# ==============================
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #f8fbff 0%, #eaf2fb 100%);
}

/* Center wrapper inside wide layout */
.center-wrapper {
    max-width: 900px;
    margin: 0 auto;
}

/* Glass card */
.main-card {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(14px);
    border-radius: 28px;
    padding: 80px 60px;
    box-shadow: 0 25px 60px rgba(0,0,0,0.08);
    border: 1px solid rgba(255,255,255,0.6);
    text-align: center;
    margin-top: 80px;
}

/* Typography */
.title-text {
    font-size: 40px;
    font-weight: 600;
    color: #1f2d3d;
    margin-bottom: 12px;
}

.subtitle-text {
    font-size: 19px;
    color: #6b7a90;
    margin-bottom: 50px;
}

/* Button base */
div[data-testid="stButton"] button {
    transition: all 0.25s ease-in-out;
    border-radius: 18px !important;
    font-weight: 600;
    letter-spacing: 0.5px;
}

/* Image center */
.image-center {
    display: flex;
    justify-content: center;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)


# ==============================
# VALENTINE GATE
# ==============================
if not st.session_state.answered_yes:

    scale = 1.25 ** st.session_state.nay_count
    yay_font = 22 + (st.session_state.nay_count * 10)
    yay_padding = 16 + (st.session_state.nay_count * 6)
    nay_font = max(16 - (st.session_state.nay_count * 2), 1)
    nay_opacity = max(1 - (st.session_state.nay_count * 0.15), 0.05)

    st.markdown(f"""
    <style>
        div[data-testid="stButton"] button[kind="primary"] {{
            font-size: {yay_font}px !important;
            padding: {yay_padding}px {yay_padding*2}px !important;
            transform: scale({scale});
            background-color: #1f77b4 !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 14px 35px rgba(31,119,180,0.35);
        }}

        div[data-testid="stButton"] button[kind="primary"]:hover {{
            transform: scale({scale + 0.05});
            box-shadow: 0 20px 45px rgba(31,119,180,0.45);
        }}

        .nay-btn-style button {{
            font-size: {nay_font}px !important;
            opacity: {nay_opacity};
            background-color: transparent !important;
            color: #6b7a90 !important;
            border: 1px solid #d0d7e2 !important;
        }}

        .nay-btn-style button:hover {{
            background-color: #f1f4f9 !important;
        }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="center-wrapper">
        <div class="main-card">
            <div class="title-text">A Question For You</div>
            <div class="subtitle-text">
                Would you like to be my Valentine?
            </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        if st.button(f"YES{'!' * st.session_state.nay_count}", type="primary"):
            st.session_state.answered_yes = True
            st.rerun()

    with col2:
        for _ in range(random.randint(0, 8)):
            st.write("")

        inner_cols = st.columns([1,1,1])
        with inner_cols[random.randint(0,2)]:
            st.markdown('<div class="nay-btn-style">', unsafe_allow_html=True)
            if st.button("No"):
                st.session_state.nay_count += 1
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)


# ==============================
# AFTER YES
# ==============================
else:

    st.markdown("""
    <div class="center-wrapper">
        <div class="main-card">
            <div class="title-text" style="color:#1f77b4;">
                Successfully Accepted 💙
            </div>
            <div class="subtitle-text">
                You are now permanently allocated in my life portfolio.
            </div>
    """, unsafe_allow_html=True)

    st.balloons()

    st.markdown("""
        <div style="
            margin-top:40px;
            padding:35px;
            border-radius:22px;
            background: white;
            border: 1px solid #e1e8f2;
            box-shadow: 0 12px 35px rgba(0,0,0,0.06);
        ">
            <h3 style="color:#1f77b4;">Elite Partner Profile - Keff Chan</h3>
            <p><b>Status:</b> Long-Term Commitment</p>
            <p><b>Ability:</b> Elite Affection + Horny :p</p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Open Your Gift 🎁"):
        st.success("You just unlocked the rarest item: My Heart.")

        try:
            with open("me and keff.jpeg", "rb") as f:
                import base64
                img_bytes = f.read()
                encoded = base64.b64encode(img_bytes).decode()

            st.markdown(f"""
            <div style="
                display:flex;
                justify-content:center;
                align-items:center;
                margin-top:40px;
            ">
                <img src="data:image/jpeg;base64,{encoded}"
                    style="
                        width:600px;
                        border-radius:20px;
                        box-shadow:0 20px 50px rgba(0,0,0,0.15);
                    ">
            </div>
            """, unsafe_allow_html=True)

        except:
            st.warning("Image not found.")


    st.markdown("</div></div>", unsafe_allow_html=True)
