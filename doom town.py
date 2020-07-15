import pygame
import random

pygame.init()
live1 = 100  # vida inicial player 1
live2 = 100  # vida inicial player 2

# colores basicos para futuro uso
blanco = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

listamenu = [0] # inicio de la lista menu que se usara para ek control de las opciones del menu .

screen = pygame.display.set_mode((1000, 575)) # se establece el size de la pantalla
pygame.display.set_caption("Prototipo I")

fuente = pygame.font.Font(None, 40) # fuente 1
fuente1 = pygame.font.Font(None, 80) # fuente 2

# Textos que se usaran en el futuro
t1 = fuente.render("mapa", 0, (blanco))
t2 = fuente.render("music", 0, (blanco))
t3 = fuente.render("p1", 0, (blanco))
t4 = fuente.render("p2", 0, (blanco))
t5 = fuente1.render("DOOM TOWN", 0, (blanco))
t6 = fuente.render("1.street", 0, (blanco))
t7 = fuente.render("2.desierto", 0, (blanco))
t8 = fuente.render("3.oriente", 0, (blanco))
t9 = fuente.render("4.futuro", 0, (blanco))
tt1 = fuente1.render("MAPA", 0, (blanco))
t10 = fuente.render("1. Robot", 0, (blanco))
t11 = fuente.render("2. Ninja", 0, (blanco))
t12 = fuente.render("3. Aventurera", 0, (blanco))
t13 = fuente.render ("1. Big Division", 0, (blanco))
t14 = fuente.render ("2. pelea con musica de Linking Park", 0, (blanco))

reloj = pygame.time.Clock()# reloj del juego

n = random.randint(0, 5) # variable para el fondo al azar del menu

# Imagenes de los botones
B1 = pygame.image.load("B2.png")
B1 = pygame.transform.scale(B1, (150, 75))
B2 = pygame.image.load("B2.png")
B2 = pygame.transform.scale(B2, (150, 75))
B3 = pygame.image.load("B2.png")
B3 = pygame.transform.scale(B3, (150, 75))
B4 = pygame.image.load("B2.png")
B4 = pygame.transform.scale(B4, (150, 75))
B5 = pygame.image.load("B1.jpg")
B5 = pygame.transform.scale(B5, (150, 75))

#musica del juego
pygame.mixer.music.load ("bigdivision.mp3")
sonido_golpe = pygame.mixer.Sound ("punch.wav")
doom_eternal = pygame.mixer.Sound ("bigdivision.wav")
lkp = pygame.mixer.Sound ("lkp.wav")
soundtrack =    doom_eternal


#imagenes del menu
menu1 = pygame.image.load("menu6.jpg")
menu2 = pygame.image.load("MENU.gif")
menu3 = pygame.image.load("MENU2.PNG")
menu4 = pygame.image.load("bg7.jpg")
menu5 = pygame.image.load("menu5.jpg")
menu6 = pygame.image.load("menu3.jpg")
menus = [menu1, menu2, menu3, menu4, menu5, menu6] #lista con todas las imagenes del menu
menu = menus[n] # variable que es una de las imagenes de la lista menus escogida al azar
menu = pygame.transform.scale(menu, (1000, 575)) # se escala la imagen del menu

# Fondos del juego (en el campo de batalla)
bg1 = pygame.image.load("bg1.jpg")
bg1 = pygame.transform.scale(bg1, (1000, 575))
bg3 = pygame.image.load("bg2.jpg")
bg3 = pygame.transform.scale(bg3, (1000, 575))
bg2 = pygame.image.load("bg.jpg")
bg2 = pygame.transform.scale(bg2, (1000, 575))
bg4 = pygame.image.load("bg3.jpg")
bg4 = pygame.transform.scale(bg3, (1000, 575))
bg5 = pygame.image.load("bg4.gif")
bg5 = pygame.transform.scale(bg4, (1000, 575))
bg6 = pygame.image.load("bg6.jpg")
bg6 = pygame.transform.scale(bg6, (1000, 575))
bg7 = pygame.image.load("bg5.jpg")
bg7 = pygame.transform.scale(bg7, (1000, 575))


def escalar(r):  #funcion para escalar las sprites
    return pygame.transform.scale(r, (100, 100))

