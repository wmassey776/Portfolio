# -*- coding: utf-8 -*-'
# !/usr/bin/env python
"""
created: 2021-06-12
@author: Will Massey
Project: Russian Roulette/Gun class
"""

from random import shuffle, choice


class Gun:
    """This is a gun class for Russian Roulette."""
    def __init__(self):
        """Initialize attributes."""
        # True represents a loaded round.
        # False represents blank rounds.
        self.bullets = [True, False, False, False, False, False]  
        
    def spin_chamber(self) -> bool:
        """Spins Gun Chamber and discharges one bullet."""
        # Spin the chamber
        shuffle(self.bullets)
        # Bullet is selected
        bullet = self.bullets.pop()            
        return bullet

