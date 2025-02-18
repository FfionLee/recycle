import pygame
import random

pygame.init()
screen=pygame.display.set_mode((1200,900))

r1=pygame.transform.scale(pygame.image.load('assets/paperbag.png'),(50,50))
r2=pygame.transform.scale(pygame.image.load('assets/pencil.png'),(50,50))
r3=pygame.transform.scale(pygame.image.load('assets/woodenbox.png'),(50,50))

r=[r1,r2,r3]

background=pygame.image.load('assets/background.png')

playing=True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.transform.scale(pygame.image.load('assets/bin.png'),(75,100))
        self.rect=self.image.get_rect()


class Recycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=random.choice(r)
        self.rect=self.image.get_rect()

class NoRecycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.transform.scale(pygame.image.load('assets/plasticbag.png'),(50,50))
        self.rect=self.image.get_rect()

NoRecycleGroup=pygame.sprite.Group()
for i in range(20):
    nonrecycle=NoRecycle()
    nonrecycle.rect.x=random.randint(50,1100)
    nonrecycle.rect.y=random.randint(50,850)
    NoRecycleGroup.add(nonrecycle)

RecycleGroup=pygame.sprite.Group()
for i in range(30):
    recycle=Recycle()
    recycle.rect.x=random.randint(50,1100)
    recycle.rect.y=random.randint(50,850)
    RecycleGroup.add(recycle)

BinGroup=pygame.sprite.Group()
bin=Player()
BinGroup.add(bin)

while playing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
    screen.blit(background,(0,0))
    BinGroup.draw(screen)
    RecycleGroup.draw(screen)
    NoRecycleGroup.draw(screen)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if bin.rect.y>0:
            bin.rect.y-=5
    if keys[pygame.K_DOWN]:
        if bin.rect.y<900:
            bin.rect.y+=5
    if keys[pygame.K_LEFT]:
        if bin.rect.x>0:
            bin.rect.x-=5
    if keys[pygame.K_RIGHT]:
        if bin.rect.x<1200:
            bin.rect.x+=5
    
    itemcollide=pygame.sprite.spritecollide(bin,RecycleGroup,True)
    print(itemcollide)
    pygame.display.update()