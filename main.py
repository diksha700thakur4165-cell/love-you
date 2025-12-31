import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="My Love's New Year Gift ❤️", page_icon="💖", layout="wide")

# --- Custom CSS for background music (hidden player) ---
st.markdown("""
    <style>
    iframe {
        display: none; /* Hide the YouTube iframe player */
    }
    .stButton>button {
        background-color: #FF69B4; /* Pink button */
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-size: 18px;
        cursor: pointer;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #FFC0CB; /* Lighter pink on hover */
        color: #333;
    }
    .st-emotion-cache-h4xjle { /* Target Streamlit's main content padding */
        padding-top: 2rem;
    }
    </style>
    <iframe width="0" height="0" src="https://www.youtube.com/embed/H5v3kku4y6Q?autoplay=1&mute=0&controls=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    """, unsafe_allow_html=True)

# --- Session State Initialization ---
if 'page' not in st.session_state:
    st.session_state.page = 'envelope_back'
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

# --- Functions for Audio Playback (for kiss sound) ---
def play_audio(audio_url):
    st.components.v1.html(
        f"""
        <audio autoplay="true">
            <source src="{audio_url}" type="audio/mp3">
        </audio>
        """,
        height=0,
        width=0,
    )

# --- PAGE LOGIC ---

# 1. Big Real Envelope Back with Teddy and Heart
if st.session_state.page == 'envelope_back':
    st.image("https://i.imgur.com/kS5x84O.png", width=700) # Placeholder for a realistic envelope back
    st.image("https://i.imgur.com/Yw1qWqT.gif", width=200) # Placeholder: Teddy holding a pink heart
    st.markdown("## Please accept this gift, Ishri Pishri! ❤️")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Yes, I accept!"):
            st.session_state.page = 'gift_boxes'
            st.rerun()
    with col2:
        if st.button("No, I don't want it."):
            st.session_state.page = 'angry_teddy'
            st.session_state.attempts += 1
            st.rerun()

# 2. Angry Teddy if "No" is clicked
elif st.session_state.page == 'angry_teddy':
    st.image("https://i.imgur.com/P1l1j.gif", width=250) # Placeholder: Angry teddy GIF
    st.markdown("## Hey! Why did you click No?! 😠")
    st.write(f"You've tried to refuse {st.session_state.attempts} time(s)! Don't make me angrier!")
    if st.button("Try Again (I'll say Yes this time!)"):
        st.session_state.page = 'envelope_back'
        st.rerun()

# 3. Gift Boxes Selection
elif st.session_state.page == 'gift_boxes':
    st.markdown("## Gift For You! 🎁")
    st.markdown("### Click any gift to open! (Choose wisely 😉)")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://i.imgur.com/8Q9S8Xj.png", width=200) # Gift Box 1
        if st.button("Open Gift 1", key="gift1"):
            st.session_state.page = 'gift1_content'
            st.rerun()
    with col2:
        st.image("https://i.imgur.com/8Q9S8Xj.png", width=200) # Gift Box 2
        if st.button("Open Gift 2", key="gift2"):
            st.session_state.page = 'gift2_content'
            st.rerun()
    with col3:
        st.image("https://i.imgur.com/8Q9S8Xj.png", width=200) # Gift Box 3
        if st.button("Open Gift 3", key="gift3"):
            st.session_state.page = 'gift3_content'
            st.rerun()

# --- CONTENT FOR GIFT 1 ---
elif st.session_state.page == 'gift1_content':
    placeholder = st.empty()
    st.balloons()
    for i in range(3, 0, -1):
        placeholder.title(f"Opening in... {i}")
        time.sleep(1)
    placeholder.empty()

    st.title("🎊 HAPPY NEW YEAR, MY LOVE! 🎊")
    st.image("https://i.imgur.com/2s4gYqG.gif", width=300) # Realistic Rose Bouquet GIF

    st.markdown("""
        ### My dearest,
        As another year unfolds, my heart only grows fonder for you. Every moment spent with you is a treasure, a beautiful chapter in our story. You fill my life with joy, laughter, and an unparalleled love. May this New Year bring us closer, stronger, and fill our days with even more magical memories. You are my everything, and I cherish you more than words can express.
        """)
    if st.button("Back to Gifts"):
        st.session_state.page = 'gift_boxes'
        st.rerun()

# --- CONTENT FOR GIFT 2 ---
elif st.session_state.page == 'gift2_content':
    st.image("https://i.imgur.com/uX8p0p7.png", width=600) # Placeholder: Certificate for World's Best BF
    st.markdown("""
        ### This certifies that:
        # ❤️ The Best Boyfriend In The World ❤️
        ## Has been awarded to YOU for your endless love, support, and for making every day brighter!
        ### Issued on: January 1st, 2024
        ### By: Your Loving Girlfriend, Ishri Pishri
        """)
    if st.button("Back to Gifts"):
        st.session_state.page = 'gift_boxes'
        st.rerun()

# --- CONTENT FOR GIFT 3 (Donkey Video) ---
elif st.session_state.page == 'gift3_content':
    st.video("https://www.youtube.com/watch?v=kYc5tL8F01o") # Placeholder: Donkey video (e.g., a cute funny one)
    st.markdown("## Hahaha! Yahi ho tum, Gadhe! 😂")
    if st.button("Okay, Okay... Aage Badho!"):
        st.session_state.page = 'realistic_kiss'
        st.rerun()

# --- REALISTIC KISS ---
elif st.session_state.page == 'realistic_kiss':
    st.image("https://i.imgur.com/CgX9H91.gif", width=400) # Placeholder: Realistic kiss GIF
    st.markdown("## Mwah! 😘")
    if st.button("Click for a Special Message"):
        play_audio("https://www.myinstants.com/media/sounds/mwah.mp3") # Play Mwah sound
        st.session_state.page = 'lovely_para'
        st.rerun()

# --- LOVELY PARA ---
elif st.session_state.page == 'lovely_para':
    st.markdown("""
        ### My one and only,
        Every kiss with you feels like magic, a promise of forever. You're not just my boyfriend; you're my best friend, my confidant, and the love of my life. This New Year, and every year after, I want to be by your side, creating countless beautiful memories. Thank you for being you.
        # I Love You So Much, Ishri Pishri ❤️
        """)
    if st.button("Start Over"):
        st.session_state.page = 'envelope_back'
        st.session_state.attempts = 0
        st.rerun()
