import pygame as pg
from pygame import Surface, SurfaceType

from settings import Settings


class Assets:
    """Lower level class to store in-game assets"""
    def __init__(self):
        settings = Settings()

        __ASSETS_SCALE = {
            40: ((pg.image.load('assets/python_40px.png'), pg.image.load('assets/c_40px.png'),
                 pg.image.load('assets/csharp_40px.png'), pg.image.load('assets/cplusplus_40px.png'),
                 pg.image.load('assets/js_40px.png'), pg.image.load('assets/java_40px.png'),
                 pg.image.load('assets/go_40px.png'), pg.image.load('assets/php_40px.png'),
                 pg.image.load('assets/rust_40px.png'), pg.image.load('assets/ruby_40px.png'),
                 pg.image.load('assets/swift_40px.png'), pg.image.load('assets/scala_40px.png'),
                 pg.image.load('assets/r_40px.png')),
                 (pg.image.load('assets/python_bodyb_40px.png'),
                  pg.image.load('assets/python_headb_40px.png'),
                  pg.image.load('assets/python_body_40px.png'))),

            50: ((pg.image.load('assets/python_50px.png'), pg.image.load('assets/c_50px.png'),
                 pg.image.load('assets/csharp_50px.png'), pg.image.load('assets/cplusplus_50px.png'),
                 pg.image.load('assets/js_50px.png'), pg.image.load('assets/java_50px.png'),
                 pg.image.load('assets/go_50px.png'), pg.image.load('assets/php_50px.png'),
                 pg.image.load('assets/rust_50px.png'), pg.image.load('assets/ruby_50px.png'),
                 pg.image.load('assets/swift_50px.png'), pg.image.load('assets/scala_50px.png'),
                 pg.image.load('assets/r_50px.png')),
                 (pg.image.load('assets/python_bodyb_50px.png'),
                  pg.image.load('assets/python_headb_50px.png'),
                  pg.image.load('assets/python_body_50px.png'))),

            60: ((pg.image.load('assets/python_60px.png'), pg.image.load('assets/c_60px.png'),
                 pg.image.load('assets/csharp_60px.png'), pg.image.load('assets/cplusplus_60px.png'),
                 pg.image.load('assets/js_60px.png'), pg.image.load('assets/java_60px.png'),
                 pg.image.load('assets/go_60px.png'), pg.image.load('assets/php_60px.png'),
                 pg.image.load('assets/rust_60px.png'), pg.image.load('assets/ruby_60px.png'),
                 pg.image.load('assets/swift_60px.png'), pg.image.load('assets/scala_60px.png'),
                 pg.image.load('assets/r_60px.png')),
                 (pg.image.load('assets/python_bodyb_60px.png'),
                  pg.image.load('assets/python_headb_60px.png'),
                  pg.image.load('assets/python_body_60px.png'))),

            64: ((pg.image.load('assets/python_64px.png'), pg.image.load('assets/c_64px.png'),
                 pg.image.load('assets/csharp_64px.png'), pg.image.load('assets/cplusplus_64px.png'),
                 pg.image.load('assets/js_64px.png'), pg.image.load('assets/java_64px.png'),
                 pg.image.load('assets/go_64px.png'), pg.image.load('assets/php_64px.png'),
                 pg.image.load('assets/rust_64px.png'), pg.image.load('assets/ruby_64px.png'),
                 pg.image.load('assets/swift_64px.png'), pg.image.load('assets/scala_64px.png'),
                 pg.image.load('assets/r_64px.png')),
                 (pg.image.load('assets/python_bodyb_64px.png'),
                  pg.image.load('assets/python_headb_64px.png'),
                  pg.image.load('assets/python_body_64px.png'))),

            80: ((pg.image.load('assets/python_80px.png'), pg.image.load('assets/c_80px.png'),
                 pg.image.load('assets/csharp_80px.png'), pg.image.load('assets/cplusplus_80px.png'),
                 pg.image.load('assets/js_80px.png'), pg.image.load('assets/java_80px.png'),
                 pg.image.load('assets/go_80px.png'), pg.image.load('assets/php_80px.png'),
                 pg.image.load('assets/rust_80px.png'), pg.image.load('assets/ruby_80px.png'),
                 pg.image.load('assets/swift_80px.png'), pg.image.load('assets/scala_80px.png'),
                 pg.image.load('assets/r_80px.png')),
                 (pg.image.load('assets/python_bodyb_80px.png'),
                  pg.image.load('assets/python_headb_80px.png'),
                  pg.image.load('assets/python_body_80px.png'))),
            120: ((pg.image.load('assets/python_120px.png'), pg.image.load('assets/c_120px.png'),
                  pg.image.load('assets/csharp_120px.png'), pg.image.load('assets/cplusplus_120px.png'),
                  pg.image.load('assets/js_120px.png'), pg.image.load('assets/java_120px.png'),
                  pg.image.load('assets/go_120px.png'), pg.image.load('assets/php_120px.png'),
                  pg.image.load('assets/rust_120px.png'), pg.image.load('assets/ruby_120px.png'),
                  pg.image.load('assets/swift_120px.png'), pg.image.load('assets/scala_120px.png'),
                  pg.image.load('assets/r_120px.png')),
                  (pg.image.load('assets/python_bodyb_120px.png'),
                  pg.image.load('assets/python_headb_120px.png'),
                  pg.image.load('assets/python_body_120px.png')))
        }

        # Assign proper assets according to square_size
        python, c, csharp, cplusplus, js, \
            java, go, php, rust, ruby, swift, scala, r = __ASSETS_SCALE[settings.square_size][0]
        self.food_images: list[Surface | SurfaceType] = [c, csharp, cplusplus, js, java, go, php, rust, ruby, swift, scala, r]
        self.forbidden_food_image: Surface | SurfaceType = python

        # Snake body in 2 classic Python colors
        self.body: Surface | SurfaceType = __ASSETS_SCALE[settings.square_size][1][0]
        self.body_yellow: Surface | SurfaceType = __ASSETS_SCALE[settings.square_size][1][2]

        # Snake image for every direction
        self.head_right: Surface | SurfaceType = __ASSETS_SCALE[settings.square_size][1][1]
        self.head_up: Surface | SurfaceType = pg.transform.rotate(self.head_right, 90)
        self.head_left: Surface | SurfaceType = pg.transform.rotate(self.head_up, 90)
        self.head_down: Surface | SurfaceType = pg.transform.rotate(self.head_left, 90)