#variable d sprite de  camianr a la derecha
walkRight = [escalar(pygame.image.load('Run (1).png')), escalar(pygame.image.load('Run (2).png')),
             escalar(pygame.image.load('Run (3).png')), escalar(pygame.image.load('Run (4).png')),
             escalar(pygame.image.load('Run (5).png')), escalar(pygame.image.load('Run (6).png')),
             escalar(pygame.image.load('Run (7).png')), escalar(pygame.image.load('Run (8).png')),
             escalar(pygame.image.load('Run (8).png'))]
# Variable de sprite de camniar a la izquierda
walkLeft = [escalar(pygame.image.load('LRun (1).png')), escalar(pygame.image.load('LRun (2).png')),
            escalar(pygame.image.load('LRun (3).png')), escalar(pygame.image.load('LRun (4).png')),
            escalar(pygame.image.load('LRun (5).png')), escalar(pygame.image.load('LRun (6).png')),
            escalar(pygame.image.load('LRun (7).png')), escalar(pygame.image.load('LRun (8).png')),
            escalar(pygame.image.load('LRun (8).png'))]
ataque_p1 = [escalar(pygame.image.load('Melee (1).png')), escalar(pygame.image.load('Melee (2).png')),
            escalar(pygame.image.load('Melee (3).png')), escalar(pygame.image.load('Melee (4).png')),
            escalar(pygame.image.load('Melee (5).png')), escalar(pygame.image.load('Melee (6).png')),
            escalar(pygame.image.load('Melee (7).png')), escalar(pygame.image.load('Melee (8).png')),
            escalar(pygame.image.load('Melee (8).png'))]
bg = bg5 #se establece fono por defecto del juego (campo de combate)
char = escalar(pygame.image.load('Melee (1).png'))  #varible de iamgen al estar parado

walkRight2 = [escalar(pygame.image.load('rRun (1).png')), escalar(pygame.image.load('rRun (2).png')),
             escalar(pygame.image.load('rRun (3).png')), escalar(pygame.image.load('rRun (4).png')),
             escalar(pygame.image.load('rRun (5).png')), escalar(pygame.image.load('rRun (6).png')),
             escalar(pygame.image.load('rRun (7).png')), escalar(pygame.image.load('rRun (8).png')),
             escalar(pygame.image.load('rRun (8).png'))]
# Variable de sprite de camniar a la izquierda
walkLeft2 = [escalar(pygame.image.load('LrRun (1).png')), escalar(pygame.image.load('LrRun (2).png')),
            escalar(pygame.image.load('LrRun (3).png')), escalar(pygame.image.load('LrRun (4).png')),
            escalar(pygame.image.load('LrRun (5).png')), escalar(pygame.image.load('LrRun (6).png')),
            escalar(pygame.image.load('LrRun (6).png')), escalar(pygame.image.load('LrRun (7).png')),
            escalar(pygame.image.load('LrRun (7).png'))]
ataque_p2 = [escalar(pygame.image.load('2mMelee (1).png')), escalar(pygame.image.load('2mMelee (2).png')),
            escalar(pygame.image.load('2mMelee (3).png')), escalar(pygame.image.load('2mMelee (4).png')),
            escalar(pygame.image.load('2mMelee (5).png')), escalar(pygame.image.load('2mMelee (6).png')),
            escalar(pygame.image.load('2mMelee (6).png')), escalar(pygame.image.load('2mMelee (7).png')),
            escalar(pygame.image.load('2mMelee (7).png'))]
char2 = escalar(pygame.image.load('mMelee (1).png'))  #varible de iamgen al estar parado




# Sprites de Ninja
DerechaNinja = [escalar(pygame.image.load('Run__000.png')), escalar(pygame.image.load('Run__001.png')),
            escalar(pygame.image.load('Run__002.png')), escalar(pygame.image.load('Run__003.png')),
            escalar(pygame.image.load('Run__003.png')), escalar(pygame.image.load('Run__005.png')),
            escalar(pygame.image.load('Run__004.png')), escalar(pygame.image.load('Run__007.png')),
            escalar(pygame.image.load('Run__008.png'))]

IzquierdaNinja =[escalar(pygame.image.load('LRun__000.png')), escalar(pygame.image.load('LRun__001.png')),
            escalar(pygame.image.load('LRun__002.png')), escalar(pygame.image.load('LRun__003.png')),
            escalar(pygame.image.load('LRun__003.png')), escalar(pygame.image.load('LRun__005.png')),
            escalar(pygame.image.load('LRun__004.png')), escalar(pygame.image.load('LRun__007.png')),
            escalar(pygame.image.load('LRun__008.png'))]

