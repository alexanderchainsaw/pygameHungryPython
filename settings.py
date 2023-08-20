from dataclasses import dataclass


@dataclass
class Settings:
    """Lower level class to store basic configuration settings"""
    width: int
    height: int
    square_size: int
    squares_x: int
    squares_y: int
