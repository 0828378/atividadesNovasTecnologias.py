# =========================================
# NIVEL 1
# =========================================
import pygame, sys, random

pygame.init()
TELA = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Nivel 1")
CLOCK = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial", 28)

class Entidade:
    def __init__(self, x, y, w, h, cor):
        self.rect = pygame.Rect(x, y, w, h)
        self.cor = cor

    def desenhar(self):
        pygame.draw.rect(TELA, self.cor, self.rect)

class Jogador(Entidade):
    def __init__(self):
        super().__init__(375, 275, 50, 50, (0,150,255))
        self.vel = 5

    def mover(self, t):
        if t[pygame.K_LEFT] and self.rect.x > 0: self.rect.x -= self.vel
        if t[pygame.K_RIGHT] and self.rect.x < 750: self.rect.x += self.vel
        if t[pygame.K_UP] and self.rect.y > 0: self.rect.y -= self.vel
        if t[pygame.K_DOWN] and self.rect.y < 550: self.rect.y += self.vel

class Inimigo(Entidade):
    def __init__(self):
        super().__init__(random.randint(0,750),0,40,40,(255,165,0))
        self.vel = random.randint(2,4)

    def mover(self, j):
        if self.rect.x < j.rect.x: self.rect.x += self.vel
        if self.rect.x > j.rect.x: self.rect.x -= self.vel
        if self.rect.y < j.rect.y: self.rect.y += self.vel
        if self.rect.y > j.rect.y: self.rect.y -= self.vel

j = Jogador()
inimigos = [Inimigo() for _ in range(4)]
vidas = 5
pontos = 0

ultimo_dano = 0
cooldown = 1000

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    t = pygame.key.get_pressed()
    j.mover(t)

    for ini in inimigos:
        ini.mover(j)
        if ini.rect.colliderect(j.rect):
            agora = pygame.time.get_ticks()
            if agora - ultimo_dano > cooldown:
                vidas -= 1
                ultimo_dano = agora
                ini.rect.topleft = (random.randint(0,750),0)

    if vidas <= 0:
        break

    pontos += 1

    TELA.fill((20,20,40))
    j.desenhar()

    for ini in inimigos:
        ini.desenhar()

    txt = fonte.render(f"Vidas: {vidas} | Pontos: {pontos}", True, (255,255,255))
    TELA.blit(txt,(10,10))

    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()


# =========================================
# NIVEL 2
# =========================================
import pygame, sys, random

pygame.init()
TELA = pygame.display.set_mode((800, 600))
CLOCK = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial", 28)

class Jogador:
    def __init__(self):
        self.rect = pygame.Rect(375,275,50,50)
        self.vel = 5

    def mover(self,t):
        if t[pygame.K_LEFT] and self.rect.x > 0: self.rect.x -= self.vel
        if t[pygame.K_RIGHT] and self.rect.x < 750: self.rect.x += self.vel
        if t[pygame.K_UP] and self.rect.y > 0: self.rect.y -= self.vel
        if t[pygame.K_DOWN] and self.rect.y < 550: self.rect.y += self.vel

    def draw(self):
        pygame.draw.rect(TELA,(0,150,255),self.rect)

class Inimigo:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0,750),0,40,40)
        self.vel = 3
        self.vida = 3

    def mover(self,j):
        if self.rect.x < j.rect.x: self.rect.x += self.vel
        if self.rect.x > j.rect.x: self.rect.x -= self.vel
        if self.rect.y < j.rect.y: self.rect.y += self.vel
        if self.rect.y > j.rect.y: self.rect.y -= self.vel

    def draw(self):
        pygame.draw.rect(TELA,(255,165,0),self.rect)

class Tiro:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,10,10)

    def mover(self):
        self.rect.y -= 7

    def draw(self):
        pygame.draw.rect(TELA,(255,255,0),self.rect)

j = Jogador()
inimigos = [Inimigo() for _ in range(4)]
tiros = []
vidas = 5
pontos = 0

