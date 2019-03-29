class background:
    
    def __init__(self, canvas):
        self.level = canvas.winfo_height() - 10
        self.canvas = canvas
        self.id = self.canvas.create_line(0, self.level, canvas.winfo_width(), self.level)
