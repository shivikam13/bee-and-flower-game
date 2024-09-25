import pgzrun,random 

WIDTH=600
HEIGHT=500
TITLE="BEE GAME"
bee=Actor('bee',(0,0))
bee.pos=150,150
flower=Actor("flower")
flower.pos=250,250
score=0

def place_flower():
   flower.x=random.randint(70,WIDTH-70)
   flower.y=random.randint(70,WIDTH-70)









def draw():
   screen.blit('background',(0,0))
   bee.draw()
   flower.draw()
   screen.draw.text("score :"+str(score),color="pink",topleft=(10,10))
def update():
   global score      
   if keyboard.left:
      bee.x=bee.x-2
   if keyboard.right:
      bee.x=bee.x+2
   if keyboard.up:
      bee.y=bee.y-2
   if keyboard.down:
      bee.y=bee.y+2
   if bee.colliderect(flower):
      score=score+10 
      place_flower()                                                   

pgzrun.go()

