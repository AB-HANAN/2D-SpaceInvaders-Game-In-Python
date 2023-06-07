# SpaceInvaders-py
Game Ha!!!

"""
Documentation

This code is an implementation of a simple 2D space shooter game called "Nebulla Wars" using the Pygame library in Python. The game involves controlling a spaceship and shooting down enemy ships while avoiding collisions with them. 
Here's a breakdown of the code and its functionality:
Imports:

The code imports necessary modules and initializes the Pygame library.
Window Setup:

The code sets up the game window with a specific width and height using the pygame.display.set_mode() function.
It also sets the window caption and icon using the pygame.display.set_caption() and pygame.display.set_icon() functions.
Loading Images:

The code loads various images used in the game using the pygame.image.load() function and stores them in variables.
Rescaling Images:

The code rescales the loaded images using the pygame.transform.scale() function to the desired sizes.
Classes:

The code defines several classes for different game objects:
Laser: Represents a laser fired by the player or enemy ships.
Ship: An abstract class representing a ship with common attributes and methods.
Player: Inherits from the Ship class and represents the player-controlled spaceship.
Enemy: Inherits from the Ship class and represents the enemy spaceships.
Asteroid: Represents asteroids in the game.
PowerUp: Represents power-ups in the game.
Collision Detection:

The code defines a collide function that checks for collisions between two objects based on their masks.
Main Game Loop:

The code defines the main game loop, where the game logic and rendering occur.
It initializes variables for the game state, such as the player's lives, score, and level.
Inside the game loop, the code handles events, updates the game state, and redraws the window.
Redrawing the Window:

The redraw_window function is responsible for rendering the game objects, text labels, and updating the display.
Game Logic:

The game logic includes checking for collisions, moving objects, shooting lasers, and spawning enemies, power-ups, and asteroids based on the current level.

"""

import pygame
import os
import time
import random
pygame.font.init()

#Window (Display)
WIDTH,HEIGHT = 700,750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Nebulla Wars")
ICON = pygame.image.load(os.path.join("Images","icon.png"))
pygame.display.set_icon(ICON)



#Loading all the Images used in the Game
#Player 
SPACESHIP = pygame.image.load(os.path.join("Images","spaceship.png"))
#Enemy player
ALIEN1 = pygame.image.load(os.path.join("Images","alien1.png"))
ALIEN2 = pygame.image.load(os.path.join("Images","alien2.png"))
ALIEN3 = pygame.image.load(os.path.join("Images","alien4.png"))
#Asteriods
largeA = pygame.image.load(os.path.join("Images","largeA.png"))
smallA = pygame.image.load(os.path.join("Images","smallA.png"))
whiteA = pygame.image.load(os.path.join("Images","whiteA.png"))
METEORITE = pygame.image.load(os.path.join("Images","meteorite.png"))
#PowerUp
POWERUP = pygame.image.load(os.path.join("Images","powerUp.png"))
POWERUP2 = pygame.image.load(os.path.join("Images","powerUp2.png"))
#Bullet
BULLET = pygame.image.load(os.path.join("Images","bullet.png"))
BULLET2 = pygame.image.load(os.path.join("Images","bullet2.png"))
BALL = pygame.image.load(os.path.join("Images","ballblack.png"))
#BackGround
BG = pygame.transform.scale(pygame.image.load(os.path.join("Images","background.png")),(WIDTH,HEIGHT))#BG Seting to the Games Height and Width



#Rescaling Images
SPACESHIP= pygame.transform.scale(SPACESHIP,(50,50))
ALIEN1 = pygame.transform.scale(ALIEN1,(100,100))
ALIEN2 = pygame.transform.scale(ALIEN2,(50,50))
ALIEN3 = pygame.transform.scale(ALIEN3,(50,50))
BULLET = pygame.transform.scale(BULLET,(50,50))
BULLET2 = pygame.transform.scale(BULLET2,(50,50))
POWERUP = pygame.transform.scale(POWERUP,(50,50))
POWERUP2 = pygame.transform.scale(POWERUP2,(50,50))

