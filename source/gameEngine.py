import numpy as np


class gameState():
    def __init__(self) -> None:
        self.board = np.array([["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                                ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                                ["--", "--", "--", "--", "--", "--", "--", "--"],
                                ["--", "--", "--", "--", "--", "--", "--", "--"],
                                ["--", "--", "--", "--", "--", "--", "--", "--"],
                                ["--", "--", "--", "--", "--", "--", "--", "--"],
                                ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                                ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
                                ])

        self.whiteTurn = True
        self.moveLog = []

        