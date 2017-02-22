'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
'''

'''
Samantha Bennefield
2/10/17
Mr. Davis
Pong
'''

import pygame
import sys

listLaser=[]

#Background
spaceshipImg = pygame.image.load('spaceship.png')
spaceImg = pygame.image.load('space.jpg')

background = (0, 0, 0)
entity_color = (255, 255, 255)


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # This makes a rectangle around the entity, used for anything
        # from collision to moving around.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class Spaceship(Entity):
    def __init__(self, x, y, width, height):
        super(Spaceship, self).__init__(x, y, width, height)

        self.image = spaceshipImg


class Player(Spaceship):
    def __init__(self, x, y, width, height):
        super(Player, self).__init__(x, y, width, height)

        # How many pixels the Player Paddle should move on a given frame.
        self.y_change = 0
        # How many pixels the paddle should move each frame a key is pressed.
        self.y_dist = 5

    def MoveKeyDown(self, key):
        if (key == pygame.K_UP):
            self.y_change += -self.y_dist
        elif (key == pygame.K_DOWN):
            self.y_change += self.y_dist
        elif (key == pygame.K_SPACE):
            bullet = Bullet(player.rect.x+90, player.rect.y+59, 10, 10)
            all_sprites_list.add(bullet)
            listLaser.append(bullet)



    def MoveKeyUp(self, key):
        if (key == pygame.K_UP):
            self.y_change += self.y_dist
        elif (key == pygame.K_DOWN):
            self.y_change += -self.y_dist

    def update(self):
        self.rect.move_ip(0, self.y_change)

        #Keep the spaceship on screen
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > window_height - self.height:
            self.rect.y = window_height - self.height


class Asteroid(Entity):
    def __init__(self, x, y, width, height):
        super(Asteroid, self).__init__(x, y, width, height)

        self.image = pygame.Surface([width, height])
        self.image.fill(entity_color)

        self.x_direction = 5

        self.speed = 2

    def update(self):
        self.rect.x-=self.speed
        if self.rect.x <= 0:
            self.kill()


class Bullet(Entity):
    def __init__(self, x, y, width, height):
        super(Bullet, self).__init__(x, y, width, height)

        self.image = pygame.Surface([width, height])
        self.image.fill(entity_color)

        self.x_direction = 1
        self.y_direction = 0

        self.speed = 3

    def update(self):
        self.rect.move_ip(self.speed * self.x_direction,
                          self.speed * self.y_direction)

        if self.rect.x > window_width: #<---If it goes off the screen
            self.kill()


pygame.init()

BLACK = (0, 0, 0)

window_width = 700
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Asteroids")

clock = pygame.time.Clock()

player = Player(20, window_height / 2, 20, 50)
asteroid = Asteroid(window_width - 40, window_height / 2, 30, 30)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
all_sprites_list.add(asteroid)


def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True

    return False

def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

#Game Loop
while True:
    # Event processing here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            player.MoveKeyDown(event.key)
        elif event.type == pygame.KEYUP:
            player.MoveKeyUp(event.key)

    for ent in all_sprites_list:



        ent.update()




    screen.fill(BLACK)
    screen.blit(spaceImg, (200, 200))
    '''screen.blit(textSurfaceObj1, textRectObj1)
    screen.blit(textSurfaceObj2, textRectObj2)'''

    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)