ultimo_dano = 0
cooldown = 1000

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
            tiros.append(Tiro(j.rect.centerx, j.rect.y))

    t = pygame.key.get_pressed()
    j.mover(t)

    for tiro in tiros[:]:
        tiro.mover()
        for ini in inimigos[:]:
            if tiro.rect.colliderect(ini.rect):
                ini.vida -= 1
                if ini.vida <= 0:
                    inimigos.remove(ini)
                if tiro in tiros:
                    tiros.remove(tiro)
                break

    for ini in inimigos:
        ini.mover(j)
        if ini.rect.colliderect(j.rect):
            agora = pygame.time.get_ticks()
            if agora - ultimo_dano > cooldown:
                vidas -= 1
                ultimo_dano = agora

    if vidas <= 0:
        break

    pontos += 1

    TELA.fill((20,20,40))
    j.draw()

    for ini in inimigos:
        ini.draw()

    for tiro in tiros:
        tiro.draw()

    txt = fonte.render(f"Vidas: {vidas} | Pontos: {pontos}", True, (255,255,255))
    TELA.blit(txt,(10,10))

    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()


# =========================================
# NIVEL 3
# =========================================
import pygame, sys, random

pygame.init()
TELA = pygame.display.set_mode((800, 600))
CLOCK = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial", 28)
fonte_grande = pygame.font.SysFont("Arial", 48)

class Jogador:
    def __init__(self):
        self.rect = pygame.Rect(375,275,50,50)
        self.vel = 5

    def mover(self,t):
        if t[pygame.K_LEFT] and self.rect.x > 0: self.rect.x -= self.vel
        if t[pygame.K_RIGHT] and self.rect.x < 750: self.rect.x += self.vel
        if t[pygame.K_UP] and self.rect.y > 0: self.rect.y -= self.vel
        if t[pygame.K_DOWN] and self.rect.y < 550: self.rect.y += self.vel

    def draw(self):
        pygame.draw.rect(TELA,(0,150,255),self.rect)

class Inimigo:
    def __init__(self, vel):
        self.rect = pygame.Rect(random.randint(0,750),0,40,40)
        self.vel = vel
        self.vida = 3

    def mover(self,j):
        if self.rect.x < j.rect.x: self.rect.x += self.vel
        if self.rect.x > j.rect.x: self.rect.x -= self.vel
        if self.rect.y < j.rect.y: self.rect.y += self.vel
        if self.rect.y > j.rect.y: self.rect.y -= self.vel

    def draw(self):
        pygame.draw.rect(TELA,(255,165,0),self.rect)

class Tiro:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,10,10)

    def mover(self):
        self.rect.y -= 7

    def draw(self):
        pygame.draw.rect(TELA,(255,255,0),self.rect)

niveis = {
    1: {"vel":2,"qtd":3},
    2: {"vel":3,"qtd":5},
    3: {"vel":5,"qtd":7}
}

nivel = 1
pontos = 0
mostrar = False
tempo_msg = 0

j = Jogador()
inimigos = [Inimigo(niveis[nivel]["vel"]) for _ in range(niveis[nivel]["qtd"])]
tiros = []
vidas = 5

ultimo_dano = 0
cooldown = 1000

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
            tiros.append(Tiro(j.rect.centerx, j.rect.y))

    t = pygame.key.get_pressed()
    j.mover(t)

    for tiro in tiros[:]:
        tiro.mover()
        for ini in inimigos[:]:
            if tiro.rect.colliderect(ini.rect):
                ini.vida -= 1
                if ini.vida <= 0:
                    inimigos.remove(ini)
                if tiro in tiros:
                    tiros.remove(tiro)
                break

    for ini in inimigos:
        ini.mover(j)
        if ini.rect.colliderect(j.rect):
            agora = pygame.time.get_ticks()
            if agora - ultimo_dano > cooldown:
                vidas -= 1
                ultimo_dano = agora

    if vidas <= 0:
        break

    pontos += 1

    if pontos % 500 == 0:
        if nivel < 3:
            nivel += 1
            mostrar = True
            tempo_msg = pygame.time.get_ticks()
            inimigos = [Inimigo(niveis[nivel]["vel"]) for _ in range(niveis[nivel]["qtd"])]

    TELA.fill((20,20,40))
    j.draw()

    for ini in inimigos:
        ini.draw()

    for tiro in tiros:
        tiro.draw()

    txt = fonte.render(f"Nivel: {nivel} | Vidas: {vidas} | Pontos: {pontos}", True, (255,255,255))
    TELA.blit(txt,(10,10))

    if mostrar:
        if pygame.time.get_ticks() - tempo_msg < 2000:
            texto = fonte_grande.render(f"NIVEL {nivel}", True, (255,255,255))
            TELA.blit(texto,(250,250))
        else:
            mostrar = False

    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()


