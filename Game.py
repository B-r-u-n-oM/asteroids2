import pyxel
from Player import *
from Asteroid import *
from settings import *


class Game:
    def __init__(self):
        self.player = Player()
        self.elapsedtime = 0
        self.width = game["width"]
        self.height = game["height"]
        self.caption = game["caption"]
        self.fps = game["fps"]
        pyxel.init(self.width, self.height, caption=self.caption, fps=self.fps, quit_key=pyxel.KEY_Q)
        pyxel.run(self.update, self.draw)

    def count_execution_time(self):
        game["elapsed_time"] += game["frame"]

    def update(self):
        self.count_execution_time()
        if game["page"] == "home":
            pyxel.cls(pyxel.COLOR_BLACK)
            if pyxel.btn(pyxel.KEY_ENTER): game["page"] = "playing"
            elif pyxel.btn(pyxel.KEY_R):  game["page"] = "records"
        elif game["page"] == "playing":
            pyxel.cls(pyxel.COLOR_BLACK)
            self.player.move(), self.player.teleport(), self.player.shot(), self.player.verify_collision()
            self.player.lives = 0 #JUST FOR TEST -------- remove this after that
            if self.player.lives == 0: game["page"] = "gameover"
            for b in bullet["bullets"]:
                b.move(), b.check_limit()
                self.player.points += b.verify_collision()
            Asteroid()
            for a in asteroid["asteroids"]: a.move(), a.check_limit()
        elif game["page"] == "records":
            pyxel.cls(pyxel.COLOR_BLACK)
            if pyxel.btn(pyxel.KEY_B): game["page"] = "home"
        elif game["page"] == "gameover":
            pyxel.cls(pyxel.COLOR_BLACK)
            self.player.setnickname()
            #if pyxel.btn(pyxel.KEY_S): game["page"] = "home"

    def draw(self):
        if game["page"] == "home":
            pyxel.text(game["width"] / 2 - len("Welcome to the") * 2, game["height"] / 3, "Welcome to the",
                       pyxel.COLOR_WHITE)
            pyxel.text(game["width"] / 2 - len("Asteroids Game!") * 2, game["height"] / 2, "Asteroids Game!",
                       pyxel.COLOR_WHITE)
            pyxel.text(game["width"] / 2 - len("Press Enter to start") * 2, game["height"] / 1.5,
                       "Press Enter to start", pyxel.COLOR_YELLOW)
            pyxel.text(1, game["height"] - 10, "(R) Records", pyxel.COLOR_RED)
            pyxel.text(game["width"] / 2 + 3 * len("(Q) Quit"), game["height"] - 10, "(Q) Quit", pyxel.COLOR_WHITE)
        elif game["page"] == "playing":
            self.player.draw()
            for b in bullet["bullets"]: b.draw()
            for a in asteroid["asteroids"]: a.draw()
        elif game["page"] == "records":
            pyxel.text(game["width"] / 2 - len("Records") * 2, 10, "Records",
                       pyxel.COLOR_RED)
            pyxel.text(1, game["height"] - 10, "(B) Back", pyxel.COLOR_WHITE)

            with open("records.csv") as data:
                records = [line.split(",") for line in data]
            for i in range(len(records)):
                pyxel.text(10, 20 + 10 * i, "%s-" % records[i][0], pyxel.COLOR_YELLOW)
                pyxel.text(16, 20 + 10 * i, records[i][1], pyxel.COLOR_WHITE)
                pyxel.text(game["width"] - 30, 20 + 10 * i, records[i][2], pyxel.COLOR_YELLOW)
        elif game["page"] == "gameover":
            pyxel.text(game["width"] / 2 - len("GAME OVER") * 2, 10, "GAME OVER",
                       pyxel.COLOR_RED)

            pyxel.text(1, game["height"] / 3, "Points: %s" % self.player.points, pyxel.COLOR_WHITE)
            pyxel.text(1, game["height"] / 2, "Insert your nickname: ", pyxel.COLOR_YELLOW)
            pyxel.text(1, game["height"] / 1.5, self.player.nickname, pyxel.COLOR_WHITE)
            pyxel.text(1, game["height"] - 10, "(S) Skip", pyxel.COLOR_WHITE)

