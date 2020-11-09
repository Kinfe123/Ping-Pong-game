import pygame
pygame.init()
pygame.mixer.init()
width = 750
height = 500
win = pygame.display.set_mode((width , height))
pygame.display.set_caption("KINFISH PONG GAME!")
black = (0 , 0 , 0)
white = (255 , 255 , 255)
icon_img = pygame.image.load('pongicon3.png')
pygame.display.set_icon(icon_img)
pygame.mixer.music.load("bgmusic.wav")
pygame.mixer.music.play(-1)

#Paddle -> 


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10 , 75])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.score = 0

class Pong(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10 , 10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.speed = 10
        self.x_change = 1
        self.y_change = 1
        
        
paddle1 = Paddle()
paddle1.rect.x = 25 # 0 , 25 
paddle1.rect.y = height / 2 - 25
paddle2 = Paddle()
paddle2.rect.x = width - 25 # width - 25
paddle2.rect.y = height / 2 - 25

paddle_speed = 10
pong = Pong()
pong.rect.x = width / 2 - 10
pong.rect.y = height / 2 - 10

sprites = pygame.sprite.Group()
sprites.add(paddle1 , paddle2 , pong)
def draw():
    win.fill(black)
    font = pygame.font.Font("Bristone.ttf" , 25)
    text = font.render("PONG GAME" , True  , (white))
    text_rect = text.get_rect()
    text_rect.center = (width // 2  , 25 )
    #Player1 
    player_font = pygame.font.Font("Bristone.ttf" , 15)
    player_score = player_font.render("Score A: " + str(paddle1.score)  , True , (white))
    player_rect = player_score.get_rect()
    player_rect.center = (75 , 50)
    win.blit(player_score , player_rect)
    #Player2
    player2_font = pygame.font.Font("Bristone.ttf" , 15)
    player2_score = player2_font.render("Score B: " + str(paddle2.score)  , True , (white))
    player2_rect = player2_score.get_rect()
    player2_rect.center = (width - 75 , 50)
    win.blit(player2_score , player2_rect)
    
    win.blit(text , text_rect)
    sprites.draw(win)
    pygame.display.update()
    

def soundForCollision():
    play = pygame.mixer.Sound("pongs.wav")
    play.play()
isTrue = True 
while isTrue:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            isTrue = False
            
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddle1.rect.y -= paddle_speed
    if key[pygame.K_s]:
        paddle1.rect.y += paddle_speed
    if key[pygame.K_UP]:
        paddle2.rect.y -= paddle_speed
    if key[pygame.K_DOWN]:
        paddle2.rect.y += paddle_speed
        
    pong.rect.x += pong.speed * pong.x_change 
    pong.rect.y += pong.speed * pong.y_change
    if pong.rect.y >= 490:
        pong.y_change = -1
    if pong.rect.x >= 740:
        pong.rect.x , pong.rect.y = width / 2 , height / 2
        paddle1.score +=1
        pong.x_change = -1
        
    if pong.rect.y < 0:
        pong.y_change = 1
    if pong.rect.x < 10:
        pong.rect.x , pong.rect.y = width / 2 , height / 2
        paddle2.score+=1
        pong.x_change = 1
        
    if paddle1.rect.colliderect(pong.rect):
        soundForCollision()
        pong.x_change = 1
        
    if paddle2.rect.colliderect(pong.rect):
        soundForCollision()
        pong.x_change = -1
        
        
        
    
            
    draw()
    
        
            
 
            
            
pygame.quit()
