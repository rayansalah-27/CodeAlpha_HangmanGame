# 🎯 Hangman Game

A simple, text-based Hangman game built with Python. The player guesses letters to reveal a hidden word, with only **6 incorrect attempts** allowed. This project demonstrates fundamental Python concepts including loops, conditionals, functions, and the `random` module.

---

## ✨ Features

- 🎲 **Random word selection** from a predefined list of common words.
- 🖥️ **Clear, user-friendly console interface**.
- ✅ **Input validation** – only single alphabetic characters are accepted.
- 🚫 **Duplicate guess prevention** – you cannot guess the same letter twice.
- 🔄 **Replay option** – play as many rounds as you like.
- 📊 **Displays guessed letters and remaining attempts** at each turn.

---

## 📝 Word List

The game currently uses the following **5 common English words**:

- 🍎 `apple`
- 🏠 `house`
- 🌊 `river`
- 🎵 `music`
- 😊 `smile`

> 💡 **Tip:** You can easily customize this list by editing the `WORD_LIST` variable inside `hangman.py`.

---

## 🚀 How to Run

1. **Ensure you have Python 3** installed. Check by running:
   ```bash
   python --version
