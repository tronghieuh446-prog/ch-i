import subprocess
import datetime
from theme import PROMPT

history = []


def execute(command: str):

    if not command.strip():
        return

    history.append(command)

    if command.lower() == "clear":
        subprocess.run("cls", shell=True)
        return

    if command.lower() == "history":

        print("\nHistory\n")

        for index, item in enumerate(history, 1):
            print(f"{index}. {item}")

        return

    if command.lower() == "help":

        print("""
Commands

help
history
clear
exit

Other commands are executed by Windows.
""")

        return

    subprocess.run(command, shell=True)


def terminal():

    while True:

        now = datetime.datetime.now().strftime("%H:%M:%S")

        try:

            command = input(PROMPT)

            if command.lower() in ["exit", "quit"]:
                print("Goodbye.")
                break

            execute(command)

        except KeyboardInterrupt:
            print()