#Classes(Making Objects)
class Laser:
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img,(self.x,self.y))

    def move(self,vel):
        self.y += vel

    def off_screen(self,height):  
        return not (self.y<= height and self.y >=0)

    def collision(self,obj):  
        return collide(self,obj)    

class Ship: #Abstract Class (The content of this Class will be Inherited)
    COOLDOWN =30
    def __init__(self,x,y,health=100):
        self.x = x
        self.y = y
        self.health = health 
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_count = 0

    def move_lasers(self,vel,obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 5
                self.lasers.remove(laser)  

    def draw(self,window):
        window.blit(self.ship_img,(self.x,self.y))
        for laser in self.lasers:
            laser.draw(window)

    def cooldown(self):
        if self.cool_down_count >= self.COOLDOWN:
            self.cool_down_count = 0
        elif self.cool_down_count >0:
            self.cool_down_count +=1    

    def shoot(self):
        if self.cool_down_count == 0:
            laser = Laser(self.x,self.y,self.laser_img)
            self.lasers.append(laser)
            self.cool_down_count = 1

    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self,x,y,score,health=100):
        super().__init__(x,y,health)
        self.ship_img = SPACESHIP
        self.laser_img = BULLET
        #Mask Will Help us to do Picture Perfect Collision on to the Image Loaded on the screen
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.score = score

    def move_lasers(self,vel,objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.score += 10
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self,window):
        super().draw(window)
        self.healthBar(window)
    def healthBar(self,window):
        # BAR_LENGTH = 100
        # BAR_HEIGHT = 10
        # health_bar_x = WIDTH - BAR_LENGTH - 10
        # health_bar_y = 10

        # if self.health <= 0:
        #     self.health = 0

        # fill_width = (self.health / 100) * BAR_LENGTH
        # outline_rect = pygame.Rect(health_bar_x, health_bar_y, BAR_LENGTH, BAR_HEIGHT)
        # fill_rect = pygame.Rect(health_bar_x, health_bar_y, fill_width, BAR_HEIGHT)

        # pygame.draw.rect(WIN, (255, 0, 0), fill_rect)
        # pygame.draw.rect(WIN, (255, 255, 255), outline_rect, 2)
        pygame.draw.rect(window,(255,0,0),(self.x,self.y+self.ship_img.get_height()+ 10,self.ship_img.get_width(),10))
        pygame.draw.rect(window,(0,255,0),(self.x,self.y+self.ship_img.get_height()+ 10,self.ship_img.get_width()*((self.max_health-self.health)/self.max_health),10))
                         
class Enemy(Ship):
    Number_Map = {
        "1": (ALIEN1, BULLET2),
        "2": (ALIEN2, BULLET2),
        "3": (ALIEN3, BULLET2)
    }
    
    def __init__(self, x, y, num, choice, width, height, health=100): 
        super().__init__(x, y, health)
        self.choice = choice
        self.width = width
        self.height = height
        self.ship_img, self.laser_img = self.Number_Map[str(num)]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.shoot_offset = 0 if num == 1 else self.width // 2  # Offset for alien1

    def move(self, vel, player):
        self.y += vel
        self.move_lasers(vel, player)

    def shoot(self):
        if self.cool_down_count == 0:
            if self.ship_img == ALIEN1:
                laser_x = self.x+22 + self.shoot_offset  # Adjust the laser x-coordinate for alien1
            else:
                laser_x = self.x-50 + self.width  # Center the laser for other aliens

            laser = Laser(laser_x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_count = 1

class Asteroid:
    Number_Map = {
        "1": (whiteA),
        "2": (METEORITE)
    }
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.astroimg = self.Number_Map[str(num)]
        self.astro_number = str(num)
        self.mask = pygame.mask.from_surface(self.astroimg)
    def draw(self,screen):
        screen.blit(self.astroimg,(self.x,self.y))

class PowerUp:
    Number_Map = {
        "1": (POWERUP),
        "2": (POWERUP2)
    }
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.powerimg = self.Number_Map[str(num)]
        self.power_number = str(num)
        self.mask = pygame.mask.from_surface(self.powerimg)
    def draw(self,screen):
        screen.blit(self.powerimg,(self.x,self.y))

def collide(obj1,obj2): # The collision between any two
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask,(offset_x,offset_y)) != None


