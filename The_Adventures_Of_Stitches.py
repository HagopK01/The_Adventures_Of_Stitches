# Hagop Kiljian
# David Kara-Yacoubian
#Importing pygame, system, and random modules
import pygame, sys
import random
#Initializing pygame
pygame.init()
#Setting the dimensions of the window (width, height). Change the numbers to change the size of the window
win = pygame.display.set_mode((1200, 600))
#setting name of the window
pygame.display.set_caption("The Adventures of Stitches")
#Defining time in game
clock = pygame.time.Clock()
#defining background for game
background = pygame.image.load('Backgrounds/Longer_Background.png')
background = pygame.transform.scale(background,(1500,600))
#defining captains quarters
bossbackground = pygame.image.load('Backgrounds/Captains_Quarters_.png')
bossbackground = pygame.transform.scale(bossbackground,(1500,600))

#defining background for menu
main_menu_background = pygame.image.load('Backgrounds/Game_Title_Screen.png')
main_menu_background = pygame.transform.scale(main_menu_background,(1200,600))
#defining background for game over
game_over_background = pygame.image.load('Backgrounds/Game_Over.png')
game_over_background = pygame.transform.scale(game_over_background,(1200,600))
#defining background for victory
victory_background = pygame.image.load('Backgrounds/Victory.png')
victory_background = pygame.transform.scale(victory_background,(1200,600))
#heart sprite for lives
heart = pygame.image.load('Buttons&Icons/Full_Heart.png')
heart = pygame.transform.scale(heart, (220, 220))
emptyheart = pygame.image.load('Buttons&Icons/Empty_Heart.png')
emptyheart = pygame.transform.scale(emptyheart, (220, 220))
#skull sprite for boss cutscene
skull = pygame.image.load('Buttons&Icons/SKULL.png')
pygame.display.set_icon(skull)
skull = pygame.transform.scale(skull, (220, 220))
# bullet sprite
cannonball = pygame.image.load('Sprites/Bullet.png')
cannonball = pygame.transform.scale(cannonball, (220, 220))
#options images
superjumptoggle = pygame.image.load('Buttons&Icons/Options/Toggle.png')
superjumptoggle = pygame.transform.scale(superjumptoggle, (440, 440))
bulletspeedtoggle = pygame.image.load('Buttons&Icons/Options/Bullet Speed.png')
bulletspeedtoggle = pygame.transform.scale(bulletspeedtoggle, (440, 440))
#controls images
esc = pygame.image.load('Buttons&Icons/Controls/Esc.png')
esc = pygame.transform.scale(esc, (440, 440))
wasd = pygame.image.load('Buttons&Icons/Controls/WASD with text.png')
wasd = pygame.transform.scale(wasd, (440, 440))
kstab = pygame.image.load('Buttons&Icons/Controls/K with text.png')
kstab = pygame.transform.scale(kstab, (440, 440))
#pause images
pauseon = pygame.image.load('Buttons&Icons/Pause/Paused1.png')
pauseon = pygame.transform.scale(pauseon, (440, 440))
pauseoff = pygame.image.load('Buttons&Icons/Pause/Paused2.png')
pauseoff = pygame.transform.scale(pauseoff, (440, 440))
#superjump sprites for superjump indicator
superjumpicon = pygame.image.load('Buttons&Icons/Super_Jump.png')
superjumpicon = pygame.transform.scale(superjumpicon, (220, 220))
superjumpready = pygame.image.load('Buttons&Icons/Ready.png')
superjumpready = pygame.transform.scale(superjumpready, (220, 220))
superjumppending = pygame.image.load('Buttons&Icons/SuperJumpPending.png')
superjumppending = pygame.transform.scale(superjumppending, (220, 220))
#setting sound effects
hitSound = pygame.mixer.Sound("Sounds&Music/Sound Effects/GettingHitSound.wav")
bossLaugh = pygame.mixer.Sound("Sounds&Music/Sound Effects/Wario Laugh.wav")
extraLifeSound = pygame.mixer.Sound("Sounds&Music/Sound Effects/coinsoundeffect.wav")

