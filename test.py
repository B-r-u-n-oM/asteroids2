import pyxel
from math import radians, sqrt, cos, sin

COS_30 = sqrt(3) / 2


class Triangulo:
    def __init__(self, x, y, angle, size):
        self.x = x  # Coordenadas do centro do triângulo
        self.y = y
        self.angle = angle  # angulo em radianos
        self.size = size
        self.rot_speed = ...
        self.vx = ...
        self.vy = ...

    def update(self):
        ...

    def radius(self):
        return self.size / 2

    def collide_circle(self, x, y, r):
        """
        Retorna verdadeiro se colide com o círculo de centro em x, y e raio r.
        """
        dist = sqrt((x - self.x)**2 + (y - self.y)**2)
        return dist < r + self.radius()

    def rotate(self, angle):
        """
        Roda o triângulo pelo ângulo dado em radianos
        """
        self.angle += angle

    def draw(self, color=pyxel.COLOR_WHITE):
        """
        Desenha o triângulo com a cor "color" especificada.
        """
        (x1, y1), (x2, y2), (x3, y3) = self.vertices()
        pyxel.tri(x1, y1, x2, y2, x3, y3, color)

    def drawb(self, color=pyxel.COLOR_WHITE):
        """
        Desenha a borda do triângulo com a cor "color" especificada.
        """
        (x1, y1), (x2, y2), (x3, y3) = self.vertices()
        pyxel.trib(x1, y1, x2, y2, x3, y3, color)

    def vertices(self):
        """
        Retorna uma lista com os três vértices do triângulo.
        """
        base = self.size / 2
        dist = base / COS_30

        angle = self.angle
        x = self.x
        y = self.y

        x1 = x + dist * cos(angle)
        y1 = y + dist * sin(angle)

        x2 = x + dist * cos(angle + radians(120))
        y2 = y + dist * sin(angle + radians(120))

        x3 = x + dist * cos(angle + radians(240))
        y3 = y + dist * sin(angle + radians(240))

        return [(x1, y1), (x2, y2), (x3, y3)]


def update():
    tri.rotate(radians(1))


def draw():
    pyxel.cls(pyxel.COLOR_BLACK)
    tri.drawb()


pyxel.init(120, 80)

tri = Triangulo(60, 40, 0, 20)

pyxel.run(update, draw)