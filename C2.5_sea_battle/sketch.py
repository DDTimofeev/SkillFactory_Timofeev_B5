class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self,other):\
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f"Dot({self.x},{self.y})"
class Ship:
    def __init__(self,bow,l,o):
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l
    def dots(self):
        ship_dots = []
        for i in range (self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x+=1

            if self.o == 1:
                cur_y+=1

            ship_dots.append(Dot(cur_x, cur_y))
        return ship_dots

s = Ship(Dot(1,2),4,0)
print(s.dots())