#Defining player object
class player(object):
    idleLeft = [pygame.image.load('Sprites/MainCharacter/Main Character Idle1.png'),
                pygame.image.load('Sprites/MainCharacter/Main Character Idle2.png')]
    idleRight = []
    walkLeft = [pygame.image.load('Sprites/MainCharacter/Main Character Walk Loop1.png'),
                pygame.image.load('Sprites/MainCharacter/Main Character Walk Loop2.png'),
                pygame.image.load('Sprites/MainCharacter/Main Character Walk Loop3.png'),
                pygame.image.load('Sprites/MainCharacter/Main Character Walk Loop4.png')]
    walkRight = []
    jumpLeft = [pygame.image.load('Sprites/MainCharacter/Main Character Jumping1.png'),
                pygame.image.load('Sprites/MainCharacter/Main Character Jumping2.png'),
                pygame.image.load('Sprites/MainCharacter/Main Character Jumping3.png')]
    jumpRight = []
    fallLeft = [pygame.image.load('Sprites/MainCharacter/Main Character Falling1.png'),
                pygame.image.load('Sprites/MainCharacter/Main Character Falling2.png')]
    fallRight = []
    crouchLeft = [pygame.image.load('Sprites/MainCharacter/Main Character Crouch.png')]
    crouchRight = []
    stabLeft = [pygame.image.load('Sprites/MainCharacter/Main Character Mellee Attack2.png'),
                pygame.image.load('Sprites/MainCharacter/Main Character Mellee Attack1.png')]
    stabRight = []
    hitLeft = [pygame.image.load('Sprites/MainCharacter/Main Character Hurt2.png')]
    hitRight = []
    """
    shootLeft = []
    shootRight = []
    """
    animations = [[idleLeft,idleRight],[walkLeft,walkRight],[jumpLeft,jumpRight],
                  [crouchLeft,crouchRight],[stabLeft,stabRight],[fallLeft,fallRight],[hitLeft,hitRight]]
    #flipping all images
    i = 0
    for animation in animations:
        j = 0
        for spriteLoop in animation:
            k = 0
            if j > 0:
                break
            for image in spriteLoop:
                image = pygame.transform.scale(spriteLoop[k], (220, 220))
                spriteLoop[k] = image
                image2 = pygame.transform.flip(image, True, False)
                animation[1].append(image2)
                k +=1
            j +=1
        i +=1
    def __init__(self, x, y, width, height, scrollx):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #The number changes running speed of player
        self.vel = 15
        ##number sets lives of player
        self.lives = 3
        self.hitcount = 0
        self.hitright = False
        self.isLand = False
        self.isCrouch = False
        self.left = False
        self.right = True
        self.standing = True
        self.walkCount = 0
        self.idleCount = 0
        #player's y velocity
        self.yvel = 0
        self.jumpCount = 0
        self.isStab = False
        self.stabCount = 0
        self.shootCount = 0
        self.superjumpCount = 0
        self.isClimb = False
        self.wasClimb = False
        self.climbCount = 0
        self.hitbox = (self.x + 35, self.y + 50, self.width - 130, self.height - 50)
        self.scrollx = scrollx

    def draw(self, win):
        self.move()
        # game over
        if self.lives < 1 and self.hitcount <55:
            global game_start
            game_start = False
        #invincibility after getting hit
        if self.hitcount > 0:
            self.hitcount -=1
        #hit knockback
        if self.hitcount >=50:
            self.vel = 20
            if self.hitright:
                if self.x < 1140:
                    self.x += self.vel
            else:
                if self.x > -20:
                    self.x -= self.vel
        else:
            self.vel = 15
        #stabbing animation
        if self.stabCount > 0:
            self.stabCount -= 1
        if self.stabCount == 4:
            self.isStab = True
        if self.stabCount < 1:
            self.isStab = False
        #shooting frames so player doesn't shoot too fast
        if self.shootCount > 0:
            self.shootCount +=1
        if self.shootCount >4:
            self.shootCount = 0
        #setting player sprite
        if self.walkCount + 1 >= 27:
            self.walkCount = 1
        if self.standing:
            self.idleCount +=1
        else:
            self.idleCount = 0
        if self.idleCount > 13:
            self.idleCount = 0
        #player jumps after jumpsquat animation
        if self.jumpCount > 0:
            self.jumpCount -=1
            if self.jumpCount == 0:
                self.isLand = False
                self.yvel = -15
                self.walkCount = 0
        #superjump
        if self.jumpCount < 0:
            self.jumpCount +=1
            if self.jumpCount == 0:
                self.isLand = False
                self.yvel = -22
                self.superjumpCount = 0
                self.walkCount = 0
        #SETTING PLAYER SPRITE
        #blinking animation after getting hit
        if self.hitcount < 10 or (self.hitcount >19 and self.hitcount <30) or (self.hitcount>39):
            #if in hitstun
            if self.hitcount >= 50:
                if self.right:
                    win.blit(self.hitRight[0], (self.x - 50, self.y - 40))
                else:
                    win.blit(self.hitLeft[0], (self.x - 50, self.y - 40))
            #if stabbing
            elif self.stabCount > 0:
                if self.right:
                    win.blit(self.stabRight[self.stabCount//5], (self.x - 30, self.y - 40))
                else:
                    win.blit(self.stabLeft[self.stabCount//5], (self.x - 65, self.y - 40))
            #if shooting
            elif self.shootCount > 0:
                pass
            elif self.climbCount > 0:
                pass
            #if in jumpsquat animation
            elif self.jumpCount > 0:
                if self.right:
                    win.blit(self.jumpRight[0], (self.x - 30, self.y - 40))
                else:
                    win.blit(self.jumpLeft[0], (self.x - 70, self.y - 40))
            #if in the air
            elif not(self.isLand):
                if self.right:
                    #if jumping up
                    if self.yvel <= 0:
                        if self.yvel <-6:
                            win.blit(self.jumpRight[1], (self.x - 30, self.y - 40))
                        else:
                            win.blit(self.jumpRight[2], (self.x - 30, self.y - 40))
                    #if falling down
                    else:
                        if self.yvel <6:
                            win.blit(self.fallRight[0], (self.x - 30, self.y - 40))
                        else:
                            win.blit(self.fallRight[1], (self.x - 30, self.y - 40))
                else:
                    # if jumping up
                    if self.yvel <= 0:
                        if self.yvel <-6:
                            win.blit(self.jumpLeft[1], (self.x - 70, self.y - 40))
                        else:
                            win.blit(self.jumpLeft[2], (self.x - 70, self.y - 40))
                    else:
                        # if falling down
                        if self.yvel <6:
                            win.blit(self.fallLeft[0], (self.x - 70, self.y - 40))
                        else:
                            win.blit(self.fallLeft[1], (self.x - 70, self.y - 40))
            #if in the walking loop
            elif self.walkCount > 0:
                if self.right:
                    win.blit(self.walkRight[self.walkCount//7], (self.x - 60, self.y - 40))
                else:
                    win.blit(self.walkLeft[self.walkCount // 7], (self.x - 40, self.y - 40))
            #if crouching
            elif self.isCrouch:
                if self.right:
                    win.blit(self.crouchRight[0], (self.x-40,self.y-40))
                else:
                    win.blit(self.crouchLeft[0], (self.x - 60, self.y - 40))
            #if doing nothing,so just standing, idle animation
            else:
                if self.right:
                    win.blit(self.idleRight[self.idleCount//7], (self.x-35,self.y-40))
                else:
                    win.blit(self.idleLeft[self.idleCount//7], (self.x-65, self.y - 40))
        #setting player hitboxes
        if self.isCrouch:
            self.hitbox = (self.x + 35, self.y + 70, self.width-130, self.height-70)
        else:
            self.hitbox = (self.x + 35, self.y + 50, self.width-130, self.height-50)
        #draws hitbox
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        #pygame.draw.rect(win, (255, 0, 0), (self.x,self.y,self.width,self.height), 2)
        #setting player's stabbing hitboxes
        if self.right:
            self.stabhitbox = (self.hitbox[0]+110, self.hitbox[1]+20, self.width/4, self.height/2)
        else:
            self.stabhitbox = (self.hitbox[0] - 100, self.hitbox[1] + 20, self.width / 4, self.height / 2)
        #draws stabbing hitbox
        """
        if self.isStab:
            pygame.draw.rect(win, (255, 0, 0), self.stabhitbox, 2)"""

    def move(self):
        global keys
        keys = pygame.key.get_pressed()
        # Movement left and right
        # cant move during boss cutscene
        if not (level == 3 and cutsceneCount > 0 and cutsceneCount < 90):
            # cant move while in hitstun
            if self.hitcount < 50:
                # change left moving key "a"
                if keys[pygame.K_a]:
                    if not (self.isCrouch) or not (self.isLand):
                        if self.scrollx > 0:
                            if self.x > 200:
                                self.x -= self.vel
                            else:
                                self.scrollx -= self.vel
                        else:
                            if self.x > 0:
                                self.x -= self.vel
                        self.walkCount += 1
                        if self.stabCount > 10 or self.stabCount == 0:
                            self.left = True
                            self.right = False
                            self.standing = False
                # change right moving key "d"
                elif keys[pygame.K_d]:
                    if not (self.isCrouch) or not (self.isLand):
                        if self.scrollx + 1000 < last_tilex[level-1]:
                            if self.x < 800:
                                self.x += self.vel
                            else:
                                self.scrollx += self.vel
                        else:
                            if self.x <= 1140:
                                self.x += self.vel
                        self.walkCount += 1
                        if self.stabCount > 10 or self.stabCount == 0:
                            self.right = True
                            self.left = False
                            self.standing = False
                else:
                    self.standing = True
                    self.walkCount = 0
        # cant attack until after boss cutscene
        if not (level == 3 and cutsceneCount > 0):
            """
            #Player shooting bullets
            #change shooting key "l", cant shoot while crouched
            if keys[pygame.K_l] and not(self.isCrouch):
                #cant shoot while crouched or while stabbing or if in hitstun
                if self.shootCount == 0 and self.stabCount ==0 and self.hitcount <50:
                    if self.left:
                        facing = -1
                    else:
                        facing = 1
                    #2 is max number of bullets on screen at a time
                    if len(bullets) < 2:
                        #(0,0,0)is color, 10 is bullet size
                        bullets.append(
                            projectile(round(self.x + self.width / 2)+scrollx, round(self.y + self.height // 2), 10, (0, 0, 0), facing,level))

                    self.shootCount = 1
            """
            # cant stab while crouching
            if keys[pygame.K_k] and not (self.isCrouch):
                # cant stab if already stabbing, if shooting, or if in hitstun
                if self.stabCount == 0 and self.shootCount == 0 and self.hitcount < 50:
                    self.stab()

        # player falls down pit
        if self.y > 580:
            self.x = 80
            self.y = 150
            self.yvel = 0
        # player collision with platforms
        self.isLand = False
        # checks level to collide with platforms
        for Platform in stage_layout[level-1][0]:
            # player on a platform
            if self.y + self.height >= Platform.y and self.y + self.height <= Platform.y + Platform.height:
                if self.x + (self.width / 2) >= Platform.x and self.x + (
                        self.width / 2) <= Platform.x + Platform.width + 40:
                    if not(self.isClimb):
                        if self.yvel >= 0:
                            self.isLand = True
                            self.yvel = 0
                            self.y = Platform.y - self.height
                    elif (keys[pygame.K_w] or keys[pygame.K_s]) and not(keys[pygame.K_LSHIFT]):
                        self.isClimb = False
        #player obtains item
        for item in stage_layout[level-1][3]:
            if self.hitbox[1] < item.y + 200 and self.hitbox[1] + self.hitbox[3] > item.y + 70:
                if self.hitbox[0] + self.hitbox[2] > item.x+ 100 and self.hitbox[0] < item.x + 150:
                    if item.image == heart:
                        if self.lives < 3:
                            self.lives +=1
                        extraLifeSound.play()
                        item.kill()
        #cant move vertically if in captain cutscene
        if cutsceneCount == 0 or cutsceneCount == 90:
            self.wasClimb = False
            #player climbing ladder
            for ladder in stage_layout[level - 1][2]:
                # player climbing ladders
                if (self.y + self.height >= ladder.y and self.y + self.height <= ladder.y + ladder.height) and \
                        (self.x + 10 >= ladder.x and self.x +
                        self.width -30 <= ladder.x + ladder.width):
                    if not (self.isClimb) and (keys[pygame.K_w] or keys[pygame.K_s]) and keys[pygame.K_LSHIFT]:
                        self.isClimb = True
                        self.yvel = 0
                    if keys[pygame.K_LSHIFT]:
                        self.wasClimb = True
            if not(self.wasClimb):
                self.isClimb = False
            # player falling
            if not self.isLand and not self.isClimb:
                self.isLand = False
                self.yvel += 1
                self.y += self.yvel
                self.y += self.yvel
            #player going up or down ladder
            elif self.isClimb:
                if keys[pygame.K_w]:
                    self.y -= 12
                if keys[pygame.K_s]:
                    self.y += 12
            # Player Jumping and Crouching
            else:
                self.yvel = 0
                # player jump
                if keys[pygame.K_w] and not (self.isCrouch):
                    # not in jumpsquat and not in hitstun
                    if self.jumpCount == 0 and self.hitcount < 50:
                        self.jumpCount = 2
                #superjump
                if keys[pygame.K_SPACE] and self.superjumpCount >0:
                    # not in jumpsquat and not in hitstun
                    if self.jumpCount == 0 and self.hitcount < 50:
                        self.jumpCount = -2
                # Crouching
                if keys[pygame.K_s]:
                    if self.hitcount < 50:
                        self.isCrouch = True
                        self.walkCount = 0
                        if superjump == True and self.superjumpCount<100:
                            self.superjumpCount +=1
                else:
                    self.isCrouch = False
                    self.superjumpCount = 0
        # Player hit by an enemy or stabs enemy(checks level)
        for enemy in stage_enemies[level-1]:
            if enemy.visible:
                #player and enemy collision
                if self.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and self.hitbox[1] + self.hitbox[3]  > enemy.hitbox[1]:
                    if self.hitbox[0] + self.hitbox[2] > enemy.hitbox[0] and self.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                        self.hit(1)
                        if self.x > enemy.x:
                            self.hitright = True
                        else:
                            self.hitright = False
                #player stabs an enemy
                if self.isStab and enemy.__class__ != captainbird:
                    if self.stabhitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and self.stabhitbox[1] + \
                            self.stabhitbox[3] > enemy.hitbox[1]:
                        if self.stabhitbox[0] + self.stabhitbox[2] > enemy.hitbox[0] and \
                                self.stabhitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                            if enemy.hitCount ==0:
                                enemy.hit(2)
                                enemy.hitCount = 7
                #player stabbed by grunt
                if enemy.__class__ == walker:
                    if enemy.isStab:
                        if enemy.stabhitbox[1] < self.hitbox[1] + self.hitbox[3] and enemy.stabhitbox[1] + enemy.stabhitbox[3] > self.hitbox[1]:
                            if enemy.stabhitbox[0] + enemy.stabhitbox[2] > self.hitbox[0] and enemy.stabhitbox[0] < self.hitbox[0] + self.hitbox[2]:
                                self.hit(1)
                                if self.x > enemy.x:
                                    self.hitright = True
                                else:
                                    self.hitright = False

    def hit(self,damage):
        if self.hitcount == 0:
            #plays hit sound
            hitSound.play()
            self.hitcount = 60
            self.stabCount = 0
            # reduces player lives
            self.lives -= damage
            self.yvel = 3
    def stab(self):
        self.stabCount = 10

class powerup(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,image):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = image
        self.width = width
        self.height = height
        self.scrollx = self.x
    def draw(self,win):
        self.x = self.scrollx - Stitches.scrollx
        win.blit(self.image, (self.x,self.y, self.width,self.height))

#Defining player's bullets
class projectile(object):
    def __init__(self, x, y, radius, color, facing, level):
        self.x = x
        self.y = y
        self.scrollx = self.x
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = bulletspeed * self.facing
        self.level = level

    def draw(self, win):
        #pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        win.blit(cannonball, (self.x- 100,self.y - 150))
        self.move()
    def move(self):
        self.x = self.scrollx - Stitches.scrollx
        # bullet moving
        if self.scrollx < 4000 and self.scrollx > 0:
            self.scrollx += self.vel
        # bullet disappears off screen
        if self.x > 1200 or self.x <= 0:
            bullets.pop(bullets.index(self))
        elif self.level != level:
            bullets.pop(bullets.index(self))
        else:
            # enemy and bullet collision
            if level == 1:
                for enemy in level_1_enemies:
                    if enemy.visible:
                        if self.y - self.radius < enemy.hitbox[1] + enemy.hitbox[3] and self.y + self.radius > \
                                enemy.hitbox[1]:
                            if self.x + self.radius > enemy.hitbox[0] and self.x - self.radius < enemy.hitbox[
                                0] + enemy.hitbox[2]:
                                enemy.hit(1)
                                # bullet disappears
                                bullets.pop(bullets.index(self))
            if level == 2:
                for enemy in level_2_enemies:
                    if enemy.visible:
                        if self.y - self.radius < enemy.hitbox[1] + enemy.hitbox[3] and self.y + self.radius > \
                                enemy.hitbox[1]:
                            if self.x + self.radius > enemy.hitbox[0] and self.x - self.radius < enemy.hitbox[
                                0] + enemy.hitbox[2]:
                                enemy.hit(1)
                                # bullet disappears
                                bullets.pop(bullets.index(self))

            if captain.visible and level == 3:
                if self.y - self.radius < captain.hitbox[1] + captain.hitbox[3] and self.y + self.radius > \
                        captain.hitbox[1]:
                    if self.x + self.radius > captain.hitbox[0] and self.x - self.radius < captain.hitbox[0] + \
                            captain.hitbox[2]:
                        captain.hit(1)
                        bullets.pop(bullets.index(self))

#Defining enemy bullets
class enemy_projectile(object):
    #cannonball sprite
    bigcannonball = pygame.image.load('Sprites/BossCharacter/Main Boss Cannon ball.png')
    bigcannonball = pygame.transform.scale(bigcannonball, (220, 220))
    def __init__(self, x, y, radius, color, level, enemyfacing):
        self.x = x
        self.y = y
        self.scrollx = self.x
        self.radius = radius
        self.color = color
        self.level = level
        #Number sets enemy bullet speed
        if self.level <3:
            self.vel = 20 * enemyfacing
        else:
            self.vel = 16 * enemyfacing

    def draw(self, win):
        self.x = self.scrollx - Stitches.scrollx
        if self.level <3:
            win.blit(cannonball, (self.x - 100, self.y - 150))
        else:
            win.blit(self.bigcannonball, (self.x - 110, self.y - 120))
        #pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        self.move()
    def move(self):
        # Enemy bullet movement and hitting player
        # enemy bullet moving
        if self.scrollx < 4000 and self.scrollx > 0:
            self.scrollx += self.vel
        # disappears off screen
        if self.x > 1200 or self.x <= 0:
            enemy_bullets.pop(enemy_bullets.index(self))
        # Checking source of bullets so they disappear after each level
        elif self.level != level:
            enemy_bullets.pop(enemy_bullets.index(self))
        else:
            # player and enemy bullet collision
            if self.y - self.radius < Stitches.hitbox[1] + Stitches.hitbox[
                3] and self.y + self.radius > Stitches.hitbox[1]:
                if self.x + self.radius > Stitches.hitbox[
                    0] and self.x - self.radius < Stitches.hitbox[0] + Stitches.hitbox[2]:
                    Stitches.hit(1)
                    if Stitches.hitbox[0] + Stitches.hitbox[2] / 2 > self.x:
                        Stitches.hitright = True
                    if Stitches.hitbox[0] + Stitches.hitbox[2] / 2 < self.x:
                        Stitches.hitright = False
                    # bullet disappears
                    enemy_bullets.pop(enemy_bullets.index(self))

#Defining grunts
class walker(pygame.sprite.Sprite):
    """
    i = 0
    for costume in ('Sprites/KnifeCharacter'):

        i +=1
    """
    walkLeft = [pygame.image.load('Sprites/KnifeCharacter/Knife_Walking_PNG1.png'), pygame.image.load('Sprites/KnifeCharacter/Knife_Walking_PNG2.png')]
    walkRight = []
    attackLeft = [pygame.image.load('Sprites/KnifeCharacter/Knife_Attack3.png'),
                pygame.image.load('Sprites/KnifeCharacter/Knife_Attack2.png'),
                  pygame.image.load('Sprites/KnifeCharacter/Knife_Attack1.png')]
    attackRight = []
    i = 0
    for image in walkLeft:
        image = pygame.transform.scale(image, (220, 220))
        walkLeft[i] = image
        image2 = pygame.transform.flip(image, True, False)
        walkRight.append(image2)
        i +=1
    i = 0
    for image in attackLeft:
        image = pygame.transform.scale(image, (220, 220))
        attackLeft[i] = image
        image2 = pygame.transform.flip(image, True, False)
        attackRight.append(image2)
        i += 1
    def __init__(self, x, y, width, height, path):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scrollx = self.x
        self.isLand = True
        self.yvel = 0
        self.path = path
        self.walkCount = 0
        self.stabCount = 0
        self.isStab = False
        #Number sets walk speed of grunt
        self.vel = 7
        #grunt climbing variables
        self.wasClimb = False
        self.climbDown = False
        self.climbUp = False
        self.climbCount = 0
        #number sets health of grunt
        self.health = 5
        self.hitCount = 0
        self.visible = True
        # sets hitbox
        self.hitbox = (self.x + 35, self.y + 50, self.width - 130, self.height - 50)
        #sets stab hitbox
        self.stabhitbox = (self.hitbox[0] + self.hitbox[2], self.hitbox[1] + self.hitbox[3] / 2, self.width / 3,self.height / 7)

    def draw(self, win):
        if self.visible:
            self.x = self.scrollx - Stitches.scrollx
            if self.walkCount + 1 >= 10:
                self.walkCount = 0
            if self.climbCount > 0:
                self.climbCount += 1
            if self.climbCount + 1 >=20 and (self.climbDown or self.climbUp):
                self.climbCount = 0
            elif self.climbCount + 1 >=40:
                self.climbCount = 0
            if self.hitCount > 0:
                self.hitCount -=1
            #checks to start stabbing animation
            if self.isLand and (self.x-100 <= Stitches.x and self.x+100 >= Stitches.x):
                if self.y-50 <= Stitches.y and self.y+50 >= Stitches.y:
                    if self.stabCount == 0 and not(self.climbUp or self.climbDown):
                        self.stabCount = 16
                        self.walkCount = 0
                        if self.x < Stitches.x:
                            self.right = True
                            self.vel = 8
                        else:
                            self.right = False
                            self.vel = -8
            #stabbing animation
            if self.stabCount > 0:
                self.stabCount -= 1
                if self.stabCount == 5:
                    self.isStab = True
                if self.stabCount < 2:
                    self.isStab = False
                if self.right:
                    self.stabhitbox = (
                    self.hitbox[0] + self.hitbox[2], self.hitbox[1] + self.hitbox[3] / 2, self.width / 3,
                    self.height / 7)
                    win.blit(self.attackRight[self.stabCount // 6], (self.x - 50, self.y - 40))
                else:
                    self.stabhitbox = (
                    self.hitbox[0] - self.hitbox[2], self.hitbox[1] + self.hitbox[3] / 2, self.width / 3,
                    self.height / 7)
                    win.blit(self.attackLeft[self.stabCount // 6], (self.x - 50, self.y - 40))
                #draws stabbing hitbox
                """
                if self.isStab:
                    pygame.draw.rect(win, (255, 0, 0), self.stabhitbox, 2)"""
            #not stabbing animation
            else:
                self.move()
                if self.vel > 0:
                    win.blit(self.walkRight[self.walkCount // 5], (self.x -50, self.y-40))
                    self.walkCount += 1
                else:
                    win.blit(self.walkLeft[self.walkCount // 5], (self.x-50, self.y-40))
                    self.walkCount += 1
            #sets hitbox
            self.hitbox = (self.x + 35, self.y + 50, self.width-130, self.height-50)
            #pygame.draw.rect(win, (0,0,0), self.hitbox,2)
            #sets health bar
            pygame.draw.rect(win, (255, 0, 0), (self.x - 10, self.y +6, self.width+10, 14))
            pygame.draw.rect(win, (0, 128, 0), (self.x - 11, self.y +4, (self.width*self.health)/4.5, 17))
    #grunt walking cycle
    def move(self):
        self.wasClimb = False
        #grunt climbing ladders
        for ladder in stage_layout[level - 1][2]:
            if (self.y + self.height >= ladder.y and self.y + self.height <= ladder.y + ladder.height) and \
                    (self.x + 10 >= ladder.x and self.x +
                     self.width - 30 <= ladder.x + ladder.width):
                if self.climbCount == 0:
                    self.climbCount = 1
                    if not(self.climbUp) and not(self.climbDown):
                        if self.y > ladder.y:
                            self.climbUp = True
                        else:
                            self.climbDown = True
                self.wasClimb = True
        if not(self.wasClimb):
            if self.climbUp or self.climbDown:
                self.climbCount = 1
                self.vel *= -1
            self.climbUp = False
            self.climbDown = False
        #grunt not climbing
        if not(self.climbUp) and not(self.climbDown):
            if self.vel > 0:
                if self.scrollx + self.vel < self.path[1]:
                    self.scrollx += self.vel
                    self.walkCount +=1
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
            else:
                if self.scrollx - self.vel > self.path[0]:
                    self.scrollx += self.vel
                    self.walkCount += 1
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
            # grunt collision with platforms
            self.isLand = False
            for Platform in stage_layout[level-1][0]:
                # grunt on a platform
                if self.y + self.height >= Platform.y and self.y + self.height <= Platform.y + Platform.height:
                    if self.x + (self.width / 2) >= Platform.x and self.x + (
                            self.width / 2) <= Platform.x + Platform.width + 40:
                        if self.yvel >= 0:
                            self.isLand = True
                            self.yvel = 0
                            self.y = Platform.y - self.height
            # grunt falling
            if not self.isLand:
                self.isLand = False
                self.yvel += 1
                self.y += self.yvel
                self.y += self.yvel
        #grunt climbing
        else:
            if self.climbUp:
                self.y -= 10
            else:
                self.y +=10
    #grunt hit
    def hit(self,damage):
        self.health -= damage
        if self.health < 1:
            self.visible = False

#Defining gunman
class shooter(pygame.sprite.Sprite):
    idleLeft = [pygame.image.load('Sprites/GunCharacter/Gun_Character_Idle1.png'),
                pygame.image.load('Sprites/GunCharacter/Gun_Character_Idle2.png')]
    idleRight = []
    shootLeft = [pygame.image.load('Sprites/GunCharacter/gun_aim_PNG1.png'),
                  pygame.image.load('Sprites/GunCharacter/gun_aim_PNG2.png')]
    shootRight = []
    i = 0
    for image in idleLeft:
        image = pygame.transform.scale(image, (220, 220))
        idleLeft[i] = image
        image2 = pygame.transform.flip(image, True, False)
        idleRight.append(image2)
        i += 1
    i = 0
    for image in shootLeft:
        image = pygame.transform.scale(image, (220, 220))
        shootLeft[i] = image
        image2 = pygame.transform.flip(image, True, False)
        shootRight.append(image2)
        i += 1
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scrollx = self.x
        self.isLand = False
        self.right = False
        self.facing = -1
        self.yvel = 0
        # gunman climbing variables
        self.wasClimb = False
        self.climbDown = False
        self.climbUp = False
        self.climbCount = 0
        #sets idle cycle
        self.idleCount = 0
        self.shootCount = 0
        #sets health of gunman
        self.health = 3
        self.hitCount = 0
        self.neg = 1
        self.visible = True

    def draw(self, win):
        if self.visible:
            self.x = self.scrollx - Stitches.scrollx
            self.move()
            if self.shootCount >0:
                self.shootCount -=1
            if self.climbCount > 0:
                self.climbCount +=1
            if self.climbCount + 1 >= 20:
                self.climbCount = 0
            if self.climbCount == 0:
                self.shoot()
            if self.hitCount > 0:
                self.hitCount -=1
            #gun character shooting
            if self.shootCount > 70:
                if self.shootCount == 89:
                    self.idleCount = 0
                    if Stitches.x > self.x:
                        self.right = True
                        # bullet shot towards player
                        self.facing = 1
                    else:
                        self.right = False
                        self.facing = -1
                if self.right:
                    win.blit(self.shootRight[(self.shootCount-70) // 10], (self.x-30, self.y - 40))
                else:
                    win.blit(self.shootLeft[(self.shootCount-70) // 10], (self.x - 65, self.y - 40))

            #gun character standing
            else:
                if self.idleCount + 1 >= 20:
                    self.idleCount = 0
                self.idleCount +=1
                if Stitches.x > self.x:
                    win.blit(self.idleRight[self.idleCount//10], (self.x-30,self.y-40))
                else:
                    win.blit(self.idleLeft[self.idleCount//10], (self.x - 65, self.y - 40))
            #sets hitbox
            self.hitbox = (self.x + 35, self.y + 50, self.width-130, self.height-50)
            #pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)
            # sets health bar
            pygame.draw.rect(win, (255, 0, 0), (self.x - 10, self.y - 30, self.width - 5, 14))
            pygame.draw.rect(win, (0, 128, 0), (self.x - 11, self.y - 32, (self.width * self.health) / 3, 17))
    #gunman on platforms
    def move(self):
        self.wasClimb = False
        # gunman climbing ladders
        for ladder in stage_layout[level - 1][2]:
            if (self.y + self.height >= ladder.y and self.y + self.height <= ladder.y + ladder.height) and \
                    (self.x + 10 >= ladder.x and self.x +
                     self.width - 30 <= ladder.x + ladder.width):
                if self.climbCount == 0 and self.shootCount == 65:
                    self.climbCount = 1
                    if not (self.climbUp) and not (self.climbDown):
                        if self.y > Stitches.y:
                            self.climbUp = True
                        elif self.y < Stitches.y:
                            self.climbDown = True
                if self.shootCount <=65 and self.shootCount >=45:
                    self.wasClimb = True
        #gunman gets off ladder or not climbing
        if not (self.wasClimb):
            if self.climbUp or self.climbDown:
                self.climbCount = 1
            self.climbUp = False
            self.climbDown = False
        #gunman not climbing
        if not (self.climbUp) and not (self.climbDown):
            # gunman collision with platforms
            self.isLand = False
            for Platform in stage_layout[level-1][0]:
                # gunman on a platform
                if self.y + self.height >= Platform.y and self.y + self.height <= Platform.y + Platform.height:
                    if self.x + (self.width / 2) >= Platform.x and self.x + (
                            self.width / 2) <= Platform.x + Platform.width + 40:
                        if self.yvel >= 0:
                            self.isLand = True
                            self.yvel = 0
                            self.y = Platform.y - self.height
            # gunman falling
            if not self.isLand:
                self.isLand = False
                self.yvel += 1
                self.y += self.yvel
                self.y += self.yvel
        #gunman climbing
        else:
            if self.climbUp:
                self.y -= 10
            else:
                self.y += 10
    #gunman shooting
    def shoot(self):
        # Gunman shooting bullets
        if self.shootCount == 0:
            if self.visible:
                self.shootCount = 89
        # gunman shooting bullets
        if self.shootCount == 78:
            # (0,0,0) is bullet color, 8 is bullet size
            if self.facing == -1:
                enemy_bullets.append(enemy_projectile(round(self.scrollx - 10),
                                                      round(self.y + self.height // 2 + 5), 8,
                                                      (0, 0, 0), level, self.facing))
            else:
                enemy_bullets.append(enemy_projectile(round(self.scrollx + 125),
                                                      round(self.y + self.height // 2 + 5), 8,
                                                      (0, 0, 0), level, self.facing))

    #gunman hit
    def hit(self,damage):
        self.health -= damage
        if self.health < 1:
            self.visible = False

#defining seagulls
class bird (pygame.sprite.Sprite):
    flapRight = [pygame.image.load('Sprites/Seagull/Seagull_PNG1.png'),
                pygame.image.load('Sprites/Seagull/Seagull_PNG2.png')]
    flapLeft = []
    i = 0
    for image in flapRight:
        image = pygame.transform.scale(image, (220, 220))
        flapRight[i] = image
        image2 = pygame.transform.flip(image, True, False)
        flapLeft.append(image2)
        i += 1
    def __init__(self, x, y, width, height, path):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scrollx = self.x
        self.path = path
        self.vel = 5
        self.health = 3
        self.hitCount = 0
        self.visible = True
        self.flapCount = 0
        self.poopCount = random.randint(0,59)
        # sets hitbox
        self.hitbox = (self.x + 35, self.y + 50, self.width - 130, self.height - 50)

    def draw(self, win):
        if self.visible:
            self.x = self.scrollx - Stitches.scrollx
            if self.flapCount + 1 >= 30:
                self.flapCount = 0
            if self.poopCount >0:
                self.poopCount -=1
            if self.hitCount >0:
                self.hitCount -=1
            self.poop()
            self.move()
            if self.vel > 0:
                win.blit(self.flapRight[self.flapCount // 15], (self.x - 50, self.y - 40))
                self.flapCount += 1
            else:
                win.blit(self.flapLeft[self.flapCount // 15], (self.x - 70, self.y - 40))
                self.flapCount += 1
            # sets hitbox
            self.hitbox = (self.x + 5, self.y + 60, self.width - 100, self.height - 70)
            #pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)
            # sets health bar
            pygame.draw.rect(win, (255, 0, 0), (self.x, self.y + 30, self.width - 75, 14))
            pygame.draw.rect(win, (0, 128, 0), (self.x - 2, self.y + 28, (self.width * self.health) / 5, 17))

    def move(self):
        if self.vel > 0:
            if self.scrollx + self.vel < self.path[1]:
                self.scrollx += self.vel
                self.flapCount += 1
            else:
                self.vel = self.vel * -1
        else:
            if self.scrollx - self.vel > self.path[0]:
                self.scrollx += self.vel
                self.flapCount += 1
            else:
                self.vel = self.vel * -1
    def poop(self):
        # bird dropping bombs
        if self.poopCount == 0:
            bombs.append(
                explosive(self.scrollx + 20, self.y + self.height, 12,
                          level))
            self.poopCount = 60
    def hit(self,damage):
        self.health -= damage
        if self.health < 1:
            self.visible = False

#defining bombs
class explosive(object):
    bombimage = pygame.image.load('Sprites/Seagull/Bomb_PNG.png')
    bombimage = pygame.transform.scale(bombimage,(220,220))
    bombexplode = pygame.image.load('Sprites/Seagull/Bomb_PNG2.png')
    bombexplode = pygame.transform.scale(bombexplode, (220, 220))
    def __init__(self, x, y, radius, level):
        self.x = x
        self.y = y
        self.scrollx = self.x
        self.radius = radius
        self.yvel = 0
        self.level = level
        self.boomCount = 0
    def draw(self,win):
        self.fall()
        self.boom()
        if self.boomCount >0:
            win.blit(self.bombexplode, (self.x-110, self.y-110))
        else:
            win.blit(self.bombimage, (self.x - 110, self.y - 110))
        #pygame.draw.circle(win, (255,0,0), (self.x,self.y), self.radius)
    def fall(self):
        self.x = self.scrollx - Stitches.scrollx
        if self.x > 1200 or self.x < 0:
            bombs.pop(bombs.index(self))
        # bomb disappears after blowing up
        elif self.boomCount > 12:
            bombs.pop(bombs.index(self))
        elif self.level != level:
            bombs.pop(bombs.index(self))
        else:
            for Platform in stage_layout[level-1][0]:
                if self.y + self.radius >= Platform.y and self.y + self.radius <= Platform.y + Platform.height:
                    if self.x + (self.radius / 2) >= Platform.x and self.x + (
                            self.radius / 2) <= Platform.x + Platform.width + 40:
                        if self.boomCount == 0:
                            self.boomCount = 1
            if self.y - self.radius < Stitches.hitbox[1] + Stitches.hitbox[3] and self.y + self.radius > \
                    Stitches.hitbox[1]:
                if self.x + self.radius > Stitches.hitbox[0] and self.x - self.radius < Stitches.hitbox[0] + \
                        Stitches.hitbox[2]:
                    Stitches.hit(1)
                    if Stitches.hitbox[0] + Stitches.hitbox[2] / 2 > self.x:
                        Stitches.hitright = True
                    if Stitches.hitbox[0] + Stitches.hitbox[2] / 2 < self.x:
                        Stitches.hitright = False
                    # bomb disappears
                    bombs.pop(bombs.index(self))
        # bomb falling
        if self.boomCount < 1:
            self.yvel += 1
            self.y += self.yvel
    def boom(self):
        if self.boomCount > 0:
            self.radius = 28
            self.boomCount += 1

#Defining captain
class boss(pygame.sprite.Sprite):
    idleLeft = [pygame.image.load('Sprites/BossCharacter/Main Boss Idle1.png'),
                pygame.image.load('Sprites/BossCharacter/Main Boss Idle2.png')]
    idleRight = []
    laughLeft = [pygame.image.load('Sprites/BossCharacter/Main Boss Laugh1.png'),
                pygame.image.load('Sprites/BossCharacter/Main Boss Laugh2.png')]
    laughRight = []
    walkLeft = [pygame.image.load('Sprites/BossCharacter/Main Boss Walk Loop1.png'),
                pygame.image.load('Sprites/BossCharacter/Main Boss Walk Loop2.png'),
                pygame.image.load('Sprites/BossCharacter/Main Boss Walk Loop3.png'),
                pygame.image.load('Sprites/BossCharacter/Main Boss Walk Loop4.png')]
    walkRight = []
    jumpLeft = [pygame.image.load('Sprites/BossCharacter/Main Boss Jumping1.png'),
                pygame.image.load('Sprites/BossCharacter/Main Boss Jumping2.png')]
    jumpRight = []
    shootLeft = [pygame.image.load('Sprites/BossCharacter/Cannon1.png'),
                  pygame.image.load('Sprites/BossCharacter/Cannon2.png')]
    shootRight = []
    animations = [[idleLeft,idleRight],[laughLeft,laughRight],[walkLeft, walkRight], [jumpLeft, jumpRight],
                  [shootLeft,shootRight]]
    # flipping all images
    i = 0
    for animation in animations:
        j = 0
        for spriteLoop in animation:
            k = 0
            if j > 0:
                break
            for image in spriteLoop:
                image = pygame.transform.scale(spriteLoop[k], (220, 220))
                spriteLoop[k] = image
                image2 = pygame.transform.flip(image, True, False)
                animation[1].append(image2)
                k += 1
            j += 1
        i += 1

    def __init__(self, x, y, width, height, path):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scrollx = self.x
        self.isLand = False
        self.yvel = 0
        self.path = path
        #changes captains walk speed
        self.vel = -8
        self.walkCount = 0
        self.idleCount = 0
        # captains's y velocity
        self.yvel = 0
        self.right = False
        self.isLand = False
        self.jumpCount = 0
        self.crouchCount = 0
        self.shootCount = 20
        #changes captains health
        self.health = 14
        self.hitCount = 0
        self.neg = 1
        self.visible = True
        self.hitbox = (self.x + 5, self.y + 20, self.width - 70, self.height - 20)

    def draw(self, win):
        if self.visible:
            self.x = self.scrollx - Stitches.scrollx
            if cutsceneCount >0:
                self.health = 14
                self.idleCount += 1
                if self.idleCount > 13:
                    self.idleCount = 0
            else:
                if self.walkCount + 1 >=28:
                    self.walkCount = 0
                if self.shootCount >0:
                    self.shootCount -=1
                if self.hitCount > 0:
                    self.hitCount -= 1
                self.shoot()
                if self.jumpCount > 0:
                    self.jumpCount -= 1
                    if self.jumpCount == 0:
                        self.isLand = False
                        self.yvel = -15
                        self.walkCount = 0
            #setting boss sprites
            #if in cutscene
            if cutsceneCount >0:
                if cutsceneCount == 90:
                    win.blit(self.idleLeft[self.idleCount // 7], (self.x - 65, self.y - 40))
                elif (cutsceneCount >=15 and cutsceneCount <30) or (cutsceneCount >45 and cutsceneCount <60) or (cutsceneCount >75 and cutsceneCount <90):
                    win.blit(self.laughLeft[1], (self.x - 65, self.y - 40))
                else:
                    win.blit(self.laughLeft[0], (self.x - 65, self.y - 40))
            # if shooting
            elif self.shootCount > 70:
                if self.shootCount == 89:
                    self.idleCount = 0
                    if Stitches.x > self.x:
                        self.right = True
                        # bullet shot towards player
                        self.facing = 1
                        self.vel = 8
                    else:
                        self.right = False
                        self.facing = -1
                        self.vel = -8
                if self.right:
                    win.blit(self.shootRight[(self.shootCount-70) // 10], (self.x-45, self.y - 40))
                else:
                    win.blit(self.shootLeft[(self.shootCount-70) // 10], (self.x - 45, self.y - 40))
            else:
                self.move()
                # if in jumpsquat animation
                if self.jumpCount > 0:
                    if self.right:
                        win.blit(self.jumpRight[0], (self.x - 45, self.y - 40))
                    else:
                        win.blit(self.jumpLeft[0], (self.x - 45, self.y - 40))
                # if in the air
                elif not (self.isLand):
                    if self.right:
                        win.blit(self.jumpRight[1], (self.x - 45, self.y - 40))
                    else:
                        win.blit(self.jumpLeft[1], (self.x - 45, self.y - 40))
                # if in the walking loop
                else:
                    if self.right:
                        win.blit(self.walkRight[self.walkCount // 7], (self.x - 50, self.y - 40))
                    else:
                        win.blit(self.walkLeft[self.walkCount // 7], (self.x - 40, self.y - 40))
            #sets hitbox
            self.hitbox = (self.x + 20, self.y + 20, self.width-90, self.height-30)
            #pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)
            # sets health bar
            pygame.draw.rect(win, (255, 0, 0), (self.x - 45, self.y - 60, self.width + 25, 14))
            pygame.draw.rect(win, (0, 128, 0), (self.x - 46, self.y - 62, (self.width * self.health) / 12, 17))
    #captain moving and jumping
    def move(self):
        if self.vel > 0:
            self.right = True
            if self.scrollx + self.vel < self.path[1]:
                self.scrollx += self.vel
                self.walkCount +=1
            else:
                self.vel = self.vel * -1
        else:
            self.right = False
            if self.scrollx - self.vel > self.path[0]:
                self.scrollx += self.vel
                self.walkCount += 1
            else:
                self.vel = self.vel * -1
        # captain collision with platforms
        self.isLand = False
        for Platform in stage_layout[level-1][0]:
            # captain on a platform
            if self.y + self.height >= Platform.y and self.y + self.height <= Platform.y + Platform.height:
                if self.x + (self.width / 2) >= Platform.x and self.x + (
                        self.width / 2) <= Platform.x + Platform.width + 40:
                    if self.yvel >= 0:
                        self.isLand = True
                        self.yvel = 0
                        self.y = Platform.y - self.height
        # captain falling
        if not self.isLand:
            self.isLand = False
            self.yvel += 1
            self.y += self.yvel
            self.y += self.yvel
        else:
            # checks if player is above boss vertically and near boss horizontally
            if self.y-50 > Stitches.y and (self.x-200 <= Stitches.x and self.x+200 >= Stitches.x):
                if self.jumpCount == 0:
                    self.isLand = False
                    self.jumpCount = 3
                    self.walkCount = 0
    def shoot(self):
        if self.shootCount == 0 and self.isLand:
            if self.visible:
                self.shootCount = 89
        if self.shootCount == 78:
            # (0,0,0) is bullet color, 8 is bullet size
            if self.facing == -1:
                enemy_bullets.append(enemy_projectile(round(self.scrollx - 10),
                                                      round(self.y + self.height // 2 + 5), 16,
                                                      (0, 0, 0), level, self.facing))
            else:
                enemy_bullets.append(enemy_projectile(round(self.scrollx + 125),
                                                      round(self.y + self.height // 2 + 5), 16,
                                                      (0, 0, 0), level, self.facing))
    #captain hit
    def hit(self,damage):
        self.health -= damage
        if self.health < 1:
            self.visible = False
#defining captain's parrot
class captainbird(pygame.sprite.Sprite):
    flapLeft = [pygame.image.load('Sprites/BossCharacter/Parrot/Parrot Flying1.png'),
                 pygame.image.load('Sprites/BossCharacter/Parrot/Parrot Flying2.png')]
    flapRight = []
    swoopLeft = [pygame.image.load('Sprites/BossCharacter/Parrot/Parrot Swoop1.png'),
                 pygame.image.load('Sprites/BossCharacter/Parrot/Parrot Swoop2.png')]
    swoopRight = []
    i = 0
    for image in flapLeft:
        image = pygame.transform.scale(image, (220, 220))
        flapLeft[i] = image
        image2 = pygame.transform.flip(image, True, False)
        flapRight.append(image2)
        i += 1
    i = 0
    for image in swoopLeft:
        image = pygame.transform.scale(image, (220, 220))
        swoopLeft[i] = image
        image2 = pygame.transform.flip(image, True, False)
        swoopRight.append(image2)
        i += 1

    def __init__(self, x, y, width, height, path):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scrollx = self.x
        self.path = path
        self.vel = -6
        self.right = False
        self.visible = True
        self.flapCount = 0
        self.swoopCount = 0
        # sets hitbox
        self.hitbox = (self.x + 35, self.y + 50, self.width - 130, self.height - 50)

    def draw(self, win):
        if self.visible:
            if captain.visible == False:
                self.visible = False
            if self.flapCount + 1 >= 30:
                self.flapCount = 0
            if self.swoopCount > 0:
                self.swoopCount -= 1
            if cutsceneCount == 0:
                if self.swoopCount == 0 and (self.x-120 <= Stitches.x and self.x+120 >= Stitches.x):
                    self.swoop()
                    if self.x < Stitches.x:
                        self.right = True
                        self.vel = 8
                    else:
                        self.right = False
                        self.vel = -8

                self.move()
            if self.swoopCount > 50:
                if self.right:
                    win.blit(self.swoopRight[(self.swoopCount-50) // 20], (self.x - 50, self.y - 30))
                else:
                    win.blit(self.swoopLeft[(self.swoopCount-50) //20], (self.x - 50, self.y - 30))
            else:
                if self.vel > 0:
                    win.blit(self.flapRight[self.flapCount // 15], (self.x - 50, self.y - 30))
                    self.flapCount += 1
                else:
                    win.blit(self.flapLeft[self.flapCount // 15], (self.x - 70, self.y - 30))
                    self.flapCount += 1
            # sets hitbox
            self.hitbox = (self.x + 5, self.y + 60, self.width - 100, self.height - 70)
            #pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)

    def move(self):
        self.x = self.scrollx - Stitches.scrollx
        if self.swoopCount > 69:
            self.scrollx += self.vel/2
            self.y += 17
        elif self.swoopCount > 49:
            self.scrollx += self.vel / 2
            self.y -= 17
        else:
            if self.vel > 0:
                if self.scrollx + self.vel < self.path[1]:
                    self.scrollx += self.vel
                    self.flapCount += 1
                else:
                    self.vel = self.vel * -1
            else:
                if self.scrollx - self.vel > self.path[0]:
                    self.scrollx += self.vel
                    self.flapCount += 1
                else:
                    self.vel = self.vel * -1

    def swoop(self):
        # parrot diving
        self.swoopCount = 89

#defining new menu buttons
class button(object):
    # play button sprites
    playbutton_up = pygame.image.load('Buttons&Icons/Menu/Play1.png')
    playbutton_up = pygame.transform.scale(playbutton_up, (220, 220))
    playbutton_down = pygame.image.load('Buttons&Icons/Menu/Play2.png')
    playbutton_down = pygame.transform.scale(playbutton_down, (220, 220))
    #controls button sprites
    controlsbutton_up = pygame.image.load('Buttons&Icons/Menu/Controls1.png')
    controlsbutton_up = pygame.transform.scale(controlsbutton_up, (220, 220))
    controlsbutton_down = pygame.image.load('Buttons&Icons/Menu/Controls2.png')
    controlsbutton_down = pygame.transform.scale(controlsbutton_down, (220, 220))
    # options button sprites
    optionsbutton_up = pygame.image.load('Buttons&Icons/Menu/Options1.png')
    optionsbutton_up = pygame.transform.scale(optionsbutton_up, (220, 220))
    optionsbutton_down = pygame.image.load('Buttons&Icons/Menu/Options2.png')
    optionsbutton_down = pygame.transform.scale(optionsbutton_down, (220, 220))
    # quit button sprites
    quitbutton_up = pygame.image.load('Buttons&Icons/Menu/Quit1.png')
    quitbutton_up = pygame.transform.scale(quitbutton_up, (220, 220))
    quitbutton_down = pygame.image.load('Buttons&Icons/Menu/Quit2.png')
    quitbutton_down = pygame.transform.scale(quitbutton_down, (220, 220))
    # return button sprites
    returnbutton_up = pygame.image.load('Buttons&Icons/Options/Return1.png')
    returnbutton_up = pygame.transform.scale(returnbutton_up, (220, 220))
    returnbutton_down = pygame.image.load('Buttons&Icons/Options/Return2.png')
    returnbutton_down = pygame.transform.scale(returnbutton_down, (220, 220))
    # resume button sprites
    resumebutton_up = pygame.image.load('Buttons&Icons/Pause/Resume1.png')
    resumebutton_up = pygame.transform.scale(resumebutton_up, (220, 220))
    resumebutton_down = pygame.image.load('Buttons&Icons/Pause/Resume2.png')
    resumebutton_down = pygame.transform.scale(resumebutton_down, (220, 220))
    # menu button sprites
    menubutton_up = pygame.image.load('Buttons&Icons/Pause/Menu1.png')
    menubutton_up = pygame.transform.scale(menubutton_up, (220, 220))
    menubutton_down = pygame.image.load('Buttons&Icons/Pause/Menu2.png')
    menubutton_down = pygame.transform.scale(menubutton_down, (220, 220))
    # off button sprites
    offbutton_up = pygame.image.load('Buttons&Icons/Options/OFF1.png')
    offbutton_up = pygame.transform.scale(offbutton_up, (220, 220))
    offbutton_down = pygame.image.load('Buttons&Icons/Options/OFF2.png')
    offbutton_down = pygame.transform.scale(offbutton_down, (220, 220))
    # on button sprites
    onbutton_up = pygame.image.load('Buttons&Icons/Options/ON1.png')
    onbutton_up = pygame.transform.scale(onbutton_up, (220, 220))
    onbutton_down = pygame.image.load('Buttons&Icons/Options/ON2.png')
    onbutton_down = pygame.transform.scale(onbutton_down, (220, 220))
    # fast button sprites
    fastbutton_up = pygame.image.load('Buttons&Icons/Options/Fast1.png')
    fastbutton_up = pygame.transform.scale(fastbutton_up, (220, 220))
    fastbutton_down = pygame.image.load('Buttons&Icons/Options/Fast2.png')
    fastbutton_down = pygame.transform.scale(fastbutton_down, (220, 220))
    # slow button sprites
    slowbutton_up = pygame.image.load('Buttons&Icons/Options/Slow1.png')
    slowbutton_up = pygame.transform.scale(slowbutton_up, (220, 220))
    slowbutton_down = pygame.image.load('Buttons&Icons/Options/Slow2.png')
    slowbutton_down = pygame.transform.scale(slowbutton_down, (220, 220))
    def __init__(self,x,y,width,height,image,imagex,imagey):
        self.x = x
        self.y = y
        self.image = image
        self.width = width
        self.height = height
        self.imagex = imagex
        self.imagey = imagey
    def draw(self, win, outline=None):
        #pygame.draw.rect(win, (255,0,0), (self.x, self.y, self.width, self.height), 0)
        # Call this method to draw the button on the screen
        win.blit(self.image,(self.imagex,self.imagey))

    def isOver(self, mousepos):
        if mousepos[0] > self.x and mousepos[0] < self.x + self.width:
            if mousepos[1] > self.y and mousepos[1] < self.y + self.height:
                return True

        return False

#creating platforms
class Platform(pygame.sprite.Sprite):
    # tileset sprite
    woodboard = pygame.image.load('Tilesets/Boat_Tile_1.png')
    woodboard = pygame.transform.scale(woodboard, (220, 220))
    sand = pygame.image.load('Tilesets/Beach.png')
    sand = pygame.transform.scale(sand, (220, 220))
    def __init__(self,x,y,width,height,image):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = image
        self.width = width
        self.height = height
        self.scrollx = self.x
    def draw(self,win):
        self.x = self.scrollx - Stitches.scrollx
        win.blit(self.image, (self.x,self.y-165,self.width,self.height))

#creating boxes for background
class background_tile(pygame.sprite.Sprite):
    box = pygame.image.load('Tilesets/Box.png')
    box = pygame.transform.scale(box, (220, 220))
    crate = pygame.image.load('Tilesets/Crate.png')
    crate = pygame.transform.scale(crate, (220, 220))
    tree = pygame.image.load('Tilesets/Tree.png')
    tree = pygame.transform.scale(tree, (220, 220))
    def __init__(self,x,y,width,height,image):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = image
        self.width = width
        self.height = height
        self.scrollx = self.x
    def draw(self,win):
        self.x = self.scrollx - Stitches.scrollx
        win.blit(self.image, (self.x,self.y-165,self.width,self.height))

class climbable(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,image):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = image
        self.width = width
        self.height = height
        self.scrollx = self.x
    def draw(self,win):
        self.x = self.scrollx - Stitches.scrollx
        win.blit(self.image, (self.x,self.y-165,self.width,self.height))
        pygame.draw.rect(win, (0,0,0), (self.x,self.y,self.width,self.height), 2)
"""
DEFINING ALL
MENUS AND SCREENS
"""
def main_menu():
    # defines play button
    play_button = button(520, 370, 105, 45, button.playbutton_up, 462, 285)
    # defines instructions button
    controls_button = button(465, 430, 210, 45, button.controlsbutton_up, 460, 342)
    # defines options button
    options_button = button(270, 500, 185, 45, button.optionsbutton_up, 250, 412)
    # defines quit button
    quit_button = button(700, 500, 105, 45, button.optionsbutton_up, 650, 412)
    # defines return button
    return_button = button(495, 500, 155, 45, button.returnbutton_up, 460, 412)
    # defines superjump on/off button
    superjump_button = button(520, 100, 75, 45, button.onbutton_up, 450, 10)
    # defines bullet speed button
    bulletspeed_button = button(520, 300, 105, 45, button.fastbutton_up, 450, 210)
    # if instructions are being viewed
    global instructions
    instructions = False
    # if options are being viewed
    global options
    options = False
    global superjump
    superjump = True
    global bulletspeed
    bulletspeed = 20
    global click
    click = False
    global music
    pygame.mixer.music.stop()
    music = pygame.mixer.music.load("Sounds&Music/Music/SpongeBob Production Music Oyster Girls.mp3")
    pygame.mixer_music.play(-1)
    # Main menu
    while True:
        global mousepos
        mousepos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            click = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(60)
        # main menu and instructions background set
        win.fill((60, 60, 250))
        # Main menu
        if not (instructions) and not (options):
            # defines title and menu buttons
            win.blit(main_menu_background, (0, 0))
            # draws play button
            play_button.draw(win)
            if play_button.isOver(mousepos):
                play_button.image = button.playbutton_down
            else:
                play_button.image = button.playbutton_up
            # draws instructions button
            controls_button.draw(win)
            if controls_button.isOver(mousepos):
                controls_button.image = button.controlsbutton_down
            else:
                controls_button.image = button.controlsbutton_up
            # draws options button
            options_button.draw(win)
            if options_button.isOver(mousepos):
                options_button.image = button.optionsbutton_down
            else:
                options_button.image = button.optionsbutton_up
            # draws quit button
            quit_button.draw(win)
            if quit_button.isOver(mousepos):
                quit_button.image = button.quitbutton_down
            else:
                quit_button.image = button.quitbutton_up
        else:
            win.blit(background, (0, 0))
            # Instructions screen
            if instructions:
                win.blit(esc, (-100, 0))
                win.blit(kstab, (300, 0))
                win.blit(wasd, (700, 0))
                # draws return button
                return_button.draw(win)
                if return_button.isOver(mousepos):
                    return_button.image = button.returnbutton_down
                else:
                    return_button.image = button.returnbutton_up
            # options
            else:
                win.blit(superjumptoggle, (0, -100))
                win.blit(bulletspeedtoggle, (0, 100))
                # draws return button
                superjump_button.draw(win)
                if superjump_button.isOver(mousepos):
                    if superjump:
                        superjump_button.image = button.onbutton_down
                    else:
                        superjump_button.image = button.offbutton_down
                else:
                    if superjump:
                        superjump_button.image = button.onbutton_up
                    else:
                        superjump_button.image = button.offbutton_up
                # draws bullet speed button
                bulletspeed_button.draw(win)
                if bulletspeed_button.isOver(mousepos):
                    if bulletspeed == 20:
                        bulletspeed_button.image = button.fastbutton_down
                    else:
                        bulletspeed_button.image = button.slowbutton_down
                else:
                    if bulletspeed == 20:
                        bulletspeed_button.image = button.fastbutton_up
                    else:
                        bulletspeed_button.image = button.slowbutton_up
                # draws return button
                return_button.draw(win)
                if return_button.isOver(mousepos):
                    return_button.image = button.returnbutton_down
                else:
                    return_button.image = button.returnbutton_up

        # Checks if mouse over return button and if button clicked, goes to main menu
        if return_button.isOver(mousepos) and (options or instructions):
            if click:
                click = False
                instructions = False
                options = False
        # Checks if mouse over quit button and if button clicked, game quits
        if quit_button.isOver(mousepos) and not (instructions) and not (options):
            if click:
                pygame.quit()
                sys.exit()
        # Checks if mouse over play button and if button clicked, game starts
        if play_button.isOver(mousepos) and not (instructions) and not (options):
            if click:
                stage_1()
                break
        # Checks if mouse over instructions button and if button clicked, goes to instructions
        if controls_button.isOver(mousepos) and (not (instructions) and not (options)):
            if click:
                click = False
                instructions = True
        # Checks if mouse over options button and if button clicked, goes to options
        if options_button.isOver(mousepos) and not (instructions) and not (options):
            if click:
                click = False
                options = True
        # Checks if mouse over superjump button and if button clicked, toggles superjump
        if superjump_button.isOver(mousepos) and options:
            if click:
                click = False
                if superjump:
                    superjump = False
                else:
                    superjump = True
        # Checks if mouse over bullet speed button and if button clicked, toggles bullet speed
        if bulletspeed_button.isOver(mousepos) and options:
            if click:
                click = False
                if bulletspeed == 20:
                    bulletspeed = 40
                else:
                    bulletspeed = 20
        # refreshes screen
        pygame.display.update()


def stage_1():
    # starts at level 1
    global level
    level = 1
    #Defines stage elements for stage 1
    # defines platforms for level 1. ' ' is air, G is ground, B is ground with box, C is ground with crate, T is ground with tree
    level_1_map = [[' ', ' ', ' ', ' ', ' ', 'G', 'G', 'C', ' ', ' ', ' ', ' ', 'G', 'G', 'G', ' ', ' ', ' '],
                   [' ', ' ', ' ', 'B', 'G', ' ', ' ', ' ', 'G', 'G', 'G', ' ', 'G', 'G', 'G', ' ', ' ', ' '],
                   ['G', 'T', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'T', 'G', 'G', 'G', 'G', 'T', 'G']]
    # defines platforms for level 2
    level_2_map = [[' ', ' ', 'B', 'B', ' ', 'G', 'G', ' ', ' ', ' ', ' ', 'B', 'G', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', 'G', 'G', 'G', 'G', 'B', ' ', ' ', ' ', ' ', 'G', 'C', 'G', ' ', ' '],
                   ['G', 'G', 'C', 'G', 'B', 'G', 'G', 'C', 'C', 'C', 'G', 'G', 'B', 'B', 'G', 'G', 'C', 'G']]
    # defines platforms for level 3
    level_3_map = [[' ', 'G', ' ', 'C', ' ', 'G', ' '],
                   [' ', 'G', ' ', 'G', ' ', 'G', ' '],
                   ['G', 'B', 'G', 'G', 'B', 'G', 'G']]
    stage_map = [level_1_map, level_2_map, level_3_map]
    stage_layout = [[level_1_platforms, level_1_boxes, level_1_ladders, level_1_powerups],
                    [level_2_platforms, level_2_boxes, level_2_ladders, level_2_powerups],
                    [level_3_platforms, level_3_boxes, level_3_ladders, level_3_powerups]]
    #empties all sprite groups
    for z in stage_layout:
        for tile in z:
            tile.empty()
    #saves last platform x value to check going to next level
    global last_tilex
    last_tilex = [0,0,0]
    level_number = 0
    for stage_level in stage_map:
        tiley = 150
        for layer in stage_level:
            tilex = 0
            for tile in layer:
                global Platform
                if tile != ' ' and tile != 'l':
                    if tiley > 350 and level_number == 0:
                        ground = Platform(tilex, tiley, 220, 64, Platform.sand)
                    else:
                        ground = Platform(tilex, tiley, 220, 64, Platform.woodboard)
                    stage_layout[level_number][0].add(ground)
                    if tile == 'B':
                        box = background_tile(tilex, tiley, 220, 220, background_tile.box)
                        stage_layout[level_number][1].add(box)
                    if tile == 'C':
                        box = background_tile(tilex, tiley, 220, 220, background_tile.crate)
                        stage_layout[level_number][1].add(box)
                    if tile == 'T':
                        tree = background_tile(tilex, tiley - 60, 220, 200, background_tile.tree)
                        stage_layout[level_number][1].add(tree)
                    if tile == 'L':
                        ladder = climbable(tilex, tiley-200, 220, 200, background_tile.box)
                        stage_layout[level_number][2].add(ladder)
                if tile == 'l':
                    ladder = climbable(tilex, tiley-200, 220, 220, background_tile.box)
                    stage_layout[level_number][2].add(ladder)
                tilex += 220
            tiley += 200
        last_tilex[level_number] = tilex - 220
        level_number += 1
    #defines powerups
    extralife = powerup(3020,0,220,220,heart)
    level_1_powerups.add(extralife)
    extralife2 = powerup(200, 200, 220, 220, heart)
    level_3_powerups.add(extralife2)
    # Defines grunts. first 2 values are location, values 3 and 4 are width and height, last value is x value where he turns around
    level_1_enemies.empty()
    grunt = walker(880, 150, 180, 180, (450, 1500))
    grunt2 = walker(1900, 150, 180, 180, (1800, 2200))
    grunt3 = walker(2900, 100, 180, 180, (2600, 3050))
    grunt4 = walker(2800, 350, 180, 180, (2750, 3200))
    seagull = bird(750, 0, 180, 100, (150, 1150))
    seagull2 = bird(2130, 0, 180, 100, (1800, 3000))
    level_1_enemies.add(grunt)
    level_1_enemies.add(grunt2)
    level_1_enemies.add(grunt3)
    level_1_enemies.add(grunt4)
    level_1_enemies.add(seagull)
    level_1_enemies.add(seagull2)
    # Defines level 2 enemies
    level_2_enemies.empty()
    grunt5 = walker(500, 0, 180, 180, (400, 1100))
    grunt6 = walker(1900, 150, 180, 180, (1800, 2200))
    grunt7 = walker(2900, 0, 180, 180, (2800, 3400))
    # Defines gunman. first 2 values are location, last 2 values are width and height
    gunman = shooter(1350, 150, 180, 180)
    seagull3 = bird(800, 0, 180, 100, (250, 1300))
    seagull4 = bird(1900, 0, 180, 100, (1600, 2700))
    level_2_enemies.add(grunt5)
    level_2_enemies.add(grunt6)
    level_2_enemies.add(grunt7)
    level_2_enemies.add(gunman)
    level_2_enemies.add(seagull3)
    level_2_enemies.add(seagull4)
    #defines boss level enemies
    level_3_enemies.empty()
    level_3_enemies.add(captain)
    level_3_enemies.add(parrot)
    # to test if game paused
    global paused
    paused = False
    global reset
    reset = False
    # change your number of starting lives here
    Stitches.lives = 3
    global music
    pygame.mixer.music.stop()
    music = pygame.mixer_music.load("Sounds&Music/Music/Donkey Kong Country King K Rool Theme Song.mp3")
    #music = pygame.mixer_music.load("Sounds&Music/Music/SpongeBob SquarePants Production Music - What Shall We Do with the Drunken Sailor.mp3")
    pygame.mixer.music.play(-1)
    global cutsceneCount
    cutsceneCount = 90
    while True:
        #drawing everything
        # changes background color during gameplay
        win.fill((255, 255, 255))
        # changes background image
        if level < 3:
            win.blit(background, (0 - Stitches.scrollx / 10, 0))
        else:
            win.blit(bossbackground, (0 - Stitches.scrollx / 10, 0))
        # draws skull for boss cutscene
        if (cutsceneCount >= 15 and cutsceneCount < 30) or (
                cutsceneCount > 45 and cutsceneCount < 60) or (
                cutsceneCount > 75 and cutsceneCount < 90):
            win.blit(skull, (500, 200))
        # draws platforms and background objects
        for ground in stage_layout[level-1][0]:
            ground.draw(win)
        for box in stage_layout[level-1][1]:
            box.draw(win)
        for ladder in stage_layout[level-1][2]:
            ladder.draw(win)
        for item in stage_layout[level - 1][3]:
            item.draw(win)
        # lives counter
        if Stitches.lives > 0:
            win.blit(heart, (900, -100))
        else:
            win.blit(emptyheart, (900, -95))
        if Stitches.lives > 1:
            win.blit(heart, (950, -100))
        else:
            win.blit(emptyheart, (950, -95))
        if Stitches.lives > 2:
            win.blit(heart, (1000, -100))
        else:
            win.blit(emptyheart, (1000, -95))
        #draws super jump toggler
        if superjump:
            win.blit(superjumpicon, (0,-100))
            if Stitches.superjumpCount >= 50:
                win.blit(superjumpready, (150, -70))
            else:
                win.blit(superjumppending, (150,-70))
        # defines enemy in each level
        for enemy in stage_enemies[level-1]:
            enemy.draw(win)
        for bullet in bullets:
            bullet.draw(win)
        for enemy_bullet in enemy_bullets:
            enemy_bullet.draw(win)
        for bomb in bombs:
            bomb.draw(win)
        Stitches.draw(win)
        # game ping
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # game paused
        if keys[pygame.K_ESCAPE]:
            pygame.mixer_music.pause()
            pause_menu()
            if reset:
                break
            pygame.mixer_music.unpause()
        # starts boss cutscene
        if level == 3 and Stitches.x > 500 and cutsceneCount == 90:
            pygame.mixer_music.fadeout(500)
            bossLaugh.play()
            cutsceneCount -= 1
        if cutsceneCount >0 and cutsceneCount <90:
            cutsceneCount -= 1
            if cutsceneCount == 0:
                music = pygame.mixer.music.load('Sounds&Music/Music/Pirate Fantasy Music - Rising Sun.mp3')
                pygame.mixer.music.play(-1)
        #captain dies
        if captain.health < 1:
            pygame.mixer_music.fadeout(1000)
        # Player moving to next level at far right of screen
        if Stitches.x >= 1140:
            # if last level, must defeat captain
            if level < 3 or (level == 3 and captain.visible == False):
                level += 1
                Stitches.hitcount = 0
                # resets player position
                Stitches.x = 80
                Stitches.scrollx = 0
            # Game finishes after boss level
            if level > 3:
                break
        #game over
        if Stitches.lives < 1 and Stitches.hitcount < 52:
            break
        pygame.display.update()
    if not(reset):
        game_finished(Stitches)

#creating the pause menu
def pause_menu():
    # defines main menu button
    menu_button = button(400, 500, 105, 45, button.menubutton_up, 340, 423)
    # defines resume button
    resume_button = button(525, 350, 155, 45, button.resumebutton_up, 500, 252)
    # defines quit button
    quit_button = button(700, 500, 105, 45, button.optionsbutton_up, 650, 412)
    global paused
    global game_start
    global reset
    reset = False
    paused = True
    pausecount = 0
    while paused:
        # pause menu background set
        win.fill((255, 0, 0))
        pausecount += 1
        if pausecount > 60:
            pausecount = 0
        if pausecount < 30:
            win.blit(pauseon, (350, 0))
        mousepos = pygame.mouse.get_pos()
        # draws resume button
        resume_button.draw(win)
        if resume_button.isOver(mousepos):
            resume_button.image = button.resumebutton_down
        else:
            resume_button.image = button.resumebutton_up
        # draws main menu button
        menu_button.draw(win)
        if menu_button.isOver(mousepos):
            menu_button.image = button.menubutton_down
        else:
            menu_button.image = button.menubutton_up
        # draws quit button
        quit_button.draw(win)
        if quit_button.isOver(mousepos):
            quit_button.image = button.quitbutton_down
        else:
            quit_button.image = button.quitbutton_up
        clock.tick(60)
        for event in pygame.event.get():
            click = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Checks if mouse over return button and if button clicked, goes to main menu
            if resume_button.isOver(mousepos):
                if click:
                    paused = False
            # Checks if mouse over quit button and if button clicked, game quits
            if quit_button.isOver(mousepos):
                if click:
                    pygame.quit()
                    sys.exit()
            #Checks if mouse over main menu button and if button clicked, goes to main menu
            if menu_button.isOver(mousepos):
                if click:
                    reset = True
                    paused = False
        pygame.display.update()


def game_finished(Stitches):
    # defines main menu button
    menu_button = button(400, 500, 105, 45, button.menubutton_up, 340, 423)
    # defines quit button
    quit_button = button(700, 500, 105, 45, button.optionsbutton_up, 650, 412)
    pygame.mixer_music.stop()
    if Stitches.lives > 0:
        music = pygame.mixer.music.load("Sounds&Music/Music/Super Smash Bros Melee - DK's Victory.mp3")
        pygame.mixer_music.play(1)
    else:
        music = pygame.mixer.music.load("Sounds&Music/Music/Donkey Kong Country Music SNES - Game Over.mp3")
        pygame.mixer_music.play(1)
    # GAMEOVER or Game Finished
    gameover = True
    while gameover:
        mousepos = pygame.mouse.get_pos()
        if Stitches.lives >0:
            win.fill((0, 0, 200))
            # sets victory screen
            win.blit(victory_background, (20, -20))
        else:
            win.fill((255, 0, 0))
            win.blit(game_over_background, (0, 0))
        # draws main menu button
        menu_button.draw(win)
        if menu_button.isOver(mousepos):
            menu_button.image = button.menubutton_down
        else:
            menu_button.image = button.menubutton_up
        # draws quit button
        quit_button.draw(win)
        if quit_button.isOver(mousepos):
            quit_button.image = button.quitbutton_down
        else:
            quit_button.image = button.quitbutton_up
        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            click = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Checks if mouse over quit button and if button clicked, game quits
            if quit_button.isOver(mousepos):
                if click:
                    pygame.quit()
                    sys.exit()
            # Checks if mouse over main menu button and if button clicked, goes to main menu
            if menu_button.isOver(mousepos) and not (instructions):
                if click:
                    gameover = False


"""
MAIN
GAME
 """
level_1_map = []
level_2_map = []
level_3_map = []
level_1_platforms = pygame.sprite.Group()
level_1_boxes = pygame.sprite.Group()
level_1_ladders = pygame.sprite.Group()
level_1_powerups = pygame.sprite.Group()
level_2_platforms = pygame.sprite.Group()
level_2_boxes = pygame.sprite.Group()
level_2_ladders = pygame.sprite.Group()
level_2_powerups = pygame.sprite.Group()
level_3_platforms = pygame.sprite.Group()
level_3_boxes = pygame.sprite.Group()
level_3_ladders = pygame.sprite.Group()
level_3_powerups = pygame.sprite.Group()
stage_map = [level_1_map,level_2_map,level_3_map]
stage_layout = [[level_1_platforms,level_1_boxes,level_1_ladders,level_1_powerups],
                [level_2_platforms,level_2_boxes,level_2_ladders,level_2_powerups],
                [level_3_platforms,level_3_boxes,level_3_ladders,level_3_powerups]]
level_1_enemies = pygame.sprite.Group()
level_2_enemies = pygame.sprite.Group()
level_3_enemies = pygame.sprite.Group()
stage_enemies = [level_1_enemies,level_2_enemies,level_3_enemies]
#Main Loop
while True:
    scrollx = 0
    Stitches = player(80, 150, 180, 180, scrollx)
    captain = boss(1000, 370, 180, 180, (100, 1250))
    parrot = captainbird(1050, 0, 180, 100, (100, 1300))
    # defines bullet lists
    bullets = []
    enemy_bullets = []
    bombs = []
    main_menu()



#when game exited, pygame window shuts off
pygame.quit()
sys.exit()