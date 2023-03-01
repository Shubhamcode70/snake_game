from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Current Score {self.score}", move=False, align="center", font=("Times New Roman", 18, "bold"))

    def score_update(self):
        self.clear()
        self.score = self.score + 5
        self.write(f"Current Score {self.score}", move=False, align="center", font=("Times New Roman", 18, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"FINAL SCORE {self.score}", move=False, align="center", font=("Times New Roman", 18, "bold"))
        self.goto(0, -20)
        self.write("GAME OVER", move=False, align="center", font=("Times New Roman", 18, "bold"))