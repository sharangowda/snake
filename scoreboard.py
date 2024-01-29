from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 260)
        self.score = 0
        with open('Capstones\snake-game\highscore.txt') as data:
            self.highscore = int(data.read())
        self.write(f'Score: {self.score} ', True,
                   align='center', font=("arial", 22, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 260)
        self.write(f'Score: {self.score} ', True,
                   align='center', font=("arial", 22, "normal"))

    def game_over(self):
        self.goto(0, 0)
        if self.score > self.highscore:
            self.highscore = self.score
            with open('Capstones\snake-game\highscore.txt', 'w') as score:
                score.write(str(self.score))
        self.write(f'Game Over. Your highscore is {self.highscore}', True, align='center', font=(
            "arial", 22, "normal"))
