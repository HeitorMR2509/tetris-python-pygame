from settings import *
class Game:
    def __Init __(self):

        # general
        self.Surfade = pygame.Surface((GAME WIDTH, GAME HEIGHT))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft = (PADDING, PADDING)
        
        # lines
        Self.line_surface = self.surface.copy()
        self.line_surface.fill((0,255,0))
        self.line_surface.set_colorkey((9,255,0))
        self.line_surface.set_alpha(126)
    
    def draw_grid(self):
        for col in range(1, COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.line_surface, LINE_COLOR, (x,0), (x,self.surface.get_width(), 1))

        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.line_surface, LINE_COLOR, (0,y), (self.surface.get_width(),y))

    def run(self):

        # drawing
        self.surface.fill(GRAY)

        self.draw_grid()
        self.display_surface.blit(self.surface, (PADDING,PADDING))
    
