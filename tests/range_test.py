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
import unittest

class TestRange(unittest.TestCase):
    
    def test_conv(self):
        # test conv() with parameter not a Range object or a list of integers, it will raise execption
        with self.assertRaises(TypeError) as te:
            Range.conv("a")
        self.assertEqual(str(te.exception), "other must be a Range object or a list of integers")
        
        # test conv() with parameter a list, but not a list of integers, it will raise execption
        with self.assertRaises(TypeError) as te:
            Range.conv([1, "a"])
        self.assertEqual(str(te.exception), "other must be a Range object or a list of integers")
        
        # test conv() with parameter a list, but not a list of 2 integers, it will raise execption
        with self.assertRaises(ValueError) as ve:
            Range.conv([1, 2, 3])
        self.assertEqual(str(ve.exception), "list must have 2 elements")
        
        self.assertEqual(Range.conv([1, 2]), Range(1, 2))
        self.assertEqual(Range.conv(Range(1, 2)), Range(1, 2))
        
    
    # test Range start equal end, it will raise execption "start must be < end"
    def test_init(self):
        with self.assertRaises(ValueError) as ve:
            start = 3
            end = 2
            Range(start, end)
        self.assertEqual(str(ve.exception), "start must be < end")
        
        # test Range start greater than end, it will raise execption "start must be < end"
        with self.assertRaises(ValueError) as ve:
            start = 5
            end = 3
            Range(start, end)
        self.assertEqual(str(ve.exception), "start must be < end")
        
        # test Range start not integer, it will raise execption "start and end must be integers"
        with self.assertRaises(TypeError) as te:
            start = "a"
            end = 3
            Range(start, end)
        self.assertEqual(str(te.exception), "start and end must be integers")
        
        # test Range end not integer, it will raise execption "start and end must be integers"
        with self.assertRaises(TypeError) as te:
            start = 3
            end = "a"
            Range(start, end)
        self.assertEqual(str(te.exception), "start and end must be integers")
        
        # test Range start greater than 2**32, it will raise execption "start and end must be <= 2**32"
        with self.assertRaises(OverflowError) as oe:
            start = 2**32+1
            end = 3
            Range(start, end)
        self.assertEqual(str(oe.exception), "start and end must be <= 2**32")
        
        # test Range end greater than 2**32, it will raise execption "start and end must be <= 2**32"
        with self.assertRaises(OverflowError) as oe:
            start = 3
            end = 2**32+1
            Range(start, end)
        self.assertEqual(str(oe.exception), "start and end must be <= 2**32")
        
        start = 3
        end = 5
        originRange = Range(start, end)
        self.assertEqual(str(originRange), "[3, 5)")
        
        
    def test_remove(self):
        # test Range start less than right start, and Range end large than right end，it will raise execption
        # left Range: [3, 5) right Range: [1, 2), raise execption "right range must be overlap with this range"
        with self.assertRaises(TypeError) as te:
            start = 3
            end = 5
            left = Range(start, end)
            left.remove("a")
        self.assertEqual(str(te.exception), "other must be a Range object or a list of integers")
        
        # test Range start equal right start, it will return []
        # left Range: [3, 5) right Range: [3, 5), result is []
        start = 3
        end = 5
        left = Range(start, end)
        right = Range(start, end)
        self.assertEqual(left.remove(right), [])
        
        # test Range start equal right end, it will return left Range
        # left Range: [3, 5) right Range: [5, 6), result is [3, 5)
        start = 3
        end = 5
        left = Range(start, end)
        right = Range(end, end+1)
        self.assertEqual(left.remove(right), [left])
        
        # test Range end equal right start, it will return left Range
        # left Range: [3, 5) right Range: [2, 3), result is [3, 5)
        start = 3
        end = 5
        left = Range(start, end)
        right = Range(start-1, start)
        self.assertEqual(left.remove(right), [left])
        
        # test Range end equal right end, it will return range(right.end, self.end-1)
        # left Range: [3, 5) right Range: [4, 5), result is [3, 4)
        start = 3
        end = 5
        left = Range(start, end)
        right = Range(end-1, end)
        self.assertEqual(left.remove(right), [Range(start, end-1)])
        
        # test Range start large than right start, and Range end less than right end, it will return []
        # left Range: [3, 5) right Range: [2, 6), result is []
        start = 3
        end = 5
        left = Range(start, end)
        right = Range(start-1, end+1)
        self.assertEqual(left.remove(right), [])
        
        # test Range start less than right start, and Range end large than right end, it will return a range list
        # left Range: [1, 10) right Range: [3, 5), result is [[1, 3),[5, 10)]
        start = 1
        end = 10
        left = Range(start, end)
        right = Range(start+2, start+4)
        self.assertEqual(left.remove(right), [Range(start, start+2), Range(start+4, end)])
        
        # test Range start less than right start, and Range end equal right end, it will return a range list
        # left Range: [3, 5) right Range: [1, 2), result is [3, 5)
        start = 3
        end = 5
        left = Range(start, end)
        right = Range(start-2, start-1)
        self.assertEqual(left.remove(right), [left])
        
        # test Range start less than right start, and Range end equal right end, it will return a range list
        # left Range: [3, 5) right Range: [6, 7), result is [3, 5)
        start = 3
        end = 5
        left = Range(start, end)
        right = Range(end+1, end+2)
        self.assertEqual(left.remove(right), [left])
        
        # test Right start equal Range end and Right start, it will return Range(start, right.end)
        # left Range: [3, 5) right Range: [5, 5), result is [3, 5)
        start = 3
        end = 5
        left = Range(start, end)
        right = Range(end, end)
        self.assertEqual(left.remove(right), [left])
        
    def test_add(self):      
        # test Range start less than right start, and Range end large than right end，it will raise execption
        # left Range: [3, 5) right Range: [1, 2), raise execption "right range must be overlap with this range"
        with self.assertRaises(ValueError) as ve:
            start = 3
            end = 5
            left = Range(start, end)
            left.add([start-2, start-1])
        self.assertEqual(str(ve.exception), "other range must be overlap with this range")
        
        # test Range start less than right start, and Range end equal right end, it will raise execption
        # left Range: [3, 5) right Range: [6, 7), raise execption "right range must be overlap with this range"
        with self.assertRaises(ValueError) as ve:
            start = 3
            end = 5
            left = Range(start, end)
            left.add([end+1, end+2])
        self.assertEqual(str(ve.exception), "other range must be overlap with this range")
        
        with self.assertRaises(TypeError) as te:
            start = 3
            end = 5
            left = Range(start, end)
            left.add("a")
        self.assertEqual(str(te.exception), "other must be a Range object or a list of integers")
        
        # test Range start equal right start, it will return left Range
        # left Range: [3, 5) right Range: [3, 5), result is [3, 5)
        start = 3
        end = 5
        left = Range(start, end)
        self.assertEqual(left.add([start, end]), left)
        
        # test Range start equal right end, it will return left Range
        # left Range: [3, 5) right Range: [5, 5), result is [3, 5)
        start = 5
        end = 5
        left = Range(start, end)
        self.assertEqual(left.add([start, end]), left)
        
        # test Range start equal right end, and Range end less than right end, it will return left Range(start, right.end)
        # left Range: [3, 5) right Range: [5, 6), result is [3, 6)
        start = 3
        end = 5
        left = Range(start, end)
        self.assertEqual(left.add([end, end+1]), Range(start, end+1))
        
        # test Range end equal right start, it will return left Range
        # left Range: [3, 5) right Range: [2, 3), result is [2, 5)
        start = 3
        end = 5
        left = Range(start, end)
        self.assertEqual(left.add([start-1, start]), Range(start-1, end))
        
        # test Range end equal right end, it will return range(right.end, self.end-1)
        # left Range: [3, 5) right Range: [4, 5), result is [3, 5)
        start = 3
        end = 5
        left = Range(start, end)
        self.assertEqual(left.add([end-1, end]), left)
        
        # test Range start large than right start, and Range end less than right end, it will return None
        # left Range: [3, 5) right Range: [2, 6), result is [2, 6)
        start = 3
        end = 5
        left = Range(start, end)
        self.assertEqual(left.add([start-1, end+1]), Range(start-1, end+1))
        
        # test Right start equal Range end and Right start, it will return Range(start, right.end)
        # left Range: [3, 5) right Range: [5, 5), result is [3, 5)
        start = 3
        end = 5
        left = Range(start, end)
        self.assertEqual(left.add([end, end]), Range(start, end))
 
        
    def test_overlap(self):
        # test Range start less than right start, and Range end large than right end，it will raise execption
        # left Range: [3, 5) right Range: [1, 2), raise execption "right range must be overlap with this range"
        with self.assertRaises(TypeError) as te:
            start = 3
            end = 5
            left = Range(start, end)
            left.overlap("a")
        self.assertEqual(str(te.exception), "other must be a Range object or a list of integers")
        
        # test Range start equal right start, it will return True
        # left Range: [3, 5) right Range: [3, 5), result is True
        start = 3
        end = 5
        left = Range(start, end)
        right = Range(start, end)
        self.assertEqual(left.overlap(right), True)
        
        # test Range start equal right end, it will return False
        # left Range: [3, 5) right Range: [5, 6), result is True
        start = 3
        end = 5
        left = Range(start, end)
        right = Range(end, end+1)
        self.assertEqual(left.overlap(right), True)
        
        # test Range end equal right start, it will return False
        # left Range: [3, 5) right Range: [2, 3), result is True
        start = 3
        end = 5
        left = Range(start, end)
        right = Range(start-1, start)
        self.assertEqual(left.overlap(right), True)
        
        # test Range end equal right end, it will return True
        # left Range: [3, 5) right Range: [4, 5), result is True
        start = 3
        end = 5
        left = Range(start, end)
        right = Range(end-1, end)
        self.assertEqual(left.overlap(right), True)
        
        # test Range start large than right start, and Range end less than right end, it will return True
        # left Range: [3, 5) right Range: [2, 6), result is True
        start = 3
        end = 5
        left = Range(start, end)
        right = Range(start-1, end+1)
        self.assertEqual(left.overlap(right), True)
        
        # test Range start less than right start, and Range end large than right end, it will return False
        # left Range: [3, 5) right Range: [1, 2), result is False
        start = 3
        end = 5
        left = Range(start, end)
        right = Range(start-2, start-1)
        self.assertEqual(left.overlap(right), False)
        
        
if __name__ == '__main__':
    unittest.main()