AtaqueNinjap2 = [escalar(pygame.image.load('Attack__000.png')), escalar(pygame.image.load('Attack__001.png')),
            escalar(pygame.image.load('Attack__002.png')), escalar(pygame.image.load('Attack__003.png')),
            escalar(pygame.image.load('Attack__004.png')), escalar(pygame.image.load('Attack__005.png')),
            escalar(pygame.image.load('Attack__006.png')), escalar(pygame.image.load('Attack__007.png')),
            escalar(pygame.image.load('Attack__008.png'))]

AtaqueNinjap1 = [escalar(pygame.image.load('2Attack__000.png')), escalar(pygame.image.load('2Attack__001.png')),
            escalar(pygame.image.load('2Attack__002.png')), escalar(pygame.image.load('2Attack__003.png')),
            escalar(pygame.image.load('2Attack__004.png')), escalar(pygame.image.load('2Attack__005.png')),
            escalar(pygame.image.load('2Attack__006.png')), escalar(pygame.image.load('2Attack__007.png')),
            escalar(pygame.image.load('2Attack__008.png'))]

standNinja = escalar(pygame.image.load('Attack__000.png'))

#Sprites de Robots
DerechaRobot =[escalar(pygame.image.load('Run (1).png')), escalar(pygame.image.load('Run (2).png')),
             escalar(pygame.image.load('Run (3).png')), escalar(pygame.image.load('Run (4).png')),
             escalar(pygame.image.load('Run (5).png')), escalar(pygame.image.load('Run (6).png')),
             escalar(pygame.image.load('Run (7).png')), escalar(pygame.image.load('Run (8).png')),
             escalar(pygame.image.load('Run (8).png'))]

IzquierdaRobot = [escalar(pygame.image.load('LRun (1).png')), escalar(pygame.image.load('LRun (2).png')),
            escalar(pygame.image.load('LRun (3).png')), escalar(pygame.image.load('LRun (4).png')),
            escalar(pygame.image.load('LRun (5).png')), escalar(pygame.image.load('LRun (6).png')),
            escalar(pygame.image.load('LRun (7).png')), escalar(pygame.image.load('LRun (8).png')),
            escalar(pygame.image.load('LRun (8).png'))]

ataqueRobotp1 = [escalar(pygame.image.load('Melee (1).png')), escalar(pygame.image.load('Melee (2).png')),
            escalar(pygame.image.load('Melee (3).png')), escalar(pygame.image.load('Melee (4).png')),
            escalar(pygame.image.load('Melee (5).png')), escalar(pygame.image.load('Melee (6).png')),
            escalar(pygame.image.load('Melee (7).png')), escalar(pygame.image.load('Melee (8).png')),
            escalar(pygame.image.load('Melee (8).png'))]

ataqueRobotp2 = [escalar(pygame.image.load('2Melee (1).png')), escalar(pygame.image.load('2Melee (2).png')),
            escalar(pygame.image.load('2Melee (3).png')), escalar(pygame.image.load('2Melee (4).png')),
            escalar(pygame.image.load('2Melee (5).png')), escalar(pygame.image.load('2Melee (6).png')),
            escalar(pygame.image.load('2Melee (7).png')), escalar(pygame.image.load('2Melee (8).png')),
            escalar(pygame.image.load('2Melee (8).png'))]

standRobot = escalar(pygame.image.load('2Melee (1).png'))

#Sprties aventurera
DerechaAventura =  [escalar(pygame.image.load('rRun (1).png')), escalar(pygame.image.load('rRun (2).png')),
             escalar(pygame.image.load('rRun (3).png')), escalar(pygame.image.load('rRun (4).png')),
             escalar(pygame.image.load('rRun (5).png')), escalar(pygame.image.load('rRun (6).png')),
             escalar(pygame.image.load('rRun (7).png')), escalar(pygame.image.load('rRun (8).png')),
             escalar(pygame.image.load('rRun (8).png'))]

IzquierdaAventura = [escalar(pygame.image.load('LrRun (1).png')), escalar(pygame.image.load('LrRun (2).png')),
            escalar(pygame.image.load('LrRun (3).png')), escalar(pygame.image.load('LrRun (4).png')),
            escalar(pygame.image.load('LrRun (5).png')), escalar(pygame.image.load('LrRun (6).png')),
            escalar(pygame.image.load('LrRun (6).png')), escalar(pygame.image.load('LrRun (7).png')),
            escalar(pygame.image.load('LrRun (7).png'))]

