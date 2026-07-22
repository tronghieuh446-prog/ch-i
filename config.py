# ==========================================
# Alex Dev Hacker Terminal
# config.py
# ==========================================

# -------- General --------

APP_NAME = "Alex Dev Hacker"

APP_VERSION = "1.0"

AUTHOR = "Alex"

# -------- Prompt --------

PROMPT_NAME = "Alex"

PROMPT_SUFFIX = "Dark"

PROMPT_SYMBOL = ">"

# -------- Window --------

WINDOW_TITLE = "Alex Dev Hacker"

WINDOW_WIDTH = 120

WINDOW_HEIGHT = 35

# -------- Colors --------

BLACK = "\033[30m"

RED = "\033[91m"

GREEN = "\033[92m"

YELLOW = "\033[93m"

BLUE = "\033[94m"

MAGENTA = "\033[95m"

CYAN = "\033[96m"

WHITE = "\033[97m"

RESET = "\033[0m"

BOLD = "\033[1m"

# -------- Prompt Color --------

PROMPT = (
    RED
    + PROMPT_NAME
    + GREEN
    + PROMPT_SUFFIX
    + YELLOW
    + PROMPT_SYMBOL
    + " "
    + RESET
)

# -------- Banner --------

BANNER = rf"""{RED}{BOLD}

 █████╗ ██╗     ███████╗██╗  ██╗
██╔══██╗██║     ██╔════╝╚██╗██╔╝
███████║██║     █████╗   ╚███╔╝
██╔══██║██║     ██╔══╝   ██╔██╗
██║  ██║███████╗███████╗██╔╝ ██╗
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝

          Alex Dev Hacker

{RESET}
"""

# -------- Loading --------

LOADING_TEXT = "Loading"

LOADING_SPEED = 0.30

# -------- Dashboard --------

LINE = "=" * 70

SHOW_CPU = True

SHOW_RAM = True

SHOW_DISK = True

SHOW_TIME = True

SHOW_USER = True

SHOW_WINDOWS = True

SHOW_PYTHON = True

# -------- Matrix --------

ENABLE_MATRIX = False

MATRIX_SPEED = 0.03

# -------- Logger --------

SAVE_HISTORY = True

HISTORY_FILE = "history.log"

# -------- Theme --------

THEME_NAME = "Black Neon"

BACKGROUND = "BLACK"

ACCENT = "GREEN"

# -------- Future --------

ENABLE_SOUND = False

ENABLE_SPLASH = True

ENABLE_ANIMATION = True
