import random
import pygame as pg

class Sprite:
    def __init__(self, sheet, pos, area, name):
        self._sheet = sheet
        self._pos = pos
        self._area = area
        self._name = name

    @property
    def bounds(self):
        x, y = self._pos
        w, h = self._area[2:]
        return x, y, w, h

    def move(self, dpos):
        x, y = self._pos
        dx, dy = dpos
        self._pos = x + dx, y + dy

    def haspoint(self, pos):
        px, py = pos
        x, y, w, h = self.bounds
        return x <= px < x+w and y <= py < y+h
        # return pg.Rect(*self.bounds).collidepoint(pos)

    def render(self, screen):
        screen.blit(self._sheet, self._pos, self._area)
    
    @property
    def name(self):
        return self._name
    
if __name__ == '__main__':
    pg.init()
    pg.display.set_caption("Rock Paper Scissor")
    screen = pg.display.set_mode((800, 600))

    width = 150
    def sprite_x(n):
        margin = 6
        offset = 10
        return margin + offset + (width + offset) * n

    # initialize
    sprite_sheet = pg.image.load('gfx/rsp.png')
    sprite_sheet.set_colorkey((255, 254, 254)) # (r, g, b) 0-255

    sprites = [
        Sprite(sprite_sheet, (  0,   0), (sprite_x(0), 29, width, width), 'rock'),
        Sprite(sprite_sheet, (200,   0), (sprite_x(1), 29, width, width), 'paper'),
        Sprite(sprite_sheet, (  0, 200), (sprite_x(2), 29, width, width), 'scissor'),
        Sprite(sprite_sheet, (200, 200), (sprite_x(3), 29, width, width), 'lizard'),
        Sprite(sprite_sheet, (400,   0), (sprite_x(4), 29, width, width), 'spock'),
    ]

    player_choice = None

    running = True
    last_ticks = None
    while running:
        # process input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if player_choice is None:
                    hits = [s.name for s in sprites if s.haspoint(event.pos)]
                    did_hit = False
                    for hit in hits:
                        player_choice = hit
                        did_hit = True
                        print(hit)

                        computer_choice = random.choice(['rock', 'paper', 'scissor', 'lizard', 'spock'])
                        print(computer_choice)
                        # Logikk
                        # print resultat

                        break
                    if not did_hit:
                        print('Try to aim better')

        ticks = pg.time.get_ticks()
        delta_time = 0 if last_ticks is None else ticks - last_ticks
        last_ticks = ticks

        # update
        # sprites[0].move((delta_time/100, 0))
        # if pg.time.get_ticks() % 1000 < 10:
        #     print(player_choice)

        # render
        screen.fill((240, 240, 240))
        for s in sprites:
            s.render(screen)

        pg.display.flip()