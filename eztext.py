# input lib
from pygame.locals import *
import pygame, string

class ConfigError(KeyError): pass

class Config:
    """ A utility for configuration """
    def __init__(self, options, *look_for):
        assertions = []
        for key in look_for:
            if key[0] in options.keys(): exec('self.'+key[0]+' = options[\''+key[0]+'\']')
            else: exec('self.'+key[0]+' = '+key[1])
            assertions.append(key[0])
        for key in options.keys():
            if key not in assertions: raise ConfigError(key+' not expected as option')

class Input:
    """ A text input for pygame apps """
    def __init__(self, **options):
        """ Options: x, y, font, color, restricted, maxlength, prompt """
        self.options = Config(options, ['x', '0'], ['y', '0'], ['font','pygame.font.Font("font/gameplay.ttf", 35)'],
                              ['color', '(0,0,0)'], ['restricted',
 '\'abcdefghijklmnopqrstuvwxyz.@\''],
                              ['maxlength', '-1'], ['prompt', '\'\''],['focus','False'])
        self.x = self.options.x; self.y = self.options.y
        self.font = self.options.font
        self.color = self.options.color
        self.restricted = self.options.restricted
        self.maxlength = self.options.maxlength
        self.prompt = self.options.prompt; self.value = ''
        self.shifted = False
        self.pause = 0
        self.focus = self.options.focus

    def set_pos(self, x, y):
        """ Set the position to x, y """
        self.x = x
        self.y = y

    def set_font(self, font):
        """ Set the font for the input """
        self.font = font

    def draw(self, surface):
        """ Draw the text input to a surface """
        text = self.font.render(self.prompt+self.value, 1, self.color)
        surface.blit(text, (self.x, self.y))

    def update(self, events):
        """ Update the input based on passed events """
        if self.focus != True:
            return

        pressed = pygame.key.get_pressed()#Add ability to hold down delete key and delete text
        if self.pause == 3 and pressed[K_BACKSPACE]:
            self.pause = 0
            self.value = self.value[:-1]
        elif pressed[K_BACKSPACE]:
            self.pause += 1
        else:
            self.pause = 0

        for event in events:
            if event.type == KEYUP:
                if event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = False
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE: self.value = self.value[:-1]
                elif event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = True
                elif event.key == K_RETURN: return self.value#return value
                if not self.shifted:
                    if event.key == K_a and 'a' in self.restricted: self.value += 'a'
                    elif event.key == K_b and 'b' in self.restricted: self.value += 'b'
                    elif event.key == K_c and 'c' in self.restricted: self.value += 'c'
                    elif event.key == K_d and 'd' in self.restricted: self.value += 'd'
                    elif event.key == K_e and 'e' in self.restricted: self.value += 'e'
                    elif event.key == K_f and 'f' in self.restricted: self.value += 'f'
                    elif event.key == K_g and 'g' in self.restricted: self.value += 'g'
                    elif event.key == K_h and 'h' in self.restricted: self.value += 'h'
                    elif event.key == K_i and 'i' in self.restricted: self.value += 'i'
                    elif event.key == K_j and 'j' in self.restricted: self.value += 'j'
                    elif event.key == K_k and 'k' in self.restricted: self.value += 'k'
                    elif event.key == K_l and 'l' in self.restricted: self.value += 'l'
                    elif event.key == K_m and 'm' in self.restricted: self.value += 'm'
                    elif event.key == K_n and 'n' in self.restricted: self.value += 'n'
                    elif event.key == K_o and 'o' in self.restricted: self.value += 'o'
                    elif event.key == K_p and 'p' in self.restricted: self.value += 'p'
                    elif event.key == K_q and 'q' in self.restricted: self.value += 'q'
                    elif event.key == K_r and 'r' in self.restricted: self.value += 'r'
                    elif event.key == K_s and 's' in self.restricted: self.value += 's'
                    elif event.key == K_t and 't' in self.restricted: self.value += 't'
                    elif event.key == K_u and 'u' in self.restricted: self.value += 'u'
                    elif event.key == K_v and 'v' in self.restricted: self.value += 'v'
                    elif event.key == K_w and 'w' in self.restricted: self.value += 'w'
                    elif event.key == K_x and 'x' in self.restricted: self.value += 'x'
                    elif event.key == K_y and 'y' in self.restricted: self.value += 'y'
                    elif event.key == K_z and 'z' in self.restricted: self.value += 'z'
                    elif event.key == K_PERIOD and '.' in self.restricted: self.value += '.'
                elif self.shifted:
                    if event.key == K_2 and '@' in self.restricted: self.value += '@'

        if len(self.value) > self.maxlength and self.maxlength >= 0: self.value = self.value[:-1]
