# 🐍 Snake, Water, Gun Game

A simple **Snake, Water, Gun** game built using Python. The computer randomly chooses between snake, water, and gun, while the player enters their choice.

## 🎮 How the Game Works

The choices are represented by numbers:

| Number | Choice   |
| -----: | -------- |
|    `1` | 🐍 Snake |
|   `-1` | 💧 Water |
|    `0` | 🔫 Gun   |

### Winning Rules

* 🐍 Snake beats 💧 Water
* 💧 Water beats 🔫 Gun
* 🔫 Gun beats 🐍 Snake
* Same choice → Draw

## 🛠️ Technologies Used

* **Python**
* `random` module

## 🚀 How to Run

1. Make sure Python is installed.
2. Clone the repository:

```bash
git clone <your-repository-url>
```

3. Open the project folder:

```bash
cd <project-folder>
```

4. Run the program:

```bash
python main.py
```

## 💻 Example

```text
Enter your choice (1 for snake, -1 for water, 0 for gun): 1
Computer chose: water
You Win!
```

## 📚 What I Learned

This project helped me practice:

* `if`, `elif`, and `else`
* Nested conditional statements
* User input with `input()`
* Type conversion using `int()`
* The `random` module
* Python conditional expressions
* Basic game logic

## 🔮 Future Improvements

* Add input validation
* Add multiple rounds
* Keep track of the score
* Add a replay option
* Create a graphical interface


Built as a beginner Python project while learning programming fundamentals.
