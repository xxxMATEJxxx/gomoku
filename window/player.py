import tkinter
import time
import threading
import numpy as np

FIELD_SIZE = 30

class Player(threading.Thread):
    def __init__(self, player_sign):
        threading.Thread.__init__(self)
        self.start()
        self.sign = player_sign
        self.name = 'window' + str(player_sign)
    def run(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window, bg='black', height=FIELD_SIZE * 15, width=FIELD_SIZE * 15)
        self.canvas.pack()
        self.grid = np.zeros((15,15))
        self.canvas.bind('<Button-1>', self.handle_mouse_click)

        image_x = tkinter.PhotoImage(file='img/image_x.png')
        image_o = tkinter.PhotoImage(file='img/image_o.png')
        for i in range(15):
            self.canvas.create_line(
              FIELD_SIZE * i,
              0,
              FIELD_SIZE * i,
              FIELD_SIZE * 15,
              fill='#333',
            )
            self.canvas.create_line(
              0,
              FIELD_SIZE * i,
              FIELD_SIZE * 15,
              FIELD_SIZE * i,
              fill='#333',
            )
        if self.sign == 1:
            self.opponent_image = image_o
            self.player_image = image_x
        else:
            self.opponent_image = image_x
            self.player_image = image_o
        print(self.opponent_image)
        self.window.mainloop()

    def handle_mouse_click(self, event):
        y = event.y//FIELD_SIZE
        x = event.x//FIELD_SIZE
        if self.grid[y,x] == 0:
          self.last_click = (event.y//FIELD_SIZE, event.x//FIELD_SIZE)

    def play(self, opponent_move):
        
        print(f'opponent played {opponent_move}')
        if (opponent_move != None):
            row, col = opponent_move
            self.grid[row, col] = -self.sign
            self.canvas.create_image(
                    col * FIELD_SIZE,
                    row * FIELD_SIZE,
                    image = self.opponent_image,
                    anchor='nw'
            )
        self.last_click = None
        while(self.last_click == None):
            time.sleep(0.016)
        row, col = self.last_click
        print(f'you played      {row, col}')
        self.grid[row, col] = -self.sign
        self.canvas.create_image(
                col * FIELD_SIZE,
                row * FIELD_SIZE,
                image = self.player_image,
                anchor='nw',
        )
        return (row, col)