ataqueAventurap1 = [escalar(pygame.image.load('mMelee (1).png')), escalar(pygame.image.load('mMelee (2).png')),
            escalar(pygame.image.load('mMelee (3).png')), escalar(pygame.image.load('mMelee (4).png')),
            escalar(pygame.image.load('mMelee (5).png')), escalar(pygame.image.load('mMelee (6).png')),
            escalar(pygame.image.load('mMelee (6).png')), escalar(pygame.image.load('mMelee (7).png')),
            escalar(pygame.image.load('mMelee (7).png'))]

ataqueAventurap2 = [escalar(pygame.image.load('2mMelee (1).png')), escalar(pygame.image.load('2mMelee (2).png')),
            escalar(pygame.image.load('2mMelee (3).png')), escalar(pygame.image.load('2mMelee (4).png')),
            escalar(pygame.image.load('2mMelee (5).png')), escalar(pygame.image.load('2mMelee (6).png')),
            escalar(pygame.image.load('2mMelee (6).png')), escalar(pygame.image.load('2mMelee (7).png')),
            escalar(pygame.image.load('2mMelee (7).png'))]

standAventura = escalar(pygame.image.load('mMelee (1).png'))
cal = 0 #variable de calculo
pygame.display.flip()
game = True  #variable del juego, cuando es false el juego se detiene
factor = True # factor true para mostrar el menu principal
mecha = False # variable true para mostrar el campo de batalla
#coordenadas del player 1 (p1)
x = 2000
y = 1000

vel = 10 #velocicad (v1)
salto = False #variable para activar salto
csalto = 10 #oonstante de longitud de salto
derecha = False #variable para activar caminar a dereha
izquierda = False  #variable para activar caminar a izquierda
cwalk = 0 #constante de caminata
atacar_p1 = False #variable para habilitar ataque de p1
constante_ataquep1=0 #constante de incio de ataque p1

#variables de player 2
x_player2 = 2000
y_player2 = 1000

velocidad2=10
salto_player2 = False
constante_salto_player2 = 10
derecha_palyer2 = False
izquierda_player2 = False
constante_caminar_player2 = 0
atacar_p2 = False #variable para habilitar ataque de p1
constante_ataquep2=0 #constante de incio de ataque p1


def funcion(x): #funcion para recolectar el ultimo ajuste elegido y activar su respectiva ventana.
    A = listamenu[len(listamenu) - 1]
    return A


