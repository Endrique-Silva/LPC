import pygame

pygame.init()

HEIGHT, WIDTH = 800, 893
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
FPS = 60

score = 0
balls = 1
velocity = 4

paddle_width = 60
paddle_height = 20

sprites_list = pygame.sprite.Group()


class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > WIDTH - wall_width - paddle_width:
            self.rect.x = WIDTH - wall_width - paddle_width

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < wall_width:
            self.rect.x = wall_width


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.velocity = [velocity, velocity]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = self.velocity[0]
        self.velocity[1] = -self.velocity[1]


paddle = Paddle(pygame.Color("blue"), paddle_width, paddle_height)
paddle.rect.x = WIDTH // 2 - paddle_width // 2
paddle.rect.y = HEIGHT - 65

ball = Ball(pygame.Color("white"), 10, 10)
ball.rect.x = WIDTH // 2 - 5
ball.rect.y = HEIGHT // 2 - 5

all_bricks = pygame.sprite.Group()

brick_width = 55
brick_height = 16
x_gap = 7
y_gap = 5
wall_width = 16


def bricks():
    for j in range(8):
        for i in range(14):
            if j < 2:
                if i == 0:
                    brick = Brick(pygame.Color("red"), brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(pygame.Color("red"), brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    sprites_list.add(brick)
                    all_bricks.add(brick)
            if 1 < j < 4:
                if i == 0:
                    brick = Brick(pygame.Color("orange"), brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(pygame.Color("orange"), brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    sprites_list.add(brick)
                    all_bricks.add(brick)
            if 3 < j < 6:
                if i == 0:
                    brick = Brick(pygame.Color("green"), brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(pygame.Color("green"), brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    sprites_list.add(brick)
                    all_bricks.add(brick)
            if 5 < j < 8:
                if i == 0:
                    brick = Brick(pygame.Color("yellow"), brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(pygame.Color("yellow"), brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    sprites_list.add(brick)
                    all_bricks.add(brick)


brick_wall = bricks()

sprites_list.add(paddle)
sprites_list.add(ball)


def main(score, balls):

    step = 0

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.moveLeft(10)
        if keys[pygame.K_RIGHT]:
            paddle.moveRight(10)

        sprites_list.update()

        if ball.rect.y < 40:
            ball.velocity[1] = -ball.velocity[1]

        if ball.rect.x >= WIDTH - wall_width - 10:
            ball.velocity[0] = -ball.velocity[0]

        if ball.rect.x <= wall_width:
            ball.velocity[0] = -ball.velocity[0]

        if ball.rect.y > HEIGHT:
            ball.rect.x = WIDTH // 2 - 5
            ball.rect.y = HEIGHT // 2 - 5
            ball.velocity[1] = ball.velocity[1]
            balls += 1
            if balls == 4:
                font = pygame.font.SysFont('arial', 70)
                text = font.render("GAME OVER", True, pygame.Color("white"))
                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                run = False

        if pygame.sprite.collide_mask(ball, paddle):
            ball.rect.x += ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            ball.bounce()

        brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
        for brick in brick_collision_list:
            ball.bounce()
            if len(brick_collision_list) > 0:
                step += 1
                for i in range(0, 448, 28):
                    if step == i:
                        ball.velocity[0] += 1
                        ball.velocity[1] += 1
            if 380.5 > brick.rect.y > 338.5:
                score += 1
                brick.kill()
            elif 338.5 > brick.rect.y > 294:
                score += 3
                brick.kill()
            elif 294 > brick.rect.y > 254.5:
                score += 5
                brick.kill()
            else:
                score += 7
                brick.kill()
            if len(all_bricks) == 0:
                font = pygame.font.SysFont("arial", 70)
                text = font.render("SCREEN CLEARED", True, pygame.Color("white"))
                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                sprites_list.add(ball)
                screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                run = False

        screen.fill(pygame.Color("black"))

        pygame.draw.line(screen, pygame.Color("grey"), [0, 19], [WIDTH, 19], 40)
        pygame.draw.line(screen, pygame.Color("grey"), [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT], wall_width)
        pygame.draw.line(screen, pygame.Color("grey"), [(WIDTH - wall_width / 2) - 1, 0], [(WIDTH - wall_width / 2) - 1, HEIGHT], wall_width)

        pygame.draw.line(screen, pygame.Color("blue"), [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2], [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)
        pygame.draw.line(screen, pygame.Color("blue"), [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2], [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)

        pygame.draw.line(screen, pygame.Color("red"), [(wall_width / 2) - 1, 212.5], [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap], wall_width)
        pygame.draw.line(screen, pygame.Color("red"), [(WIDTH - wall_width / 2) - 1, 212.5], [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap], wall_width)

        pygame.draw.line(screen, pygame.Color("orange"), [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap], [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], wall_width)
        pygame.draw.line(screen, pygame.Color("orange"), [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap], [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], wall_width)

        pygame.draw.line(screen, pygame.Color("green"), [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], wall_width)
        pygame.draw.line(screen, pygame.Color("green"), [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], wall_width)

        pygame.draw.line(screen, pygame.Color("yellow"), [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], [(wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap], wall_width)
        pygame.draw.line(screen, pygame.Color("yellow"), [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], [(WIDTH - wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap], wall_width)

        font = pygame.font.SysFont('arial', 70)
        text = font.render(str(f"{score:03}"), True, pygame.Color("white"))
        screen.blit(text, (80, 120))
        text = font.render(str(balls), True, pygame.Color("white"))
        screen.blit(text, (520, 41))
        text = font.render('000', True, pygame.Color("white"))
        screen.blit(text, (580, 120))
        text = font.render('1', True, pygame.Color("white"))
        screen.blit(text, (20, 40))

        sprites_list.draw(screen)

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()


main(score, balls)