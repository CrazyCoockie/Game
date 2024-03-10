import pygame

pygame.init()

flscr = 0
widht, height = pygame.display.list_modes()[0][0], pygame.display.list_modes()[0][1]
screen = pygame.display.set_mode((widht, height - flscr))

pixel_x = widht/500
pixel_y = height/250



player_x = 70
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
glavplatform = Platform(0, height-(pixel_y*20), widht, 100)
glavplatform.blockcord()

player_y = glavplatform.y

def provpaltform(x, y, jump_count, jump):
    jump = True
    if jump_count > 0:
        return True, y, jump_count, jump
    for cord in range(len(block)):
        if block[cord][0] <= x <= block[cord][0] + block[cord][2] or block[cord][0] <= x+(pixel_x*17) <= block[cord][0] + block[cord][2]:
            proverka_y = y - (jump_count * abs(jump_count)) * 0.35

            if y <= block[cord][1] and block[cord][1] < proverka_y:
                jump_count = 0
                jump = False
                y = block[cord][1]
                return False, y, jump_count, jump
    return True, y, jump_count, jump



while run:
    platform1 = Platform(0, glavplatform.y-(pixel_y*40), pixel_x*80, pixel_y*10)
    platform1.blockcord()
    platform2 = Platform(platform1.x+(pixel_x*100), platform1.y-(pixel_y*60), pixel_x*80, pixel_y*10)
    platform2.blockcord()
    platform3 = Platform(platform2.x+(pixel_x*150), platform2.y-(pixel_y*40), pixel_x*80, pixel_y*10)
    platform3.blockcord()
    platform4 = Platform(platform3.x+(pixel_x*150), platform3.y-(pixel_y*40), pixel_x*80, pixel_y*10)
    platform4.blockcord()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            quit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] and jump == False: jump_count = pixel_y*2.5; player_y -= 1; jump = True
    if pressed[pygame.K_a]: player_x -= pixel_x*2
    if pressed[pygame.K_d]: player_x += pixel_y*2
    screen.fill((255, 255, 255))

    in_air, player_y, jump_count, jump = provpaltform(player_x, player_y, jump_count, jump)

    if in_air:
        player_y -= (jump_count * abs(jump_count)) * 0.35
        jump_count -= (pixel_y*0.1)

    if player_x < 0:
        player_x = 0
    if player_x + (pixel_x*17) > widht:
        player_x = widht - (pixel_x*17) + 1



    pygame.draw.rect(screen, (40, 162, 255), (player_x, player_y - (pixel_y*37), pixel_x*17, (pixel_y*37)+1))

    platform1.draw()
    platform2.draw()
    platform3.draw()
    platform4.draw()
    glavplatform.draw()

    pygame.display.flip()
    clock.tick(60)