#Main
def main():
    run = True
    FPS = 60
    
    #Score and Level
    level = 0
    lives = 5
    playerVelcity = 5
    score = 0
    lost_count = 0
    lost = False
    laser_vel = 5
    powerups = []
    asteroids = []
    asteroidspawn = 0
    powerspawn = 0
    wave_lenghtP = 3
    wave_lenghtA = 3

    main_font = pygame.font.SysFont("comicsans",20)#Fontsize of the Written Text
    Lost_font = pygame.font.SysFont("Helvetica",60)

    enemies = []
    wave_length = 5
    enemy_velocity = 1
    hi_score = 0
    player = Player(320,695,score)

    clock = pygame.time.Clock()
    def redraw_window(): 
        WIN.blit(BG, (0,0))#Top Left Cornor

        for enemy in enemies:
            enemy.draw(WIN)
        for powerup in powerups:
            powerup.draw(WIN) 
        for asteroid in asteroids:
            asteroid.draw(WIN)       
        #The Reason why the enemy is Drawn before the Player is because we want the enemy 
        #to be drawn on top of the player which means when ever the Enemy Ship will pass the players ships
        #they will automatically go behind the players image, making our player image visible at all times 
        player.draw(WIN)
         #Draw Text
        lives_label = main_font.render(f"Lives: {lives}", 1 ,(255,255,255))
        level_label = main_font.render(f"Level: {level}", 1 ,(255,255,255))
        score_label = main_font.render(f"Score: {player.score}", 1 ,(255,255,255))
        WIN.blit(lives_label,(WIDTH - level_label.get_width()-20,10))
        WIN.blit(level_label,(WIDTH - level_label.get_width()-315,10))
        WIN.blit(score_label,(WIDTH - level_label.get_width()-620,10))

        if lost:
            Lost_label = Lost_font.render("Game Over",1,(255,255,255))
            WIN.blit(Lost_label,(WIDTH/2 - Lost_label.get_width()/2 , 350))


        pygame.display.update()#Refreshs your game

    #Game Loop
    while run:
        clock.tick(FPS)
        redraw_window()
        if lives <= 0 or player.health<=0:
            lost = True
            lost_count +=1
        if lost:
            if lost_count > FPS * 5:
                run = False
                if player.score > hi_score:
                    hi_score = player.score
                    main_menu(hi_score)
            else:
                continue    
    
        if len(enemies) == 0:
            level +=1 #Adding Levels
            wave_length +=5 #Frequency at which the Enemy will Spawn after each level
       
            # for i in range(wave_length):
            #     # Generate new enemy
            #     #In this secenario I myself have taken one single Size of all the enemies
            #     enemy_width = 50  # Adjust this value based on your enemy's actual width
            #     enemy_height = 100  # Adjust this value based on your enemy's actual height
            #     enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), i % 3 + 1, random.choice(["1", "2", "3"]), enemy_width, enemy_height)
                
            #     # Check for overlap with existing enemies
            #     overlapping = False
            #     for existing_enemy in enemies:
            #         if pygame.Rect(enemy.x, enemy.y, enemy_width, enemy_height).colliderect(pygame.Rect(existing_enemy.x, existing_enemy.y, existing_enemy.width, existing_enemy.height)):
            #             overlapping = True
            #             break

            #     # If there's an overlap, generate a new enemy until there's no overlap
            #     while overlapping:
            #         enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), i % 3 + 1, random.choice(["1", "2", "3"]), enemy_width, enemy_height)
            #         overlapping = False
            #         for existing_enemy in enemies:
            #             if pygame.Rect(enemy.x, enemy.y, enemy_width, enemy_height).colliderect(pygame.Rect(existing_enemy.x, existing_enemy.y, existing_enemy.width, existing_enemy.height)):
            #                 overlapping = True
            #                 break

            #     enemies.append(enemy)
            for i in range(wave_length):
                enemy_width = 50  # Adjust this value based on your enemy's actual width
                enemy_height = 100  # Adjust this value based on your enemy's actual height
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), i % 3 + 1, random.choice(["1", "2", "3"]), enemy_width, enemy_height)
                enemies.append(enemy)
                
                if len(powerups) == 0 and powerspawn < 3 and level > 0:
                    wave_lenghtP += 5
                    for _ in range(min(wave_lenghtP,3-powerspawn)):
                        power = PowerUp(random.randrange(50,WIDTH-50),random.randrange(-1500,-100),random.choice(["1","2"]))
                        powerups.append(power)
                        powerspawn += 1
                        
                if len(asteroids) == 0 and asteroidspawn < 3 and level > 0:
                    wave_lenghtA += 5
                    for _ in range(min(wave_lenghtA,3-asteroidspawn)):
                        asteroid = Asteroid(random.randrange(50,WIDTH-50),random.randrange(-1500,-100),random.choice(["1","2"]))
                        asteroids.append(asteroid)
                        asteroidspawn += 1
           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - playerVelcity > 0: #Left (A-kYE ON THE kEYBOARD)
            player.x -= playerVelcity

        if keys[pygame.K_LEFT] and player.x - playerVelcity > 0: #Left (<-|-kYE ON THE kEYBOARD)
            player.x -= playerVelcity

        if keys[pygame.K_d] and player.x - playerVelcity + player.get_width() < WIDTH -10 : #Right (D-kYE ON THE kEYBOARD)
            player.x += playerVelcity

        if keys[pygame.K_RIGHT] and player.x - playerVelcity + player.get_width() < WIDTH -10 : #Right (->|-kYE ON THE kEYBOARD)
            player.x += playerVelcity
        if keys[pygame.K_w] and player.y - playerVelcity > 0: # up
            player.y -= playerVelcity
        if keys[pygame.K_s] and player.y + playerVelcity + player.get_height() + 15 < HEIGHT: # down
            player.y += playerVelcity
        if keys[pygame.K_SPACE]:
            player.shoot()
        if keys[pygame.K_SPACE]:
            player.shoot()
 
        #Moving Enemies 
        for enemy in enemies[:]:   
            enemy.move(enemy_velocity,player)
            enemy.move_lasers(laser_vel,player)
            if random.randrange(0,2*60) ==1:
                enemy.shoot()

            if collide(enemy,player):
                player.health -=10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -=1
                enemies.remove(enemy)
            
        player.move_lasers(-laser_vel,enemies)  

        for power in powerups:
            power.y +=enemy_velocity
            if power.y +power.height > HEIGHT:
                powerups.remove(power)
            if collide(power,player):
                if power.power_number == "1":
                    if player.health != 3:
                        player.health += 1
                elif power.power_number == "2":
                    player.COOLDOWN -= 20
                powerups.remove(power)

#Main Menu of the Program 
def main_menu(hi_score = 0):
    title_font = pygame.font.SysFont("Helvetica",50)
    score_font = pygame.font.SysFont("ocraextended", 20) 
    
    run = True
    while run:
        WIN.blit(BG,(0,0))
        title_label = title_font.render("Press Space to begin",1,(255,255,255))
        hiscore_indicator = score_font.render(f"Hi-Score:{hi_score}",1,(255,255,255))
        WIN.blit(hiscore_indicator,(10,10))
        WIN.blit(title_label,(WIDTH/2-title_label.get_width()/2,350))
        keys = pygame.key.get_pressed()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if keys[pygame.K_SPACE]:
                main()

    pygame.quit()     
         

main_menu()
