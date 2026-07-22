# ===========================================
# Alex Dev Hacker Theme
# ===========================================

import os
import time
from datetime import datetime

# ANSI Colors
BLACK="\033[30m"
RED="\033[91m"
GREEN="\033[92m"
YELLOW="\033[93m"
BLUE="\033[94m"
MAGENTA="\033[95m"
CYAN="\033[96m"
WHITE="\033[97m"

RESET="\033[0m"
BOLD="\033[1m"

TITLE="Alex Dev Hacker"

PROMPT = (
    RED + "Alex"
    + GREEN + "Dark"
    + YELLOW + "> "
    + RESET
)

BANNER=f"""{RED}{BOLD}

 █████╗ ██╗     ███████╗██╗  ██╗
██╔══██╗██║     ██╔════╝╚██╗██╔╝
███████║██║     █████╗   ╚███╔╝
██╔══██║██║     ██╔══╝   ██╔██╗
██║  ██║███████╗███████╗██╔╝ ██╗
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝

            Alex Dev Hacker

{RESET}
"""

def set_title():
    os.system(f"title {TITLE}")

def clear():
    os.system("cls")

def loading():

    txt="Loading"

    for i in range(4):

        print(
            CYAN+
            txt+
            "."*i+
            RESET,
            end="\r"
        )

        time.sleep(0.3)

def draw():

    clear()

    print(BANNER)

    print(
        GREEN+
        "="*65+
        RESET
    )

    print(
        CYAN+
        " Terminal Theme Loaded"+
        RESET
    )

    print(
        YELLOW+
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")+
        RESET
    )

    print(
        GREEN+
        "="*65+
        RESET
    )
