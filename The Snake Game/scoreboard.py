from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 268)
        self.turtle_write()

    def turtle_write(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as f:
                f.write(str(self.score))
        self.score = 0
        self.turtle_write()

    def update(self):
        self.score += 1
        self.turtle_write()
