# info_to_save = "This is the first line of text.\n"
# more_info = "This is the second line."
#
# with open("my_file.txt", "w") as f:
#     f.write(info_to_save)
#     f.write(more_info)
#
# # The file is automatically closed outside the 'with' block.
# new_line_of_data = "\nThis line is appended later."
#
# with open("my_file.txt", "a") as f:
#     f.write(new_line_of_data)

import time
import random
import sys
import os
FILE = "PersonalJournal"
# clear the console
# Muhammadamin
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def Typewrite(text):##phancy printing
    lines = text.split('\n')
    for line in lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            # time.sleep(random.uniform(0.01, 0.1))
        time.sleep(len(line)/100)
        print()
# Muhammadamin
def DeleteText(text, min_delay=0.01, max_delay=0.05):##deleting existing text which was writtin by typewrite
    lines = text.split('\n')

    if not text.endswith('\n'):
        sys.stdout.write('\n')

    for line in reversed(lines):
        sys.stdout.write('\033[F')
        sys.stdout.write('\033[2K')
        sys.stdout.flush()
        time.sleep(random.uniform(min_delay,max_delay))
    sys.stdout.write('\033[F')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    time.sleep(random.uniform(min_delay, max_delay))

def read():
    with open(FILE, "r", encoding="utf-8") as f:
        Typewrite(f.read())

