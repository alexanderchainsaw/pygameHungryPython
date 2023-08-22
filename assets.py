import pygame
from configuration import Configuration


class Assets(Configuration):
    """Lower level class to store in-game assets"""
    def __init__(self):
        super().__init__()
        """Initialize and transform assets according to configuration data"""

        self.size = self._square_size * 2

        # TODO: find proper svg's and transform them
        self.background = pygame.image.load('assets/background.png')
        self.body_blue = pygame.image.load('assets/PythonBody.png')
        self.body_yellow = pygame.image.load('assets/PythonBodyAlt.png')
        self.head = pygame.image.load('assets/PythonHead.png')

        c = pygame.transform.smoothscale(pygame.image.load('assets/c.png'), self.size)
        cplus = pygame.image.load('assets/cplusplus.png')
        csharp = pygame.image.load('assets/csharp.png')
        js = pygame.image.load('assets/js.png')
        java = pygame.image.load('assets/java.png')
        r = pygame.image.load('assets/r.png')
        ruby = pygame.image.load('assets/ruby.png')
        golang = pygame.image.load('assets/golang.png')
        php = pygame.image.load('assets/php.png')
        rust = pygame.image.load('assets/rust.png')
        swift = pygame.image.load('assets/swift.png')
        scala = pygame.image.load('assets/scala.png')
        kotlin = pygame.image.load('assets/kotlin.png')
        haskell = pygame.image.load('assets/haskell.png')

        self.food_images = [c, cplus, csharp, js, java, r, ruby, rust, golang, php, swift, scala, kotlin, haskell]

        self.forbidden_food = pygame.image.load('assets/python.svg')
