import streamlit as st
import random

# ==========================================
# 1. Liiska Kelmadaha (10 kelmadood)
# ==========================================
WORD_LIST = ["apple", "house", "river", "music", "smile", 
             "happy", "water", "cloud", "bread", "light"]

# ==========================================
# 2. CSS Qaabayn (Styling)
# ==========================================
st.markdown("""
<style>
    /* Guud ahaan bogga */
    .stApp {
        background-color: #0e1117;
        color: #f0f0f0;
    }
    
    /* Ciwaanka weyn */
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #00ffcc;
        text-align: center;
        text-shadow: 0 0 20px #00ffcc, 0 0 40px #00ffcc;
        margin-bottom: 10px;
    }
    
    /* Kelmadda qarsoon */
    .word-display {
        font-size: 3.5rem;
        font-weight: bold;
        letter-spacing: 15px;
        text-align: center;
        color: #ffffff;
        background: #1e2433;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #00ffcc;
        box-shadow: 0 0 30px rgba(0, 255, 204, 0.3);
        margin: 20px 0;
    }
    
    /* Fariimaha saxda ah */
    .success {
        color: #00ffcc;
        font-weight: bold;
    }
    
    /* Fariimaha qaladka */
    .error {
        color: #ff6b6b;
        font-weight: bold;
    }
    
    /* Xarfaha la isku dayay */
    .used-letters {
        font-size: 1.2rem;
        color: #ffd93d;
        background: #1e2433;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #ffd93d;
    }
    
    /* Badhanka */
    .stButton > button {
        background-color: #00ffcc;
        color: #0e1117;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #00cca3;
        transform: scale(1.05);
        box-shadow: 0 0 20px #00ffcc;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #161b22;
    }
    
    /* Qoraalka guud */
    .stTextInput > div > div > input {
        background-color: #1e2433;
        color: white;
        border: 2px solid #00ffcc;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. Hawlaha Ciyaarta (Game Functions)
# ==========================================
def init_game():
    """Bilow ciyaar cusub"""
    st.session_state['word'] = random.choice(WORD_LIST)
    st.session_state['guessed'] = []
    st.session_state['attempts'] = 6
    st.session_state['game_over'] = False
    st.session_state['message'] = ""
    st.session_state['message_type'] = "info"

def check_guess(guess):
    """Hubi xarafka la soo geliyey"""
    if st.session_state['game_over']:
        return
    
    # Hubi inuu yahay hal xaraf
    if len(guess) != 1 or not guess.isalpha():
        st.session_state['message'] = "✗ Fadlan soo geli hal xaraf oo keliya (a-z)"
        st.session_state['message_type'] = "error"
        return
    
    guess = guess.lower()
    word = st.session_state['word']
    
    # Haddii xarafka horay loo isku dayay
    if guess in st.session_state['guessed']:
        st.session_state['message'] = f"✗ Xarafka '{guess}' horay ayaad u isku dayday"
        st.session_state['message_type'] = "error"
        return
    
    # Ku dar liiska la isku dayay
    st.session_state['guessed'].append(guess)
    
    # Hubi saxnaanta
    if guess in word:
        st.session_state['message'] = f"✓ Sax! '{guess}' waa ku jiraa kelmadda"
        st.session_state['message_type'] = "success"
        
        # Hubi haddii kelmaddu dhamaystiran tahay
        if all(letter in st.session_state['guessed'] for letter in word):
            st.session_state['game_over'] = True
            st.session_state['score'] = st.session_state.get('score', 0) + 1
            st.session_state['message'] = f"🎉 WAA GUUL! Kelmaddii waxay ahayd: {word.upper()}"
            st.session_state['message_type'] = "success"
    else:
        st.session_state['attempts'] -= 1
        st.session_state['message'] = f"✗ Qalad! '{guess}' kuma jiro kelmadda"
        st.session_state['message_type'] = "error"
        
        # Hubi haddii fursaduhu dhammaadeen
        if st.session_state['attempts'] == 0:
            st.session_state['game_over'] = True
            st.session_state['message'] = f"💀 WAA GUULDARRO! Kelmaddii waxay ahayd: {word.upper()}"
            st.session_state['message_type'] = "error"

# ==========================================
# 4. UI-ga Ciyaarta (User Interface)
# ==========================================
def main():
    # Ciwaanka
    st.markdown('<p class="main-header">🎯 HANGMAN GAME</p>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Sidebar - Xogta ciyaarta
    with st.sidebar:
        st.markdown("## 📊 Xogta Ciyaarta")
        
        # Dhibcaha (score)
        if 'score' not in st.session_state:
            st.session_state['score'] = 0
        st.metric("🏆 Dhibcaha", st.session_state['score'])
        
        # Fursadaha hadhsan
        if 'attempts' in st.session_state:
            st.metric("❤️ Fursadaha", st.session_state['attempts'])
        
        # Xarfaha la isku dayay
        st.markdown("### 🔤 Xarfaha la isku dayay")
        if 'guessed' in st.session_state and st.session_state['guessed']:
            used = sorted(st.session_state['guessed'])
            st.markdown(f'<div class="used-letters">{", ".join(used)}</div>', unsafe_allow_html=True)
        else:
            st.markdown("*Waxba lama isku dayin*")
        
        st.markdown("---")
        
        # Badhanka bilow cusub
        if st.button("🔄 Ciyaar Cusub"):
            init_game()
            st.rerun()
    
    # Bilow ciyaar haddii aysan jirin
    if 'word' not in st.session_state:
        init_game()
    
    # Muuji kelmadda qarsoon
    word = st.session_state['word']
    guessed = st.session_state['guessed']
    
    # Diyaari qaabka kelmadda
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter.upper() + " "
        else:
            display += "_ "
    
    st.markdown(f'<div class="word-display">{display}</div>', unsafe_allow_html=True)
    
    # Fariimaha (message)
    if 'message' in st.session_state and st.session_state['message']:
        if st.session_state['message_type'] == "success":
            st.markdown(f'<p class="success">{st.session_state["message"]}</p>', unsafe_allow_html=True)
        elif st.session_state['message_type'] == "error":
            st.markdown(f'<p class="error">{st.session_state["message"]}</p>', unsafe_allow_html=True)
        else:
            st.info(st.session_state['message'])
    
    # Soo geli xaraf (input) - haddii ciyaartu dhammaan
    if not st.session_state.get('game_over', False):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            guess = st.text_input("## Soo geli xaraf:", max_chars=1, key="guess_input", 
                                  placeholder="a-z", label_visibility="collapsed")
            if guess:
                check_guess(guess)
                st.rerun()
    else:
        st.markdown("### 🏁 Ciyaartu waa dhammaatay. Riix 'Ciyaar Cusub' si aad mar kale u ciyaarto.")
    
    # Kala saar qaybaha
    st.markdown("---")
    
    # Soo bandhig kelmadda saxda ah haddii ciyaartu dhammaatay oo guuldarro ah
    if st.session_state.get('game_over', False) and st.session_state.get('attempts', 0) == 0:
        st.markdown(f"### Kelmaddii saxda ahayd: **{word.upper()}**")

if __name__ == "__main__":
    main()
