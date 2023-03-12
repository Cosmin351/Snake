import pygame

pygame.font.init()


class Text:
    def __init__(self, posx, posy, culoare, marime):
        self.posx = posx
        self.posy = posy
        self.culoare = culoare
        self.Font = pygame.font.SysFont('timesnewroman', marime)
    def draw(self, ecran, text):
        txt = self.Font.render(text, True, self.culoare)
        txtrect = txt.get_rect()
        txtrect.center = (self.posx, self.posy)
        ecran.blit(txt, txtrect)