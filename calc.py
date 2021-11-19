import pygame, sys
from pygame.locals import *
from math import cos, sin, sqrt, tan, pi


# Initialize pygame
pygame.init()
pygame.display.set_caption('Calculator')
clock = pygame.time.Clock()
SURF = pygame.display.set_mode((450, 550))
font = pygame.font.SysFont(None, 30)
calc = pygame.font.SysFont('ocraextended', 25)

FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 120)
BLACK = (0, 0, 0)
GREEN = (36, 204, 68)
mouse_pos = (0, 0)
equation = ''
y = 0
btn_width = 45
screen = pygame.Rect(50, 50, 300, 50)
mouse = pygame.draw.rect(SURF, WHITE, Rect(mouse_pos, (1, 1)))

text, pos, rect, face, text_rect = 'text', 'pos', 'rect', 'face', 'text_rect'
buttons = {
    'btn_clear': {text: 'C', pos: (100, 150)},
    'btn_bksp': {text: '<x', pos: (150, 150)},
    'btn_left': {text: '(', pos: (200, 150)},
    'btn_right': {text: ')', pos: (250, 150)},
    'btn_7': {text: '7', pos: (100, 200)},
    'btn_8': {text: '8', pos: (150, 200)},
    'btn_9': {text: '9', pos: (200, 200)},
    'btn_divide': {text: '/', pos: (250, 200)},
    'btn_4': {text: '4', pos: (100, 250)},
    'btn_5': {text: '5', pos: (150, 250)},
    'btn_6': {text: '6', pos: (200, 250)},
    'btn_multiply': {text: '*', pos: (250, 250)},
    'btn_1': {text: '1', pos: (100, 300)},
    'btn_2': {text: '2', pos: (150, 300)},
    'btn_3': {text: '3', pos: (200, 300)},
    'btn_minus': {text: '-', pos: (250, 300)},
    'btn_decimal': {text: '.', pos: (100, 350)},
    'btn_0': {text: '0', pos: (150, 350)},
    'btn_equals': {text: '=', pos: (200, 350)},
    'btn_plus': {text: '+', pos: (250, 350)},
    'btn_cos': {text: 'cos(', pos: (100, 400)},
    'btn_tan': {text: 'tan(', pos: (150, 400)},
    'btn_sin': {text: 'sin(', pos: (200, 400)},
    'btn_sqrt': {text: 'sqrt(', pos: (250, 400)},
    'btn_pi': {text: 'pi', pos: (100, 450)},
    'btn_modulo': {text: '%', pos: (150, 450)}
}
keys = "1234567890."

for button in buttons:
    b_pos = buttons[button][pos]
    b_text = buttons[button][text]

    # Create a rectangle object and store it in the dict
    rect_params = list(b_pos)
    rect_params.extend((btn_width, btn_width))
    b_rectangle = pygame.Rect(rect_params)
    buttons[button][rect] = b_rectangle

    # Create a "face" and store it in the dict
    if b_text[-1] == '(' and b_text[0] != '(':
        b_text = b_text[:-1]  # trim the trailing paren off the math functions
    b_face = font.render(b_text, True, WHITE)
    b_text_rect = b_face.get_rect()
    b_text_rect.center = b_rectangle.center  # center the text in the rect
    buttons[button][face] = b_face
    buttons[button][text_rect] = b_text_rect

while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if mouse.colliderect(buttons[button][rect]):
                        current_button = buttons[button][text]
                        if current_button == '=' and equation == '':
                            equation = ''
                        elif current_button == '=':
                            equation = f"{eval(equation)}"
                        elif current_button == 'C':
                            equation = ''
                        elif current_button == '<x':
                            equation = equation[:-1]
                        elif current_button == 'pi':
                            equation += str(pi)
                        else:
                            equation += buttons[button][text]
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                mods = pygame.key.get_mods()
                if event.key == K_c:
                    equation = ''
                elif event.key == K_EQUALS and mods & pygame.KMOD_SHIFT:
                    equation += '+'
                elif event.key == K_MINUS:
                    equation += '-'
                elif event.key == K_SLASH:
                    equation += '/'
                elif event.key == K_8 and mods & pygame.KMOD_SHIFT:
                    equation += '*'
                elif event.key == K_5 and mods & pygame.KMOD_SHIFT:
                    equation += '%'
                elif event.key == K_9 and mods & pygame.KMOD_SHIFT:
                    equation += '('
                elif event.key == K_0 and mods & pygame.KMOD_SHIFT:
                    equation += ')'
                elif event.key == K_EQUALS or event.key == K_RETURN:
                    equation = f"{eval(equation)}"
                elif event.key == K_BACKSPACE:
                    equation = equation[:-1]
                elif pygame.key.name(event.key) in keys:
                    equation += pygame.key.name(event.key)

        SURF.fill(WHITE)
        mouse = pygame.draw.rect(SURF, WHITE, Rect(mouse_pos, (1, 1)))
        pygame.draw.rect(SURF, BLACK, screen, 0)

        for button in buttons:
            pygame.draw.rect(SURF, BLUE, buttons[button][rect], 0)
            SURF.blit(buttons[button][face], buttons[button][text_rect])

        equation_text = calc.render(equation, True, GREEN)
        equation_rect = equation_text.get_rect()
        equation_rect.centery = screen.centery
        equation_rect.right = screen.right - 5
        SURF.blit(equation_text, equation_rect)
        clock.tick(FPS)
        pygame.display.update()
    except SyntaxError:
        equation = 'ERROR'
    except NameError:
        equation = 'ERROR'
    except ZeroDivisionError:
        equation = 'ERROR'
