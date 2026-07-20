import tkinter as tk
from tkinter import messagebox
import random
from tkinter import font as tkfont  # <--- FIX: import font module

# ============================================================
# 1. Word List
# ============================================================
WORDS = [
    "apple", "house", "river", "music", "smile",
    "happy", "water", "cloud", "bread", "light",
    "dream", "heart", "star", "moon", "sun",
    "forest", "ocean", "mountain", "garden", "rainbow"
]

# ============================================================
# 2. Hangman ASCII Art (6 stages)
# ============================================================
HANGMAN_STAGES = [
    """
       ------
       |    |
            |
            |
            |
            |
    ==========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    ==========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    ==========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    ==========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    ==========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    ==========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    ==========
    """
]

# ============================================================
# 3. Colors
# ============================================================
COLORS = {
    'bg': '#1a1a2e',
    'bg_secondary': '#16213e',
    'bg_input': '#0f3460',
    'fg': '#e0e0e0',
    'accent': '#00e5a0',
    'danger': '#ff6b6b',
    'success': '#00e5a0',
    'heart_on': '#ff4757',
    'heart_off': '#2d3436',
    'word_bg': '#0a0a1a',
}

# ============================================================
# 4. Main Application
# ============================================================
class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Hangman Game")
        self.root.geometry("700x750")
        self.root.configure(bg=COLORS['bg'])
        self.root.resizable(False, False)

        self.word = ""
        self.guessed_letters = []
        self.attempts = 6
        self.game_over = False
        self.score = 0
        self.message = ""
        self.message_type = ""

        # Check if Orbitron font is available; if not, use Arial
        available_fonts = tkfont.families()
        self.title_font = ('Orbitron', 28, 'bold') if 'Orbitron' in available_fonts else ('Arial', 28, 'bold')
        self.word_font = ('Orbitron', 28, 'bold') if 'Orbitron' in available_fonts else ('Arial', 28, 'bold')
        self.stats_font = ('Orbitron', 14, 'bold') if 'Orbitron' in available_fonts else ('Arial', 14, 'bold')
        self.entry_font = ('Orbitron', 20, 'bold') if 'Orbitron' in available_fonts else ('Arial', 20, 'bold')

        # UI widgets
        self.hangman_label = None
        self.word_label = None
        self.attempts_label = None
        self.hearts_label = None
        self.guessed_label = None
        self.message_label = None
        self.score_label = None
        self.entry = None

        self.init_game()
        self.create_widgets()
        self.root.bind('<Return>', self.check_guess)

    def init_game(self):
        self.word = random.choice(WORDS)
        self.guessed_letters = []
        self.attempts = 6
        self.game_over = False
        self.message = ""
        self.message_type = ""

    def check_guess(self, event=None):
        if self.game_over:
            self.show_message("Game already over! Click 'New Game'", "info")
            self.update_ui()
            return

        guess = self.entry.get().strip().lower()
        self.entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            self.show_message("⚠️ Please enter a single letter (a-z)", "error")
            self.update_ui()
            return

        if guess in self.guessed_letters:
            self.show_message(f"⏳ '{guess.upper()}' already guessed!", "error")
            self.update_ui()
            return

        self.guessed_letters.append(guess)

        if guess in self.word:
            self.show_message(f"✅ '{guess.upper()}' is in the word!", "success")
            if all(letter in self.guessed_letters for letter in self.word):
                self.game_over = True
                self.score += 1
                self.show_message(f"🏆 YOU WIN! Word: {self.word.upper()}", "success")
        else:
            self.attempts -= 1
            self.show_message(f"❌ '{guess.upper()}' is NOT in the word!", "error")
            if self.attempts == 0:
                self.game_over = True
                self.show_message(f"💀 GAME OVER! Word: {self.word.upper()}", "error")

        self.update_ui()

    def show_message(self, msg, msg_type):
        self.message = msg
        self.message_type = msg_type

    def restart_game(self):
        self.init_game()
        self.entry.config(state='normal')
        self.entry.focus_set()
        self.score_label.config(text=str(self.score))
        self.message_label.config(text="")
        self.update_ui()

    def update_ui(self):
        stage = 6 - self.attempts
        if stage > 6:
            stage = 6
        self.hangman_label.config(text=HANGMAN_STAGES[stage])

        display = " ".join([l.upper() if l in self.guessed_letters else "_" for l in self.word])
        self.word_label.config(text=display)

        self.attempts_label.config(text=f"{self.attempts} / 6")

        hearts = " ".join(["❤️" if i < self.attempts else "🖤" for i in range(6)])
        self.hearts_label.config(text=hearts)

        if self.guessed_letters:
            text = "🔤 " + ", ".join(sorted([l.upper() for l in self.guessed_letters]))
            self.guessed_label.config(text=text, fg=COLORS['accent'])
        else:
            self.guessed_label.config(text="🔤 None guessed yet", fg=COLORS['fg'])

        if self.message:
            color = COLORS['success'] if self.message_type == "success" else (
                COLORS['danger'] if self.message_type == "error" else COLORS['fg']
            )
            self.message_label.config(text=self.message, fg=color)

        if self.game_over or self.attempts == 0:
            self.entry.config(state='disabled')
        else:
            self.entry.config(state='normal')
            self.entry.focus_set()

    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg=COLORS['bg'])
        main_frame.pack(expand=True, fill='both', padx=30, pady=20)

        # Title
        tk.Label(
            main_frame,
            text="🎯 HANGMAN",
            font=self.title_font,
            bg=COLORS['bg'],
            fg=COLORS['accent']
        ).pack(pady=(0, 5))

        tk.Label(
            main_frame,
            text="Guess the word before you run out of lives",
            font=('Arial', 10, 'italic'),
            bg=COLORS['bg'],
            fg='#888'
        ).pack(pady=(0, 20))

        # Card Frame
        card_frame = tk.Frame(
            main_frame,
            bg=COLORS['bg_secondary'],
            relief='flat',
            bd=0,
            highlightthickness=0
        )
        card_frame.pack(expand=True, fill='both', pady=5)

        # Top row: Hangman + Word
        top_frame = tk.Frame(card_frame, bg=COLORS['bg_secondary'])
        top_frame.pack(expand=True, fill='both', padx=15, pady=15)

        left_frame = tk.Frame(top_frame, bg=COLORS['bg_secondary'])
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))

        self.hangman_label = tk.Label(
            left_frame,
            text=HANGMAN_STAGES[0],
            font=('Courier New', 12),
            bg=COLORS['bg_secondary'],
            fg=COLORS['accent'],
            justify='left'
        )
        self.hangman_label.pack(pady=10)

        right_frame = tk.Frame(top_frame, bg=COLORS['bg_secondary'])
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))

        word_bg = tk.Frame(
            right_frame,
            bg=COLORS['word_bg'],
            relief='flat',
            bd=2,
            highlightthickness=0
        )
        word_bg.pack(expand=True, fill='both', pady=10)

        self.word_label = tk.Label(
            word_bg,
            text="_ _ _ _ _",
            font=self.word_font,
            bg=COLORS['word_bg'],
            fg='#ffffff'
        )
        self.word_label.pack(expand=True, padx=20, pady=20)

        # Stats Row
        stats_frame = tk.Frame(card_frame, bg=COLORS['bg_secondary'])
        stats_frame.pack(fill='x', padx=15, pady=(0, 10))

        tk.Label(
            stats_frame,
            text="🏆 Score:",
            font=('Arial', 12, 'bold'),
            bg=COLORS['bg_secondary'],
            fg=COLORS['fg']
        ).pack(side='left', padx=(0, 5))

        self.score_label = tk.Label(
            stats_frame,
            text="0",
            font=self.stats_font,
            bg=COLORS['bg_secondary'],
            fg=COLORS['accent']
        )
        self.score_label.pack(side='left', padx=(0, 30))

        tk.Label(
            stats_frame,
            text="❤️ Attempts:",
            font=('Arial', 12, 'bold'),
            bg=COLORS['bg_secondary'],
            fg=COLORS['fg']
        ).pack(side='left', padx=(0, 5))

        self.attempts_label = tk.Label(
            stats_frame,
            text="6 / 6",
            font=self.stats_font,
            bg=COLORS['bg_secondary'],
            fg=COLORS['accent']
        )
        self.attempts_label.pack(side='left', padx=(0, 20))

        self.hearts_label = tk.Label(
            stats_frame,
            text="❤️ ❤️ ❤️ ❤️ ❤️ ❤️",
            font=('Arial', 18),
            bg=COLORS['bg_secondary']
        )
        self.hearts_label.pack(side='right')

        # Guessed Letters
        guessed_frame = tk.Frame(card_frame, bg=COLORS['bg_secondary'])
        guessed_frame.pack(fill='x', padx=15, pady=(0, 10))

        self.guessed_label = tk.Label(
            guessed_frame,
            text="🔤 None guessed yet",
            font=('Arial', 11),
            bg=COLORS['bg_secondary'],
            fg=COLORS['fg']
        )
        self.guessed_label.pack()

        # Input Section
        input_frame = tk.Frame(card_frame, bg=COLORS['bg_secondary'])
        input_frame.pack(fill='x', padx=15, pady=(0, 15))

        entry_bg = tk.Frame(
            input_frame,
            bg=COLORS['bg_input'],
            relief='flat',
            bd=2,
            highlightthickness=0
        )
        entry_bg.pack(side='left', expand=True, fill='x', padx=(0, 10))

        self.entry = tk.Entry(
            entry_bg,
            font=self.entry_font,
            bg=COLORS['bg_input'],
            fg=COLORS['fg'],
            insertbackground=COLORS['accent'],
            border=0,
            highlightthickness=0,
            justify='center',
            width=4
        )
        self.entry.pack(pady=8, padx=10)
        self.entry.focus_set()

        guess_btn = tk.Button(
            input_frame,
            text="🚀 Guess",
            font=('Arial', 12, 'bold'),
            bg=COLORS['accent'],
            fg=COLORS['bg'],
            relief='flat',
            padx=20,
            pady=10,
            cursor='hand2',
            command=self.check_guess
        )
        guess_btn.pack(side='right')

        # Message Label
        self.message_label = tk.Label(
            card_frame,
            text="",
            font=('Arial', 12, 'bold'),
            bg=COLORS['bg_secondary'],
            fg=COLORS['fg'],
            wraplength=600,
            justify='center'
        )
        self.message_label.pack(pady=(0, 15))

        # New Game Button
        new_game_btn = tk.Button(
            card_frame,
            text="🔄 New Game",
            font=('Arial', 12, 'bold'),
            bg=COLORS['bg'],
            fg=COLORS['accent'],
            relief='flat',
            bd=2,
            highlightthickness=0,
            padx=30,
            pady=10,
            cursor='hand2',
            command=self.restart_game
        )
        new_game_btn.pack(pady=(0, 20))

        # Footer
        tk.Label(
            main_frame,
            text="Built with ❤️ using Tkinter • CodeAlpha Internship",
            font=('Arial', 8),
            bg=COLORS['bg'],
            fg='#555'
        ).pack(pady=(10, 0))

        self.update_ui()

# ============================================================
# 5. Run
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGame(root)
    root.mainloop()
