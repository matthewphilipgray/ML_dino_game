class obstacle:
    
    width = 30
    height = 100
   
    
    def __init__(self, canvas, ground, velocity):
        
        self.posX = canvas.winfo_width()
        self.posY = ground.level
        self.velX = -velocity
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(self.posX, self.posY ,
                                self.posX + self.width, self.posY - self.height, fill = "black")
        


    def draw(self):
        
        newPos = self.posX + self.velX
     
        self.canvas.move(self.id, self.velX, 0)
        self.posX = newPos