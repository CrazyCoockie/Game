import pygame

pygame.init()

flscr = 70
widht, height = pygame.display.list_modes()[0][0], pygame.display.list_modes()[0][1]
screen = pygame.display.set_mode((widht, height - flscr))

player_x = flscr
player_y = height - 100
run = True
clock = pygame.time.Clock()
jump = False
jump_count = 0
block = []
ground = False
in_air = False


class Platform:
    def __init__(self, x, y, widht, height):
        self.x = x
        self.y = y
        self.width = widht
        self.height = height
        self.color = (0, 0, 0)

    def blockcord(self):
        block.append([self.x, self.y, self.width, self.height])

    def draw(self):
        pl = pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def collision(self, x, y):
        pass


def provpaltform(x, y, jump_count):
    if jump_count > 0:
        return True, y, jump_count
    for cord in range(len(block)):
        if block[cord][0] < x < block[cord][0] + block[cord][2] and block[cord][1] < y < block[cord][1] + block[cord][3]:
            proverka_y = block[cord][1]
            if proverka_y <= y <= proverka_y + 10:
                jump_count = 0
                return False, y, jump_count
            elif proverka_y < y:
                return True, y, jump_count
    return True, y, jump_count



while run:
    platform1 = Platform(0, height - 200, 300, 50)
    platform1.blockcord()
    platform2 = Platform(300, height - 400, 300, 50)
    platform2.blockcord()
    platform3 = Platform(500, height - 600, 300, 50)
    platform3.blockcord()
    platform4 = Platform(800, height - 800, 300, 50)
    platform4.blockcord()
    glavplatform = Platform(0, height-100, widht, 100)
    glavplatform.blockcord()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            quit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]: jump_count = 9; player_y -= 1
    if pressed[pygame.K_a]: player_x -= 7
    if pressed[pygame.K_d]: player_x += 7
    screen.fill((255, 255, 255))

    in_air, player_y, jump_count = provpaltform(player_x, player_y, jump_count)

    if in_air:
        player_y -= jump_count
        jump_count -= 0.25


    pygame.draw.rect(screen, (40, 162, 255), (player_x, player_y - 120, 60, 120))

    platform1.draw()
    platform2.draw()
    platform3.draw()
    platform4.draw()
    glavplatform.draw()

    pygame.display.flip()
    clock.tick(60)