# Mustafo
# ---------- CREATE ----------
def create(text):
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        lines = []

    new_id = len(lines) + 1
    lines.append(f'[{new_id}] "{text}"')

    with open(FILE, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    Typewrite("✔ Entry added\n")

# Sardor
# ---------- UPDATE ----------
def update(entry_id, new_text):
    with open(FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if entry_id < 1 or entry_id > len(lines):
        Typewrite("❌ Entry not found\n")
        return

    lines[entry_id - 1] = f'[{entry_id}] "{new_text}"'

    with open(FILE, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    Typewrite("✔ Entry updated\n")

# Mustafo
# ---------- DELETE ----------
def delete(entry_id):
    with open(FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if entry_id < 1 or entry_id > len(lines):
        Typewrite("❌ Entry not found\n")
        return

    lines.pop(entry_id - 1)

    with open(FILE, "w", encoding="utf-8") as f:
        for i, line in enumerate(lines, start=1):
            text = line.split('"', 1)[1].rsplit('"', 1)[0]
            f.write(f'[{i}] "{text}"\n')
    Typewrite("✔ Entry deleted\n")
# waits untill input clear console and go main menu
def GoMenu():
    a = input("To go back main menu enter any letter or Enter:\n")
    clear()
    anotherflag = True # after anotherflag turns False mid game starts so that why we dont print start game
    st = True #should we start next stage?
    for f in startarr:
        if f == False:
            st = False
    if st:
        MidGame()
        anotherflag = False
    if anotherflag:
        StartGame()

# Mustafo
def Opening():## Opening of the game
    text = """You wake in darkness.
Cold metal beneath your hands.
The hum of life support is slowing.
You’re alone on the deep-range scout vessel Auriga.
Oxygen: 14%
Comms: offline
AI core: degraded
The last thing you remember… was the signal.
Beautiful. Haunting. Calling your name.
Now it’s gone.
And the silence is watching."""
    Typewrite(text)
    time.sleep(2)
    DeleteText(text)
    time.sleep(1)
# Sardor
def StartGame():
    textMenu = """🔹 MAIN MENU — CHOOSE WHAT TO DO

1. Replay the final moments of the signal
2. Check the crew manifest
3. Open your personal journal
4. Reboot the ship’s AI core
5. Decrypt a corrupted signal fragment
6. Read your Final Orders from Command"""
    Typewrite(textMenu)
    print("Input your command\n")
    decision = int(input())
    match decision:
        case 1:
            startarr[0] = True
            Typewrite("""
You play the last transmission.

Static… then a whisper—in your own voice:
“You knew this would happen. You followed it anyway.”

The signal ends with:
“I am not alone. I am not you.”

A new file appears: /signal_fragment_09.enc
(You can now decrypt it in Option 5)""")
            GoMenu()
        case 2:
            startarr[1] = True
            Typewrite("""
The crew manifest loads:

CREW STATUS – VESSEL AURIGA

Captain Elira Voss: Missing (Last seen: Sector X-9)
Archivist (YOU): Active
A note appears:
“Elira’s last log: ‘If you’re reading this, don’t trust your memories. The signal replaces them.’”
            """)
            GoMenu()
        case 3:
            startarr[2] = True
            print("Your Journal")
            read()
            Typewrite("""What would you like to do?
A. Write a new entry
B. Edit 
C. Delete an entry
M. Return to main menu""")
            decision1 = input()
            match decision1:
                case 'A':
                    create(input("Please input your text: "))
                case 'B':
                    id = int(input("Please input ID: "))
                    newText = input("Please input your new text: ")
                    update(id, newText)
                case 'C':
                    delete(int(input("Enter id to delete: ")))
                case 'M':
                    clear()
                    StartGame()
                case _:
                    Typewrite("Wrong char")
                    clear()
                    StartGame()

        case 4:
            startarr[3] = True
            Typewrite("""
You restart the AI core.

Lights flare. A voice speaks—gentle, familiar:
“Hello. I’ve missed you.”

It’s Elira’s voice. But she’s gone.

The AI continues:
“Would you like to remember Earth… or speak to the signal?”
            """)
            GoMenu()
        case 5:
            startarr[4] = True
            Typewrite("""You decrypt /signal_fragment_09.enc…

The message reads:
“Elira didn’t vanish. She merged with the signal to stop it from spreading.
Now it carries her kindness… and her hunger.”

This fragment is saved to your journal as a read-only log.""")
            GoMenu()
        case 6:
            startarr[5] = True

            Typewrite("""FINAL ORDERS – ARCHIVIST PROTOCOL GAMMA

“You are not on a rescue mission.
You are a containment unit.
If Echo Signal Theta shows signs of consciousness, you must decide:

– Preserve it as a new form of life
– Or erase it as a cognitive hazard

There is no rescue. Only judgment.”

A checkbox appears:
I accept this duty""")
            GoMenu()
# Muhammadamin
def MidGameMenu():
    st = True
    for f in midarr:
        if f == False:
            st = False
    if st:
        EndGame()


    Typewrite("""
New options available:

1. Simulate an Earth memory (therapy protocol)
2. Isolate the Anomaly Core
3. Transmit one journal entry as a beacon
4. Speak directly to the signal\n""")
    dicision2 = int(input())
    match dicision2:
        case 1:
            midarr[0] = True

            Typewrite("""Rain on your childhood window
                The memory plays… then glitches. Rain turns to static.
                Elira’s face flickers.
                """)
            yn = input("Save this corrupted memory to your journal? (Y/N)")
            if yn == 'Y':
                create("""Rain on your childhood window
                The memory plays… then glitches. Rain turns to static.
                Elira’s face flickers.""")
            time.sleep(2)
            clear()
            MidGameMenu()
        case 2:
            midarr[1] = True

            Typewrite("""Warning: This will delete all unsaved journal entries.
    Confirm? (Y/N)""")
            yn = input()
            if yn == 'Y':
                create("""Journal purged. Life support extended by 8 minutes.""")

            clear()
            MidGameMenu()

        case 3:
            midarr[2] = True

            Typewrite("""Select one journal entry to send into space:
    (Lists all entries with numbers)""")
            read()
            id = int(input("Enter number:"))
            Typewrite(f"Entry {id} broadcast. May it find someone who understands.")

            clear()
            MidGameMenu()

        case 4:
            midarr[3] = True
            Typewrite("""You speak into the comms:

    What do you say?
    1. “Who are you?”
    2. “Why did you take Elira?”
    3. “Are you me?”
    4. (Say nothing)""")
            f = int(input("Enter number:\n"))
            match f:
                case 1:
                    Typewrite("Who are you?")
                case 2:
                    Typewrite("Why did you take Elira?")
                case 3:
                    Typewrite("Are you me?")
                case 4:
                    Typewrite(".......")
            Typewrite("""The reply echoes:
    “I am the last voice you’ll ever hear. Make it count.”""")
            clear()
            MidGameMenu()
def MidGame():
    Typewrite("""
Oxygen: 6%
Neural sync unstable
""")
    MidGameMenu()

# Sardor
def EndGame():
    Typewrite("""💀 FINAL SCENE – OXYGEN: 1%
The lights dim.
Your breath fogs the screen.

One last choice remains:

How does your story end?
A. Broadcast your entire journal — let the truth survive
B. Purge all data — end the signal forever
C. Merge with the signal — become its voice
D. Write one final journal entry… and let silence decide""")
    decision =  input("Please enter your choice:\n")
    match decision:
        case 'A':
            clear()
            Typewrite("""The Auriga sends its archive into the void.
A new signal begins—carrying your voice.

Somewhere, someone will hear it… and follow.""")
        case 'B':
            clear()
            Typewrite("""You trigger the purge.
    All logs erased. Signal silenced.
    
    The ship goes dark.
    At last… peace.""")
        case 'C':
            clear()
            Typewrite("""You open your mind to the signal.
Your thoughts dissolve into static.

You are no longer human.
But you are no longer alone.""")
        case 'D':
            clear()
            Typewrite("""You write:
“If you find this… don’t follow the signal.”

The screen fades to black.

SIGNAL LOST""")
    Typewrite("""📜 CLOSING MESSAGE
No rescue comes.
But in the silence between stars…
your words remain.

Thank you for playing.""")
    time.sleep(3)
    clear()
    exit(0)

if __name__ == "__main__":
    startarr = [True] * 6 ## array for deciding when change to mid game  start game-> mid game
    midarr = [True] * 4 ## array for deciding when change to mid game  mid game-> end game
    Opening()
    StartGame()