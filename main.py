"""
Módulo principal para el juego 'Esquiva Bloques'.

Este juego es un simple 'dodger game' donde el jugador debe esquivar
bloques que caen desde la parte superior de la pantalla. El objetivo
es sobrevivir el mayor tiempo posible para obtener la máxima puntuación.

Este archivo contiene toda la lógica del juego, incluyendo las clases
para el jugador y los enemigos, el bucle principal del juego y las
funciones de apoyo.
"""

import pygame
import random
import sys

# --- Constantes ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Player(pygame.sprite.Sprite):
    """
    Representa al jugador en el juego.

    Atributos:
        width (int): Ancho del sprite del jugador.
        height (int): Alto del sprite del jugador.
        image (pygame.Surface): La superficie que representa al jugador.
        rect (pygame.Rect): El rectángulo que define la posición y tamaño del jugador.
        speed_x (int): La velocidad de movimiento horizontal del jugador.
    """
    def __init__(self):
        """Inicializa el objeto Player, creando su imagen y posición inicial."""
        super().__init__()
        self.width = 50
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 8

    def update(self):
        """Actualiza el estado del jugador en cada fotograma."""
        # Mantiene al jugador dentro de los límites de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def move_left(self):
        """Mueve al jugador hacia la izquierda."""
        self.rect.x -= self.speed_x

    def move_right(self):
        """Mueve al jugador hacia la derecha."""
        self.rect.x += self.speed_x

    def draw(self, surface):
        """
        Dibuja al jugador en la superficie especificada.

        Args:
            surface (pygame.Surface): La superficie sobre la cual dibujar.
        """
        surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    """
    Representa a un enemigo (bloque que cae).

    Los enemigos aparecen en una posición horizontal aleatoria en la parte
    superior de la pantalla y caen a una velocidad vertical aleatoria.
    """
    def __init__(self):
        """Inicializa un enemigo con posición y velocidad aleatorias."""
        super().__init__()
        self.width = 40
        self.height = 40
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 8)

    def update(self):
        """Mueve el enemigo hacia abajo y lo elimina si sale de la pantalla."""
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.kill()

    def draw(self, surface):
        """
        Dibuja al enemigo en la superficie especificada.

        Args:
            surface (pygame.Surface): La superficie sobre la cual dibujar.
        """
        surface.blit(self.image, self.rect)


def draw_text(surface, text, size, x, y, color):
    """
    Dibuja texto en una superficie dada.

    Args:
        surface (pygame.Surface): La superficie sobre la cual dibujar.
        text (str): El contenido del texto a mostrar.
        size (int): El tamaño de la fuente.
        x (int): La coordenada x del centro del texto.
        y (int): La coordenada y del centro del texto.
        color (tuple): El color del texto en formato RGB.
    """
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


def spawn_enemy():
    """Crea una nueva instancia de Enemy y la añade a los grupos de sprites."""
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)


def reset_game():
    """Reinicia el juego a su estado inicial."""
    global score, game_over, all_sprites, enemies, player
    score = 0
    game_over = False

    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    for _ in range(8):
        spawn_enemy()


# --- Bloque principal de ejecución ---
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Esquiva Bloques")
    clock = pygame.time.Clock()

    score = 0
    game_over = False
    all_sprites = None
    enemies = None
    player = None

    reset_game()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    reset_game()

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                player.move_left()
            if keys[pygame.K_d]:
                player.move_right()

            all_sprites.update()

            if len(enemies) < 8:
                spawn_enemy()

            hits = pygame.sprite.spritecollide(player, enemies, False)
            if hits:
                game_over = True

            score += 1

        screen.fill(BLACK)
        all_sprites.draw(screen)
        draw_text(screen, f"Puntuación: {score}", 30, SCREEN_WIDTH / 2, 10, WHITE)

        if game_over:
            draw_text(screen, "GAME OVER", 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4, RED)
            draw_text(
                screen,
                "Presiona una tecla para reiniciar o ESC para salir",
                22,
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
                WHITE
            )

        pygame.display.flip()

    pygame.quit()
    sys.exit()