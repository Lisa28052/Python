import pygame
import sys

# Inicializa o pygame
pygame.init()

# Define as dimensões da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define as cores
white = (255, 255, 255)
black = (0, 0, 0)
green = (34, 139, 34)  # Cor da mesa de tênis de mesa
blue = (0, 0, 255)
red = (255, 0, 0)
gray = (100, 100, 100)

# Define as variáveis da bola
ball_width = 20
ball_x = screen_width // 2 - ball_width // 2
ball_y = screen_height // 2 - ball_width // 2
ball_dx = 8  # Velocidade inicial da bola será ajustada pelo nível de dificuldade
ball_dy = 8

# Define as variáveis das raquetes
paddle_width = 10
paddle_height = 100
paddle_speed = 10
paddle1_x = 30
paddle1_y = screen_height // 2 - paddle_height // 2
paddle2_x = screen_width - 30 - paddle_width
paddle2_y = screen_height // 2 - paddle_height // 2

# Placar
score1 = 0
score2 = 0
font = pygame.font.SysFont("Arial", 30)

# Função para desenhar o plano de fundo (mesa de tênis de mesa)
def draw_background():
    screen.fill(green)
    net_width = 4
    pygame.draw.rect(screen, white, (screen_width // 2 - net_width // 2, 0, net_width, screen_height))

# Função para desenhar a bola
def draw_ball():
    pygame.draw.rect(screen, white, (ball_x, ball_y, ball_width, ball_width))

# Função para desenhar as raquetes com cores
def draw_paddles(mode):
    if mode == 2:  # Modo de dois jogadores
        pygame.draw.rect(screen, blue, (paddle1_x, paddle1_y, paddle_width, paddle_height))
        pygame.draw.rect(screen, red, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    else:  # Modo de um jogador
        pygame.draw.rect(screen, blue, (paddle1_x, paddle1_y, paddle_width, paddle_height))  # Jogador 1 em azul
        pygame.draw.rect(screen, red, (paddle2_x, paddle2_y, paddle_width, paddle_height))   # Robô em vermelho

# Função para desenhar o placar
def draw_score():
    score_text = font.render(f"{score1}  -  {score2}", True, white)
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 20))

# Função para mostrar o ganhador com fundo colorido e uma mensagem
def show_color_winner(winner_color, message):
    screen.fill(winner_color)
    font_large = pygame.font.SysFont("Arial", 50)
    message_text = font_large.render(message, True, white)
    screen.blit(message_text, (screen_width // 2 - message_text.get_width() // 2, screen_height // 2 - message_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(2000)  # Espera 2 segundos antes de continuar

# Função para desenhar o menu com botões
def draw_menu():
    screen.fill(black)
    title_font = pygame.font.SysFont("Arial", 50)
    button_font = pygame.font.SysFont("Arial", 40)
    
    title = title_font.render("Ping Pong Game", True, white)
    screen.blit(title, (screen_width // 2 - title.get_width() // 2, screen_height // 3))
    
    single_button = pygame.Rect(screen_width // 2 - 150, screen_height // 2, 300, 50)
    two_player_button = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 70, 300, 50)
    
    pygame.draw.rect(screen, gray, single_button)
    pygame.draw.rect(screen, gray, two_player_button)
    
    single_text = button_font.render("1 Player", True, black)
    two_player_text = button_font.render("2 Players", True, black)
    
    screen.blit(single_text, (single_button.x + single_button.width // 2 - single_text.get_width() // 2, single_button.y + 10))
    screen.blit(two_player_text, (two_player_button.x + two_player_button.width // 2 - two_player_text.get_width() // 2, two_player_button.y + 10))
    
    pygame.display.flip()
    
    return single_button, two_player_button

def draw_difficulty_menu():
    screen.fill(black)
    title_font = pygame.font.SysFont("Arial", 50)
    button_font = pygame.font.SysFont("Arial", 40)
    
    title = title_font.render("Choose Difficulty", True, white)
    screen.blit(title, (screen_width // 2 - title.get_width() // 2, screen_height // 3))
    
    easy_button = pygame.Rect(screen_width // 2 - 150, screen_height // 2, 300, 50)
    medium_button = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 70, 300, 50)
    hard_button = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 140, 300, 50)
    
    pygame.draw.rect(screen, gray, easy_button)
    pygame.draw.rect(screen, gray, medium_button)
    pygame.draw.rect(screen, gray, hard_button)
    
    easy_text = button_font.render("Easy", True, black)
    medium_text = button_font.render("Medium", True, black)
    hard_text = button_font.render("Hard", True, black)
    
    screen.blit(easy_text, (easy_button.x + easy_button.width // 2 - easy_text.get_width() // 2, easy_button.y + 10))
    screen.blit(medium_text, (medium_button.x + medium_button.width // 2 - medium_text.get_width() // 2, medium_button.y + 10))
    screen.blit(hard_text, (hard_button.x + hard_button.width // 2 - hard_text.get_width() // 2, hard_button.y + 10))
    
    pygame.display.flip()
    
    return easy_button, medium_button, hard_button

def menu():
    while True:
        single_button, two_player_button = draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if single_button.collidepoint(mouse_x, mouse_y):
                    return choose_difficulty()
                if two_player_button.collidepoint(mouse_x, mouse_y):
                    return 2, None, 8, 8  # Jogar com dois jogadores

def choose_difficulty():
    while True:
        easy_button, medium_button, hard_button = draw_difficulty_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if easy_button.collidepoint(mouse_x, mouse_y):
                    return 1, 'easy', 4, 4  # Jogar sozinho, dificuldade fácil, velocidade da bola 4
                if medium_button.collidepoint(mouse_x, mouse_y):
                    return 1, 'medium', 6, 6  # Jogar sozinho, dificuldade média, velocidade da bola 6
                if hard_button.collidepoint(mouse_x, mouse_y):
                    return 1, 'hard', 8, 8  # Jogar sozinho, dificuldade difícil, velocidade da bola 8

# Função para o movimento da IA (computador)
def ai_move(difficulty):
    global ball_y, paddle2_y
    if difficulty == 'easy':
        ai_speed = 4
    elif difficulty == 'medium':
        ai_speed = 6
    else:  # Hard
        ai_speed = 8

    if paddle2_y + paddle_height // 2 < ball_y:
        paddle2_y += ai_speed
    if paddle2_y + paddle_height // 2 > ball_y:
        paddle2_y -= ai_speed
    if paddle2_y < 0:
        paddle2_y = 0
    if paddle2_y > screen_height - paddle_height:
        paddle2_y = screen_height - paddle_height

# Função de contagem regressiva animada
def countdown_animation():
    font_large = pygame.font.SysFont("Arial", 70)
    for i in range(3, 0, -1):
        screen.fill(black)
        countdown_text = font_large.render(str(i), True, white)
        screen.blit(countdown_text, (screen_width // 2 - countdown_text.get_width() // 2, screen_height // 2 - countdown_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(1000)

# Função principal do jogo
def main():
    global ball_x, ball_y, ball_dx, ball_dy, paddle1_y, paddle2_y, score1, score2
    
    mode, difficulty, ball_dx, ball_dy = menu()
    
    countdown_animation()
    
    while True:
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Movimento dos jogadores
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1_y > 0:
            paddle1_y -= paddle_speed
        if keys[pygame.K_s] and paddle1_y < screen_height - paddle_height:
            paddle1_y += paddle_speed
        
        if mode == 2:  # Modo de dois jogadores
            if keys[pygame.K_UP] and paddle2_y > 0:
                paddle2_y -= paddle_speed
            if keys[pygame.K_DOWN] and paddle2_y < screen_height - paddle_height:
                paddle2_y += paddle_speed
        else:  # Modo de um jogador
            ai_move(difficulty)
        
        # Movimento da bola
        ball_x += ball_dx
        ball_y += ball_dy
        
        # Colisão com a parede
        if ball_y <= 0 or ball_y >= screen_height - ball_width:
            ball_dy *= -1
        
        # Colisão com as raquetes
        if ball_x <= paddle1_x + paddle_width and paddle1_y < ball_y < paddle1_y + paddle_height:
            ball_dx *= -1
        if ball_x >= paddle2_x - ball_width and paddle2_y < ball_y < paddle2_y + paddle_height:
            ball_dx *= -1
        
        # Pontuação
        if ball_x < 0:
            score2 += 1
            ball_x, ball_y = screen_width // 2 - ball_width // 2, screen_height // 2 - ball_width // 2
            countdown_animation()
        if ball_x > screen_width:
            score1 += 1
            ball_x, ball_y = screen_width // 2 - ball_width // 2, screen_height // 2 - ball_width // 2
            countdown_animation()
        
        # Desenha na tela
        draw_background()
        draw_ball()
        draw_paddles(mode)
        draw_score()
        
        pygame.display.flip()
        pygame.time.Clock().tick(60)

# Executa o jogo
if __name__ == "__main__":
    main()
