from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-200,250)
        self.hideturtle()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.score}",align="center",font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over, Final score {self.score}", align="center", font=FONT)

