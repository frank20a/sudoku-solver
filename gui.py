import pygame
from sudoku import Sudoku


class App:
    def __init__(self, autorun=True, delay=50):
        self._running = True
        self.screen = None
        self.size = self.width, self.height = 650, 750

        self.delay = delay
        self.sudoku = Sudoku('games/expert4.txt')
        self.console = ''

        if autorun: self.on_execute()

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Sudoku Solver")
        self._running = True
        self.font32 = pygame.font.SysFont('arial.ttf', 32)
        self.font48 = pygame.font.SysFont('arial.ttf', 48)
        self.font16 = pygame.font.SysFont('arial.ttf', 16)
        self.font24 = pygame.font.SysFont('arial.ttf', 24)

        return True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.runBtn.collidepoint(event.pos):
                    pygame.time.set_timer(pygame.USEREVENT+1, self.delay)
                if self.stepBtn.collidepoint(event.pos):
                    self.console = self.sudoku.step()
        if event.type == pygame.USEREVENT+1:
            self.console = self.sudoku.step()
            if self.sudoku.solved(): pygame.time.set_timer(pygame.USEREVENT+1, 0)

    def on_loop(self):
        # Clear
        self.screen.fill('#d1d1d1')

        # Draw buttons
        self.runBtn = pygame.draw.rect(self.screen, '#009621', pygame.Rect(0, self.width, self.width//3, 100))
        runTxt = self.font32.render('Solve', True, '#000000')
        runTxtRect = runTxt.get_rect()
        self.screen.blit(runTxt, ((self.width//3 - runTxtRect.width)//2, self.width + (100-runTxtRect.height)//2))

        self.stepBtn = pygame.draw.rect(self.screen, '#3832a8', pygame.Rect(self.width//3, self.width, self.width//3, 100))
        stepTxt = self.font32.render('Step', True, '#000000')
        stepTxtRect = stepTxt.get_rect()
        self.screen.blit(stepTxt, ((self.width - stepTxtRect.width) // 2, self.width + (100 - stepTxtRect.height) // 2))

        # Draw grid
        for i in range(10):
            w = 4 if i % 3 == 0 else 2
            pygame.draw.line(self.screen, '#000000', (0, i*(self.width//9)), (self.width, i*(self.width//9)), w)
            pygame.draw.line(self.screen, '#000000', (i*(self.width//9), 0), (i*(self.width//9), self.width), w)

        # Draw numbers
        c_size = self.width // 9        # Cell Size
        for i, row in enumerate(self.sudoku.board):
            for j, cell in enumerate(row):
                if len(cell) == 1:
                    numTxt = self.font48.render(str(cell[0]), True, '#000000')
                    numRec = stepTxt.get_rect()
                    self.screen.blit(numTxt, ((j + 0.75) * c_size - numRec.width/2, (i + 0.5) * c_size - numRec.height/2))
                else:
                    for num in cell:
                        x = (j + ((num-1)%3)/3 + 1/8) * c_size
                        y = (i + ((num-1)//3)/3 + 1/8) * c_size
                        self.screen.blit(self.font16.render(str(num), True, '#000000'), (x, y))

        # Draw Console Text
        consoleTxt = self.font24.render(self.console, True, '#000000')
        consoleTxtRect = consoleTxt.get_rect()
        self.screen.blit(consoleTxt, ((5*self.width//3 - consoleTxtRect.width) // 2, self.width + (100 - consoleTxtRect.height) // 2))

    def on_render(self):
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if not self.on_init():
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

        self.on_cleanup()

if __name__ == '__main__':
    App()