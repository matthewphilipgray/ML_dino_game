import tkinter
from dino import dino
from ground import background
from obstacle import obstacle
import time

def game(event, top):
    
    player = dino(canvas, ground)

    counter = 0
    obstacles = []
    
    hit = False
    
    while hit == False:

        if counter % 300 == 0:
            obstacles.append(obstacle(canvas, ground, 5 + 0.01*counter))
        top.update_idletasks()
        top.update()
        player.draw()
        
        if len(obstacles) != 0:
        
            for i in range(len(obstacles)):
                obstacles[i].draw()
                
            hit =  player.collision(obstacles[0])
                        
            if obstacles[0].posX < -obstacles[0].width :
                del obstacles[0]
                
        time.sleep(0.01)

        counter = counter + 1

    canvas.create_text(540,100, text = "You lose", fill = "black", font = "Times 90 bold")

    
top = tkinter.Tk()
top.title = "Game"
top.resizable(0,0)
top.wm_attributes("-topmost", 1)

canvas = tkinter.Canvas(top, width = 1080, height = 920,  bd = 0, bg = "white")
canvas.pack()
top.update_idletasks()
top.update()




ground = background(canvas)

b = tkinter.Button(top, text="press to play", command=game(top))
b.pack()

top.update_idletasks()
top.update()
