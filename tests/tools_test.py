#!/usr/bin/env python
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
from rangelist.tools import Tools
import unittest

class TestTools(unittest.TestCase):
    def test_search(self):
        ranges = [Range(1, 5), Range(10, 20), Range(30, 40)]
        self.assertEqual(Tools.search(ranges, 0), (-1, False))
        self.assertEqual(Tools.search(ranges, 5), (0, True))
        self.assertEqual(Tools.search(ranges, 6), (0, False))
        self.assertEqual(Tools.search(ranges, 10), (1, True))
        self.assertEqual(Tools.search(ranges, 20), (1, True))
        self.assertEqual(Tools.search(ranges, 21), (1, False))
        self.assertEqual(Tools.search(ranges, 30), (2, True))
        self.assertEqual(Tools.search(ranges, 40), (2, True))
        self.assertEqual(Tools.search(ranges, 41), (2, False))
        
    def test_search_overlap(self):
        ranges = [Range(1, 5), Range(10, 20), Range(30, 40), Range(50, 60), Range(70, 80), Range(90, 100), Range(110, 120)]
        self.assertEqual(Tools.search_overlap(ranges, Range(0, 5)), [(-1, False), (0, True)])
        self.assertEqual(Tools.search_overlap(ranges, Range(0, 6)), [(-1, False), (0, True)])
        self.assertEqual(Tools.search_overlap(ranges, Range(0, 10)), [(-1, False), (0, True), (1, True)])
        self.assertEqual(Tools.search_overlap(ranges, Range(0, 11)), [(-1, False), (0, True), (1, True)])
        self.assertEqual(Tools.search_overlap(ranges, Range(0, 20)), [(-1, False), (0, True), (1, True)])
        self.assertEqual(Tools.search_overlap(ranges, Range(0, 21)), [(-1, False), (0, True), (1, True)])
        self.assertEqual(Tools.search_overlap(ranges, Range(0, 30)), [(-1, False), (0, True), (1, True), (2, True)])
        self.assertEqual(Tools.search_overlap(ranges, Range(0, 31)), [(-1, False), (0, True), (1, True), (2, True)])
        self.assertEqual(Tools.search_overlap(ranges, Range(0, 40)), [(-1, False), (0, True), (1, True), (2, True)])
        self.assertEqual(Tools.search_overlap(ranges, Range(0, 41)), [(-1, False), (0, True), (1, True), (2, True)])
        
        self.assertEqual(Tools.search_overlap(ranges, Range(1, 5)), [(0, True)])
        self.assertEqual(Tools.search_overlap(ranges, Range(1, 6)), [(0, True)])
        self.assertEqual(Tools.search_overlap(ranges, Range(1, 10)), [(0, True), (1, True)])
        self.assertEqual(Tools.search_overlap(ranges, Range(1, 11)), [(0, True), (1, True)])
        self.assertEqual(Tools.search_overlap(ranges, Range(1, 20)), [(0, True), (1, True)])
        self.assertEqual(Tools.search_overlap(ranges, Range(1, 21)), [(0, True), (1, True)])
        
        self.assertEqual(Tools.search_overlap(ranges, Range(21, 29)), [(1, False)])
        self.assertEqual(Tools.search_overlap(ranges, Range(21, 41)), [(1, False), (2, True)])
        
        self.assertEqual(Tools.search_overlap(ranges, Range(60, 66)), [(3, True)])
        self.assertEqual(Tools.search_overlap(ranges, Range(61, 66)), [(3, False)])
        self.assertEqual(Tools.search_overlap(ranges, Range(121, 121)), [])
        
if __name__ == '__main__':
    unittest.main()