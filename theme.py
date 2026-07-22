# ==========================================
# Alex Dev Hacker Terminal
# theme.py
# ==========================================

import os
import time
from datetime import datetime

from config import *

# ==========================================
# WINDOW
# ==========================================

def set_title():
    os.system(f"title {WINDOW_TITLE}")


# ==========================================
# CLEAR
# ==========================================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ==========================================
# LOADING
# ==========================================

def loading():

    clear()

    for i in range(4):

        print(
            CYAN +
            LOADING_TEXT +
            "." * i +
            RESET,
            end="\r"
        )

        time.sleep(LOADING_SPEED)

    clear()


# ==========================================
# HEADER
# ==========================================

def header():

    print(BANNER)

    print(GREEN + LINE + RESET)

    print(
        CYAN +
        f" App     : {APP_NAME}" +
        RESET
    )

    print(
        CYAN +
        f" Version : {APP_VERSION}" +
        RESET
    )

    print(
        CYAN +
        f" Author  : {AUTHOR}" +
        RESET
    )

    print(
        YELLOW +
        datetime.now().strftime("%Y-%m-%d %H:%M:%S") +
        RESET
    )

    print(GREEN + LINE + RESET)


# ==========================================
# DRAW
# ==========================================

def draw():

    clear()

    header()