def acciones_p1():  # calculo que hacen posibles el moviemiento del p1
    global cwalk
    global constante_ataquep1
    if mecha == True:
        screen.fill((0, 0, 0, 0))
        screen.blit(bg, (0, 0))

    if cwalk >= 27:
        cwalk = 0

    if izquierda:
        screen.blit(walkLeft[cwalk // 3], (x, y))
        cwalk += 1

    elif derecha:
        screen.blit(walkRight[cwalk // 3], (x, y))
        cwalk += 1

    elif  atacar_p1:
        screen.blit(ataque_p1[constante_ataquep1 // 3], (x, y))
        sonido_golpe.play()

    else:
        screen.blit(char, (x, y))
        cwalk = 0

    pygame.display.update()

def acciones_p2():  # calculo que hacen posibles el moviemiento del p2
    global constante_caminar_player2

    if constante_caminar_player2 >= 27:
        constante_caminar_player2  = 0

    if izquierda_player2:
        screen.blit(walkLeft2[constante_caminar_player2  // 3], (x_player2, y_player2))
        constante_caminar_player2  += 1

    elif derecha_palyer2:
        screen.blit(walkRight2[constante_caminar_player2  // 3], (x_player2, y_player2))
        constante_caminar_player2  += 1

    elif  atacar_p2:
        screen.blit(ataque_p2[constante_ataquep2 // 3], (x_player2, y_player2))
        sonido_golpe.play()

    else:
        screen.blit(char2, (x_player2, y_player2))
        constante_caminar_player2  = 0

    pygame.display.update()


def accionmenu(x):   # acciones que se puede hacer en cada ajuste
    global teclas
    global bg
    global  walkRight
    global walkLeft
    global walkRight2
    global walkLeft2
    global ataque_p1
    global ataque_p2
    global char
    global char2
    global soundtrack

    if x == 1: #cuando se elije el menu de fondos, botones para elegir el fondo
        if teclas[pygame.K_1]:
            bg = bg1

        if teclas[pygame.K_2]:
            bg = bg2

        if teclas[pygame.K_3]:
            bg = bg3

        if teclas[pygame.K_4]:
            bg = bg4

        if teclas[pygame.K_5]:
            bg = bg5

        if teclas[pygame.K_6]:
            bg = bg6

        if teclas[pygame.K_7]:
            bg = bg7

    if x == 3: #selecion de sprites p1
        if teclas[pygame.K_1]:
            walkRight = DerechaRobot
            walkLeft = IzquierdaRobot
            ataque_p1 = ataqueRobotp1
            char = standRobot
            print("ROBOTO")

        if teclas[pygame.K_2]:
            walkRight = DerechaNinja
            walkLeft = IzquierdaNinja
            ataque_p1 = AtaqueNinjap1
            char = standNinja
            print("NINJA")

        if teclas[pygame.K_3]:
            walkRight = DerechaAventura
            walkLeft = IzquierdaAventura
            ataque_p1 = ataqueAventurap1
            char = standAventura
            print("AVEN")

    if x==4: #selecion de sprites p2
        if teclas[pygame.K_1]:
            walkRight2 = DerechaRobot
            walkLeft2 = IzquierdaRobot
            ataque_p2 = ataqueRobotp2
            char2 = standRobot

        if teclas[pygame.K_2]:
            walkRight2 = DerechaNinja
            walkLeft2 = IzquierdaNinja
            ataque_p2 = AtaqueNinjap2
            char2 = standNinja

        if teclas[pygame.K_3]:
            walkRight2 = DerechaAventura
            walkLeft2 = IzquierdaAventura
            ataque_p2 = ataqueAventurap2
            char2 = standAventura

    if x==2:
        if teclas[pygame.K_1]:
            soundtrack = doom_eternal

        if teclas[pygame.K_2]:
            soundtrack = lkp


pygame.mixer.music.play()
while game: #bucle principal

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    vmenu = funcion(listamenu) #variable que obtiene la ultima accion del menu principal para abrir ventana de cada ajsute

    evento = pygame.mouse.get_pressed() #mouse presionado
    pos = pygame.mouse.get_pos() #posicion en eje de coordenadas del mouse
    reloj.tick(27)
    pygame.display.update()

    teclas = pygame.key.get_pressed() #tecla presionada
    # print (pos)

    if teclas[pygame.K_p]:
        game = False

    if teclas[pygame.K_0]: # si presiona sero activa menu principal
        factor = True
        x = 2000
        y = 1000
        mecha = False
        listamenu.append(0)

    accionmenu(vmenu)

    if factor == True: #menu principal odnde se encuentran botones controlados por click
        screen.blit(menu, (0, 0))
        screen.blit(B1, (200, 250))
        screen.blit(B2, (350, 250))
        screen.blit(B3, (500, 250))
        screen.blit(B4, (650, 250))
        screen.blit(B5, (430, 400))
        screen.blit(t1, (235, 270))
        screen.blit(t2, (385, 270))
        screen.blit(t3, (555, 270))
        screen.blit(t4, (705, 270))
        screen.blit(t5, (350, 70))

        if evento[0]: # eventos de click presionafdos y acciones de cada boton
            if pos[0] >= (230) and pos[1] >= (250) and pos[0] <= (311) and pos[1] <= 307:
                factor = False
                print(" haciendo click 1")
                #display de ventana de ajuste elegido
                screen.fill((0, 0, 0, 0))
                screen.blit(menu, (0, 0))
                screen.blit(tt1, (400, 100))
                screen.blit(t6, (300, 200))
                screen.blit(t7, (300, 300))
                screen.blit(t8, (300, 400))
                screen.blit(t9, (300, 500))
                listamenu.append(1)

            if pos[0] >= (382) and pos[1] >= (250) and pos[0] <= (460) and pos[1] <= 307:
                factor = False
                # display de ventana de ajuste elegido (musica)
                listamenu.append(2)
                screen.fill((0, 0, 0, 0))
                screen.blit(menu, (0, 0))
                screen.blit(t2, (300, 100))
                screen.blit(t13, (300, 400))
                screen.blit(t14, (300, 500))
                listamenu.append(2)

            if pos[0] >= (532) and pos[1] >= (255) and pos[0] <= (610) and pos[1] <= 307:
                factor = False

                listamenu.append(3)
                # display de ventana de ajuste elegido (p3)
                screen.fill((0, 0, 0, 0))
                screen.blit(menu, (0, 0))
                screen.blit(t3, (300, 100))
                screen.blit(t10, (300, 200))
                screen.blit(t11, (300, 300))
                screen.blit(t12, (300, 400))
                listamenu.append(3)

            if pos[0] >= (682) and pos[1] >= (250) and pos[0] <= (760) and pos[1] <= 307:
                factor = False

                listamenu.append(4)
                # display de ventana de ajuste elegido (p2)
                screen.fill((0, 0, 0, 0))
                screen.blit(menu, (0, 0))
                screen.blit(t4, (300, 100))
                screen.blit(t10, (300, 200))
                screen.blit(t11, (300, 300))
                screen.blit(t12, (300, 400))
                print(listamenu)

            if pos[0] >= (430) and pos[1] >= (400) and pos[0] <= (580) and pos[1] <= 474:
                factor = False
                listamenu.append(0)
                # Se activa la pantalla de combate
                print(" haciendo click 5")
                pygame.mixer.music.stop()
                soundtrack.play()
                screen.fill((0, 0, 0, 0))
                screen.blit(bg, (0, 0))
                mecha = True
                x = 250
                y = 490
                x_player2 = 700
                y_player2 = 490

    #condicionales del movimiento del p1
    if teclas[pygame.K_LEFT] and x > vel:
        x -= vel
        izquierda = True
        derecha = False
    elif teclas[pygame.K_RIGHT] and x < 940 - vel:
        x += vel
        izquierda = False
        derecha = True
    else:
        derecha = False
        izquierda = False
        cwalk = 0

    if not salto:
        if teclas[pygame.K_SPACE]:
            salto = True

    else:
        if csalto >= -10:
            sign = 1
            if csalto < 0:
                sign = -1
            y -= (csalto ** 2) * 0.5 * sign
            csalto -= 1
        else:
            salto = False
            csalto = 10
    if not atacar_p1:
        if teclas[pygame.K_m]:
            atacar_p1= True

    else:
        derecha = False
        izquierda = False
        if constante_ataquep1>=0:
            if constante_ataquep1 <26:
                constante_ataquep1 += 1

            else:
                constante_ataquep1=10
                atacar_p1 = False


    # condicionales del movimiento del p2
    if teclas[pygame.K_a] and x_player2 > velocidad2:
            x_player2 -= velocidad2
            izquierda_player2 = True
            derecha_palyer2 = False
    elif teclas[pygame.K_d] and x_player2 < 940 - velocidad2:
            x_player2 += velocidad2
            izquierda_player2 = False
            derecha_palyer2 = True
    else:
            derecha_palyer2 = False
            izquierda_player2 = False
            constante_caminar_player2 = 0

    if not salto_player2:
        if teclas[pygame.K_v]:
                salto_player2 = True

    else:
            if constante_salto_player2>= -10:
                signo = 1
                if constante_salto_player2 < 0:
                    signo = -1
                y_player2 -= (constante_salto_player2 ** 2) * 0.5 * signo
                constante_salto_player2 -= 1
            else:
                salto_player2 = False
                constante_salto_player2 = 10

    if not atacar_p2:
        if teclas[pygame.K_c]:
            atacar_p2= True

    else:
        derecha_palyer2 = False
        izquierda_player2 = False
        if constante_ataquep2 >= 0:
            if constante_ataquep2 <26:
                constante_ataquep2 += 1

            else:
                constante_ataquep2 = 10
                atacar_p2 = False
    #programacion de colison y ataque con vida
    if atacar_p1==True and x < x_player2 <= (x+100):
        live2 -= 20
        x_player2 += 20

    if atacar_p2==True and (x_player2-100)<= x <x_player2:
        live2 -= 20
        x -=20

    #cerrar el juego al perder
    if live2<=0 or live1<=0:
        game = False


    print(f"Vida p1 : {live1}")
    print(f"Vida p2 : {live2}")
    acciones_p1()
    acciones_p2()
    pygame.display.update()

pygame.quit()
