


# 🎯 Hangman Game

A beautifully designed, desktop-based Hangman game built with **Python** and **Tkinter**. Test your vocabulary skills in this classic word-guessing game with a modern dark theme, ASCII art, and interactive gameplay.

---

## 📌 Features

- 🎲 **Random word selection** – chooses from 20 common English words.
- 🖼️ **ASCII art hangman** – updates with each wrong guess (6 stages).
- ❤️ **Visual hearts system** – hearts turn dark as you lose attempts.
- 🏆 **Score tracking** – keeps your wins across multiple rounds.
- 🎨 **Dark theme UI** – modern design with neon teal accents.
- ⌨️ **Enter key support** – press Enter to submit your guess.
- ✅ **Input validation** – only single alphabetic characters accepted.
- 🚫 **Duplicate guess prevention** – can't guess the same letter twice.
- 🔄 **Replay option** – start a new game anytime.

---

## 📝 Word List

The game currently uses the following **20 common English words**:

```
apple, house, river, music, smile, happy, water, cloud, bread, light,
dream, heart, star, moon, sun, forest, ocean, mountain, garden, rainbow
```

> 💡 You can easily customize this list by editing the `WORDS` variable inside the code.

---

## 🚀 How to Run

### Prerequisites
- Python 3.7 or higher installed on your system.
- **Tkinter** is included with Python by default – no additional installation needed.

### Steps

1. **Clone or download** this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/CodeAlpha_HangmanGame.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd CodeAlpha_HangmanGame
   ```

3. **Run the game**:
   ```bash
   python app.py
   ```

> **Note:** If you named your file `hangman.py`, use:
> ```bash
> python hangman.py
> ```

4. The game window will open – start guessing letters!

---

## 🎮 Gameplay Example

```
+---------------------------------------------------+
|  🎯 HANGMAN                                       |
|  Guess the word before you run out of lives       |
|  +---------------------------------------------+  |
|  |  [Hangman Art]   [ _ _ _ _ _ ]              |  |
|  |  (e.g., O       )                          |  |
|  |  ( /|\  )                                  |  |
|  |  ( / \  )                                  |  |
|  +---------------------------------------------+  |
|  🏆 Score: 2    ❤️ Attempts: 4 / 6    ❤️❤️❤️❤️🖤🖤 |
|  🔤 A, P, R                                     |
|  [   Guess: [  ]   ]  [ 🚀 Guess ]            |
|  ✅ 'A' is in the word!                        |
|  [ 🔄 New Game ]                              |
+---------------------------------------------------+
```

---

## 📁 Project Structure

```
CodeAlpha_HangmanGame/
├── app.py              # Main application file (Tkinter)
├── README.md           # This file
└── requirements.txt    # Dependencies (empty for Tkinter)
```

---

## 🧠 Key Concepts Demonstrated

| Concept | Description |
| :--- | :--- |
| 🐍 **Python** | Core programming language |
| 🖥️ **Tkinter** | GUI framework for desktop applications |
| 🎨 **Custom UI** | Dark theme with custom colors and styling |
| 🔄 **Game Logic** | Random word selection, guess checking, win/loss conditions |
| 💾 **State Management** | Tracking game state (attempts, guessed letters, score) |
| ⌨️ **Event Handling** | Enter key binding and button clicks |
| ✅ **Input Validation** | Ensuring correct user input |

---

## 🔮 Future Improvements (Optional Ideas)

- Add **difficulty levels** (easy/medium/hard) with different word lengths.
- Add **sound effects** for correct/wrong guesses.
- Add **multiplayer mode** where players take turns.
- Add **hint system** using emoji clues.
- Save **high scores** to a file.

---

## 👤 Author

**Your Name**  
🔗 https://github.com/rayansalah-27
🔗 https://www.linkedin.com/in/rayan-salah-013043375

