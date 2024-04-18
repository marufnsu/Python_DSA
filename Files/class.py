class Cookie:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

cookie_one = Cookie("Blue")
cookie_two = Cookie("Red")

print(f"{cookie_one.get_color()} {cookie_two.get_color()}")