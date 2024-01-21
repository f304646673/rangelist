#!/usr/bin/env python3
# -*- coding: utf-8; py-indent-offset:4 -*-
# ======================================================================================================================
# Copyrigth (C) 2024 fangliang <304646673@qqcom>
#
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later
# version.
#
# ======================================================================================================================

import common
from rangelist.range import Range
from rangelist.rangelist import RangeList
import unittest

class TestRangeList(unittest.TestCase):
    def test_add(self):
        rangelist = RangeList()
        rangelist.add([1, 5])
        self.assertEqual(rangelist.toString(), "[1, 5)")
        
        rangelist.add([10, 20])
        self.assertEqual(rangelist.toString(), "[1, 5) [10, 20)")
    
        rangelist.add([6, 7])
        self.assertEqual(rangelist.toString(), "[1, 5) [6, 7) [10, 20)")
        
        rangelist.add([5, 6])
        self.assertEqual(rangelist.toString(), "[1, 7) [10, 20)")
        
        rangelist.add([4, 7])
        self.assertEqual(rangelist.toString(), "[1, 7) [10, 20)")
        
        rangelist.add([-2, -1])
        self.assertEqual(rangelist.toString(), "[-2, -1) [1, 7) [10, 20)")
        
        rangelist.add([4, 8])
        self.assertEqual(rangelist.toString(), "[-2, -1) [1, 8) [10, 20)")
        
        rangelist.add([30, 40])
        rangelist.add([-2, 19])
        self.assertEqual(rangelist.toString(), "[-2, 20) [30, 40)")
        
        rangelist.add([20, 30])
        self.assertEqual(rangelist.toString(), "[-2, 40)")
        
    def test_remove(self):
        rangelist = RangeList()
        rangelist.add([1, 5])
        rangelist.remove([2, 3])
        self.assertEqual(rangelist.toString(), "[1, 2) [3, 5)")
        
        rangelist.add([6, 10])
        rangelist.remove([6, 8])
        self.assertEqual(rangelist.toString(), "[1, 2) [3, 5) [8, 10)")
        
        rangelist.remove([1, 2])
        self.assertEqual(rangelist.toString(), "[3, 5) [8, 10)")
        
        rangelist.add([-1, 2])
        rangelist.remove([1, 8])
        self.assertEqual(rangelist.toString(), "[-1, 1) [8, 10)")
        

if __name__ == '__main__':
    unittest.main()
