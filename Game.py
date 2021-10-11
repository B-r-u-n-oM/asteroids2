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
        self.isplaying = False
        pyxel.init(self.width, self.height, caption=self.caption, fps=self.fps)
        pyxel.run(self.update, self.draw)

    def count_execution_time(self):
        game["elapsed_time"] += game["frame"]

    def update(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        self.count_execution_time()
        self.state()
        if self.isplaying:
            self.player.move(), self.player.teleport(), self.player.shot(), self.player.verify_collision()
            for b in bullet["bullets"]:
                b.move(), b.check_limit()
                self.player.points += b.verify_collision()
            Asteroid()
            for a in asteroid["asteroids"]: a.move(), a.check_limit()

    def draw(self):
        self.player.draw()
        for b in bullet["bullets"]: b.draw()
        for a in asteroid["asteroids"]: a.draw()

    def state(self):
        if pyxel.btnp(pyxel.KEY_ENTER): self.isplaying = not self.isplaying






