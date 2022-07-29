from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("data.txt") as files:
            self.high_score = int(files.read())

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.current_score}  High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.update()

    def reset_score(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as files:
                files.write(str(self.current_score))
        self.current_score = 0
        self.update()
