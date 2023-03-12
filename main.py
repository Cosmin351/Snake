import pygame
import random

class Patrat:
    def __init__(self, pos_x, pos_y, x_speed, y_speed, culoare):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.culoare = culoare
        self.x_speed = x_speed
        self.y_speed = y_speed
    def draw(self, ecran):
        pygame.draw.rect(ecran, self.culoare, [self.pos_x, self.pos_y, 10, 10])

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



pygame.init()
pygame.font.init()

def Intersectie(Obj1, Obj2):
    if (Obj1.pos_x == Obj2.pos_x) and (Obj1.pos_y == Obj2.pos_y):
        return True
    else:
        return False

def SpawnSarpe():
    global Sarpe, Viteza
    Sarpe = []
    x = (random.randint(50, Latime - 80) // 10) * 10
    y = (random.randint(90, Inaltime - 90) // 10) * 10
    Dir = 1
    directie = random.randrange(4)
    if directie == 0:
        Sarpe.append(Patrat(x, y, Viteza, 0, Culoarecap))
        Dir = Viteza * -10
        x += Dir
        for i in range(2):
            Sarpe.append(Patrat(x, y, Viteza, 0, Verde))
            x += Dir
    elif directie == 1:
        Sarpe.append(Patrat(x, y, -Viteza, 0, Culoarecap))
        Dir = Viteza * 10
        x += Dir
        for i in range(2):
            Sarpe.append(Patrat(x, y, -Viteza, 0, Verde))
            x += Dir
    elif directie == 2:
        Sarpe.append(Patrat(x, y, 0, Viteza, Culoarecap))
        Dir = Viteza * -10
        y += Dir
        for i in range(2):
            Sarpe.append(Patrat(x, y, 0, Viteza, Verde))
            y += Dir
    elif directie == 3:
        Sarpe.append(Patrat(x, y, 0, -Viteza, Culoarecap))
        Dir = Viteza * 10
        y += Dir
        for i in range(2):
            Sarpe.append(Patrat(x, y, 0, -Viteza, Verde))
            y += Dir

def Spawn(Fruct, Sarpe):
    while True:
        for patrat in Sarpe:
            if Intersectie(Fruct, patrat):
                Fruct.pos_x = ((random.randint(10, Latime - 10)) // 10) * 10
                Fruct.pos_y = ((random.randint(10, Inaltime - 10)) // 10) * 10
                return False
        return True

def Exitj():
    while True:
        pos = pygame.mouse.get_pos()
        psx = pos[0]
        psy = pos[1]

        Ecran.fill(Negru)
        Endtxt.draw(Ecran, 'Ai pierdut!')
        Endtxt2.draw(Ecran, 'Scor: ' + str(Scor))

        if 455> psx > 405 and 270 < psy < 290:
            Endtxt4.culoare = Albastru2
        else:
            Endtxt4.culoare = Negrudeschis

        if 285 > psx > 190 and 270 < psy < 290:
            Endtxt3.culoare = Albastru2
        else:
            Endtxt3.culoare = Negrudeschis

        pygame.draw.rect(Ecran, Gri, [Endtxt3.posx - 48, Endtxt3.posy - 8,  95, 20])
        pygame.draw.rect(Ecran, Gri, [Endtxt4.posx - 25, Endtxt4.posy - 9.5, 50, 20])
        Endtxt3.draw(Ecran, 'Incearca iar')
        Endtxt4.draw(Ecran, 'Iesire')
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Retry
                if 285 > psx > 190 and 270 < psy < 290:
                    return False
                # Exit
                if 455 > psx > 405 and 270 < psy < 290:
                    return True

# Culori
Verde = (0, 255, 0)
Rosu = (255, 0, 0)
Albastru = (0, 0, 255)
Albastru2 = (100, 100, 255)
Alb = (255, 255, 255)
Negru = (0, 0, 0)
Negrudeschis = (10, 10, 10)
Culoare1 = (50, 50, 50)
Culoarecap = (200, 255, 200)
Gri = (211, 211, 211)

# Ecran
Inaltime = 420
Latime = 720
Ecran = pygame.display.set_mode((Latime, Inaltime))
Ecran.fill(Culoare1)
pygame.display.set_caption('Snake')

# Obiecte

# Text
FontScor = 18
Scortxt = Text(8 + 2 * FontScor // 2, 10, Alb, FontScor)
Scor2txt = Text(35 + 2 * FontScor // 2, 25, Alb, FontScor)
Scor = 0
Scor2 = 0

FontEnd = 25
FontButon = 18
Endtxt = Text(Latime // 2 - 20, (Inaltime- 50) // 2 - FontEnd // 2, Rosu, FontEnd)
Endtxt2 = Text(Latime // 2 - 20, (Inaltime - 50) // 2 + FontEnd // 2, Rosu, FontEnd)
Endtxt3 = Text((Latime // 3), Inaltime - (Inaltime // 3), Negrudeschis, FontButon)
Endtxt4 = Text(Latime - (Latime // 2.5), Inaltime - (Inaltime // 3), Negrudeschis, FontButon)

# Sarpe
Viteza = 1
Sarpe = []
SpawnSarpe()

# Fruct
Fruct = Patrat(((random.randint(10, Latime - 10)) // 10)*10,    ((random.randint(10, Inaltime - 10)) // 10)*10, 0, 0, Rosu)
Spawn(Fruct, Sarpe)

Exit = False
ceas = pygame.time.Clock()

while not Exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and Sarpe[0].x_speed < Viteza:
                Sarpe[0].x_speed = -Viteza
                Sarpe[0].y_speed = 0
            if event.key == pygame.K_RIGHT and Sarpe[0].x_speed > -Viteza:
                Sarpe[0].x_speed = Viteza
                Sarpe[0].y_speed = 0
            if event.key == pygame.K_UP and Sarpe[0].y_speed < Viteza:
                Sarpe[0].x_speed = 0
                Sarpe[0].y_speed = -Viteza
            if event.key == pygame.K_DOWN and Sarpe[0].y_speed > -Viteza:
                Sarpe[0].x_speed = 0
                Sarpe[0].y_speed = Viteza

    # Misca sarpele
    for i in range(10):
        for patrat in Sarpe:
            if patrat.x_speed:
                patrat.pos_x += patrat.x_speed
            if patrat.y_speed:
                patrat.pos_y += patrat.y_speed

    # Verifica daca atinge fructul
    if Intersectie(Fruct, Sarpe[0]):
        Scor += 10
        Spawn(Fruct, Sarpe)
        if Sarpe[len(Sarpe)-1].x_speed == Viteza:
            Sarpe.append(Patrat(Sarpe[len(Sarpe)-1].pos_x - 10, Sarpe[len(Sarpe)-1].pos_y, Viteza, 0, Verde))
        if Sarpe[len(Sarpe)-1].x_speed == -Viteza:
            Sarpe.append(Patrat(Sarpe[len(Sarpe)-1].pos_x + 10, Sarpe[len(Sarpe)-1].pos_y, -Viteza, 0, Verde))
        if Sarpe[len(Sarpe)-1].y_speed == Viteza:
            Sarpe.append(Patrat(Sarpe[len(Sarpe)-1].pos_x, Sarpe[len(Sarpe)-1].pos_y - 10, 0, Viteza, Verde))
        if Sarpe[len(Sarpe)-1].y_speed == -Viteza:
            Sarpe.append(Patrat(Sarpe[len(Sarpe)-1].pos_x, Sarpe[len(Sarpe)-1].pos_y + 10, 0, -Viteza, Verde))

    # Verifica daca lovestti peretele sau sarpele
    for i in range(1, len(Sarpe)-1):
        if Intersectie(Sarpe[0], Sarpe[i]):
            if Exitj():
                Exit = True
                break
            else:
                Scor2 = Scor
                Scor = 0
                SpawnSarpe()
                break
        elif Sarpe[0].pos_x < 0 or Sarpe[0].pos_y < 0 or Sarpe[0].pos_x > Latime or Sarpe[0].pos_y > Inaltime:
            if Exitj():
                Exit = True
                break
            else:
                Scor2 = Scor
                Scor = 0
                SpawnSarpe()
                break

    # Schimba directia
    for i in range(len(Sarpe)-1, 0, -1):
        Sarpe[i].y_speed = Sarpe[i-1].y_speed
        Sarpe[i].x_speed = Sarpe[i-1].x_speed

    # Afiseaza
    Ecran.fill(Culoare1)
    Fruct.draw(Ecran)
    for patrat in Sarpe:
        patrat.draw(Ecran)
    if Scor < 10:
        Scortxt.posx = 9 + 2 * FontScor // 2
        Scortxt.draw(Ecran, 'Scor: ' + str(Scor))
    elif 10 < Scor < 100:
        Scortxt.posx = 11.5 + 2 * FontScor // 2
        Scortxt.draw(Ecran, 'Scor: ' + str(Scor))
    elif Scor <= 1000:
        Scortxt.posx = 16 + 2 * FontScor // 2
        Scortxt.draw(Ecran, 'Scor: ' + str(Scor))
    elif Scor <= 10000:
        Scortxt.posx = 20 + 2 * FontScor // 2
        Scortxt.draw(Ecran, 'Scor: ' + str(Scor))
    if Scor2 < 100 and Scor2:
        Scor2txt.draw(Ecran, 'Scor trecut: ' + str(Scor2))
    elif Scor2 < 1000 and Scor2:
        Scor2txt.posx = 40 + 2 * FontScor // 2
        Scor2txt.draw(Ecran, 'Scor trecut: ' + str(Scor2))
    elif Scor2 < 10000 and Scor2:
        Scor2txt.posx = 43 + 2 * FontScor // 2
        Scor2txt.draw(Ecran, 'Scor trecut: ' + str(Scor2))

    pygame.display.flip()
    ceas.tick(30)

pygame.quit()