# =========================================
# NIVEL 4
# =========================================
import pygame, sys, random

pygame.init()
TELA = pygame.display.set_mode((800, 600))
CLOCK = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial", 28)

class Jogador:
    def __init__(self):
        self.rect = pygame.Rect(375,275,50,50)
        self.vel = 5

    def mover(self,t):
        if t[pygame.K_LEFT] and self.rect.x > 0: self.rect.x -= self.vel
        if t[pygame.K_RIGHT] and self.rect.x < 750: self.rect.x += self.vel
        if t[pygame.K_UP] and self.rect.y > 0: self.rect.y -= self.vel
        if t[pygame.K_DOWN] and self.rect.y < 550: self.rect.y += self.vel

    def draw(self):
        pygame.draw.rect(TELA,(0,150,255),self.rect)

class Inimigo:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0,750),0,40,40)
        self.vel = 3
        self.vida = 3
        self.cor = (255,165,0)

    def mover(self,j):
        if self.rect.x < j.rect.x: self.rect.x += self.vel
        if self.rect.x > j.rect.x: self.rect.x -= self.vel
        if self.rect.y < j.rect.y: self.rect.y += self.vel
        if self.rect.y > j.rect.y: self.rect.y -= self.vel

    def draw(self):
        pygame.draw.rect(TELA,self.cor,self.rect)

class InimigoRapido(Inimigo):
    def __init__(self):
        super().__init__()
        self.vel = 6
        self.cor = (255,0,255)

class InimigoGigante(Inimigo):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(random.randint(0,750),0,80,80)
        self.vida = 5
        self.cor = (0,255,0)

class Tiro:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,10,10)

    def mover(self):
        self.rect.y -= 7

    def draw(self):
        pygame.draw.rect(TELA,(255,255,0),self.rect)

def spawn():
    tipo = random.choice(["normal","rapido","gigante"])
    if tipo == "rapido":
        return InimigoRapido()
    elif tipo == "gigante":
        return InimigoGigante()
    return Inimigo()

j = Jogador()
inimigos = [spawn() for _ in range(5)]
tiros = []
vidas = 5
pontos = 0

ultimo_dano = 0
cooldown = 1000

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
            tiros.append(Tiro(j.rect.centerx, j.rect.y))

    t = pygame.key.get_pressed()
    j.mover(t)

    for tiro in tiros[:]:
        tiro.mover()
        for ini in inimigos[:]:
            if tiro.rect.colliderect(ini.rect):
                ini.vida -= 1
                if ini.vida <= 0:
                    inimigos.remove(ini)
                if tiro in tiros:
                    tiros.remove(tiro)
                break

    for ini in inimigos:
        ini.mover(j)
        if ini.rect.colliderect(j.rect):
            agora = pygame.time.get_ticks()
            if agora - ultimo_dano > cooldown:
                vidas -= 1
                ultimo_dano = agora

    if vidas <= 0:
        break

    pontos += 1

    if random.randint(1,100) < 2:
        inimigos.append(spawn())

    TELA.fill((20,20,40))
    j.draw()

    for ini in inimigos:
        ini.draw()

    for tiro in tiros:
        tiro.draw()

    txt = fonte.render(f"Vidas: {vidas} | Pontos: {pontos}", True, (255,255,255))
    TELA.blit(txt,(10,10))

    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()
