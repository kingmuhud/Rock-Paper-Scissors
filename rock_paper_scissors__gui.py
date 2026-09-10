"""
Rock, Paper, Scissors — GUI version
Run: python rock_paper_scissors_gui.py
"""

import random
import tkinter as tk
from tkinter import font as tkfont


CHOICES = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors",
}

EMOJI = {
    "r": "🪨",
    "p": "📄",
    "s": "✂️",
}


def is_win(player: str, opponent: str) -> bool:
    """Return True if player beats opponent."""
    return (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    )


class RPSApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Rock · Paper · Scissors")
        self.root.geometry("420x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1a2e")

        self.user_score = 0
        self.computer_score = 0
        self.ties = 0

        self.title_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
        self.label_font = tkfont.Font(family="Helvetica", size=13)
        self.result_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
        self.button_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
        self.score_font = tkfont.Font(family="Helvetica", size=12)

        self._build_ui()

    def _build_ui(self) -> None:
        # Title
        tk.Label(
            self.root,
            text="Rock · Paper · Scissors",
            font=self.title_font,
            fg="#eaeaea",
            bg="#1a1a2e",
        ).pack(pady=(24, 8))

        # Scoreboard
        score_frame = tk.Frame(self.root, bg="#16213e", padx=16, pady=10)
        score_frame.pack(fill="x", padx=24, pady=8)

        self.score_label = tk.Label(
            score_frame,
            text=self._score_text(),
            font=self.score_font,
            fg="#a0aec0",
            bg="#16213e",
        )
        self.score_label.pack()

        # Status / result area
        self.status_label = tk.Label(
            self.root,
            text="Pick your move",
            font=self.label_font,
            fg="#cbd5e0",
            bg="#1a1a2e",
        )
        self.status_label.pack(pady=(20, 6))

        self.battle_label = tk.Label(
            self.root,
            text="",
            font=self.result_font,
            fg="#ffffff",
            bg="#1a1a2e",
        )
        self.battle_label.pack(pady=4)

        self.result_label = tk.Label(
            self.root,
            text="",
            font=self.result_font,
            fg="#48bb78",
            bg="#1a1a2e",
        )
        self.result_label.pack(pady=(4, 16))

        # Choice buttons
        btn_frame = tk.Frame(self.root, bg="#1a1a2e")
        btn_frame.pack(pady=12)

        colors = {"r": "#e53e3e", "p": "#3182ce", "s": "#38a169"}
        for key, name in CHOICES.items():
            b = tk.Button(
                btn_frame,
                text=f"{EMOJI[key]}\n{name}",
                font=self.button_font,
                width=8,
                height=3,
                bg=colors[key],
                fg="white",
                activebackground=colors[key],
                activeforeground="white",
                relief="flat",
                cursor="hand2",
                command=lambda k=key: self.play(k),
            )
            b.pack(side="left", padx=8)

        # Reset
        tk.Button(
            self.root,
            text="Reset scores",
            font=self.score_font,
            bg="#2d3748",
            fg="#e2e8f0",
            activebackground="#4a5568",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.reset_scores,
        ).pack(pady=(28, 8))

        tk.Label(
            self.root,
            text="Click Rock, Paper, or Scissors to play",
            font=("Helvetica", 10),
            fg="#718096",
            bg="#1a1a2e",
        ).pack(pady=(4, 12))

    def _score_text(self) -> str:
        return (
            f"You  {self.user_score}   ·   "
            f"Ties  {self.ties}   ·   "
            f"Computer  {self.computer_score}"
        )

    def play(self, user: str) -> None:
        computer = random.choice(["r", "p", "s"])

        self.battle_label.config(
            text=f"You {EMOJI[user]}   vs   {EMOJI[computer]} Computer"
        )

        if user == computer:
            self.ties += 1
            self.result_label.config(text="It's a tie!", fg="#ecc94b")
        elif is_win(user, computer):
            self.user_score += 1
            self.result_label.config(text="You won!", fg="#48bb78")
        else:
            self.computer_score += 1
            self.result_label.config(text="You lost!", fg="#fc8181")

        self.status_label.config(
            text=f"You chose {CHOICES[user]} · Computer chose {CHOICES[computer]}"
        )
        self.score_label.config(text=self._score_text())

    def reset_scores(self) -> None:
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        self.score_label.config(text=self._score_text())
        self.status_label.config(text="Pick your move")
        self.battle_label.config(text="")
        self.result_label.config(text="")


def main() -> None:
    root = tk.Tk()
    RPSApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
