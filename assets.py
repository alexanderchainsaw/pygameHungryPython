import pygame


class Assets:  # TODO - inherit from config to collect sqr_size
    """Lower level class to store in-game assets"""
    def __init__(self):
        """Initialize the assets"""

        self.size = None  # TODO = sqr_size * 2

        self.background = pygame.image.load('background.png')
        self.body_blue = pygame.image.load('PythonBody.png')
        self.body_yellow = pygame.image.load('PythonBodyAlt.png')
        self.head = pygame.image.load('PythonHead.png')

        c = pygame.transform.smoothscale(pygame.image.load('Assets/c.png'))
        cplus = pygame.image.load('Assets/cplusplus.png')
        csharp = pygame.image.load('Assets/csharp.png')
        js = pygame.image.load('Assets/js.png')
        java = pygame.image.load('Assets/java.png')
        r = pygame.image.load('Assets/r.png')
        ruby = pygame.image.load('Assets/ruby.png')
        golang = pygame.image.load('Assets/golang.png')
        php = pygame.image.load('Assets/php.png')
        rust = pygame.image.load('Assets/rust.png')
        swift = pygame.image.load('Assets/swift.png')
        scala = pygame.image.load('Assets/scala.png')
        kotlin = pygame.image.load('Assets/kotlin.png')
        haskell = pygame.image.load('Assets/haskell.png')

        self.food_images = [c, cplus, csharp, js, java, r, ruby, rust, golang, php, swift, scala, kotlin, haskell]

        self.forbidden_food = pygame.image.load('python.svg')
