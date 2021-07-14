# -*- coding: utf-8 -*-'
# !/usr/bin/env python
"""
created: 5/29/2021
@author: seraph★776
project:
"""


class Colors:

    @staticmethod
    def red(self):
        """red color font"""
        return f"\033[31m{self}\033[0m"

    @staticmethod
    def green(self):
        """green color font"""
        return f"\033[32m{self}\033[0m"

    @staticmethod
    def yellow(self):
        """yellow color font"""
        return f"\033[33m{self}\033[0m"


magick8BallColors = Colors()