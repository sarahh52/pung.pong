from pygame import * 

# Создаем фон игры
back = (200,255,255)
win_width=600
win_height=500
window = display.set_mode((win_width,win_height))
window.fill(back)

#Создаем логические флажки и часы для фпс
game = True 
finish=False 
clock = time.Clock()
FPS =60 

#Игровой цикл 
while game: 
    for e in event.get():
        if e.type==QUIT:
            game = False 
    display.update()
    clock.tick(FPS)






