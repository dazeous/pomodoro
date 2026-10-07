# Pomodoro Timer

A simple desktop Pomodoro timer built with Python and Tkinter. Displays a tomato with a
built-in countdown, Start/Reset controls, and checkmarks that track completed work sessions.

## Features

- 25-minute work sessions with 5-minute short breaks
- 20-minute long break after every 4 completed work sessions
- Checkmarks show completed work sessions for the current cycle (capped at four)
- Reset cancels the running countdown, clears the timer, and restores the initial state
- Start is disabled while a session is running, so countdowns never overlap
- Launches correctly from any working directory

## Requirements

- Python 3.x with Tkinter
  - Windows/macOS official installers: included
  - Debian/Ubuntu: `sudo apt install python3-tk`
- `tomato.png` (included in this repository)

## Getting started

```bash
git clone https://github.com/dazeous/pomodoro.git
cd <your-repo>
python main.py
```

## How it works

| Rep | Session     | Duration |
| --- | ----------- | -------- |
| 1   | Work        | 25 min   |
| 2   | Short break | 5 min    |
| 3   | Work        | 25 min   |
| 4   | Short break | 5 min    |
| 5   | Work        | 25 min   |
| 6   | Short break | 5 min    |
| 7   | Work        | 25 min   |
| 8   | Long break  | 20 min   |

After the long break the cycle repeats from rep 1.

### Controls

- **Start** begins the next session. Sessions chain automatically when a countdown
  reaches zero, so the timer runs until you press Reset.
- **Reset** stops the current countdown, returns the display to `00:00`, clears the
  checkmarks, and re-enables Start.

## Customization

Edit the constants at the top of `main.py`:

```python
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
```

Colors (`PINK`, `RED`, `GREEN`, `BLUE`, `YELLOW`) and fonts can be adjusted there as well.

## Project structure

```
.
├── main.py      # Timer logic and Tkinter UI
└── tomato.png   # Image shown behind the countdown
```
