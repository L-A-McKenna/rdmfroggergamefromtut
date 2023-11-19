import turtle

# title screen
wn = turtle.Screen()
wn.title("Froger by @lukemc")
wn.setup(600, 800)
wn.bgcolor("black")

# register shape
wn.register_shape("frog.gif")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# classes
class Sprite():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
    
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()

class Player(Sprite):
    def __init__(Self, x, y, width, height, image):
        Sprite.__init__(Self, x, y, width, height, image)

    def up(self):
        self.y += 45
        
# objects
player = Player(0, -300, 40, 40, "frog.gif")
player.render(pen)

# keyboard bind
wn.listen()
wn.onkeypress(player.up, "Up")

while True:
    player.render(pen)
