#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
# ======================================================================================================================
# Copyrigth (C) 2024 fangliang <304646673@qq.com>
# 
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later
# version.
#
# ======================================================================================================================

class Range(object):        
      
    # initialize the Range object
    # @param start the start of the range
    # @param end the end of the range
    # @throws TypeError if start or end is not an integer
    # @throws OverflowError if start or end is too large
    # @throws ValueError if start > end
    def __init__(self, start, end):
        if type(start) != int or type(end) != int:
            raise TypeError("start and end must be integers")
        if start > 2**32 or end > 2**32:
            raise OverflowError("start and end must be <= 2**32")
        if start >= end:
            raise ValueError("start must be < end")
        
        self.start = start
        self.end = end
        
    # string representation of the range
    # @return the string representation of the range
    def __repr__(self) -> str:
        return f"[{self.start}, {self.end})"
        
    # equal operator
    # @return the string representation of the range
    def __eq__(self, __value: object) -> bool:
        return self.start == __value.start and self.end == __value.end
        
      
    # check if the other range is overlap with this range.For example, [1, 5) is overlap with [2, 3) but not overlap with [7, 9),but [5, 6) is overlap with [1, 5).
    # @param other the other range to compare with
    # @return True if the other range is overlap with this range, False otherwise
    # @throws TypeError if other is not a Range object or a list of integers
    # @throws ValueError if other is not a list of 2 integers
    def overlap(self, other) -> bool:
        other = self.conv(other)
        return self.start <= other.end and self.end >= other.start
        
    # remove the other range from this range.For example, [1, 5) remove [2, 3) is [1, 2) [3, 5).
    # @param other - the other range to remove from this range.the other range must be a Range object or a list of 2 integers
    # @return - a list of Range objects that are the result of removing other from this range
    # @throws TypeError if other is not a Range object or a list of integers
    # @throws ValueError if other is not a list of 2 integers
    def remove(self, other) -> object:
        other = self.conv(other)
        
        if self.end < other.start or self.start > other.end:
            return [self]
        if self.start >= other.start and self.end <= other.end:
            return None
        if self.start >= other.start and self.end > other.end:
            return [Range(other.end, self.end)]
        if self.start < other.start and self.end <= other.end:
            return [Range(self.start, other.start)]
        if self.start < other.start and self.end > other.end:
            return [Range(self.start, other.start), Range(other.end, self.end)]
        
    # add the other range to this range.For example, [1, 5) add [5, 7) is [1, 7).
    # @param other - the other range to add to this range
    # @return - the new range after adding
    # @throws TypeError if other is not a Range object or a list of integers
    # @throws ValueError if other is not a list of 2 integers
    # @throws TypeError if other range is not overlap with this range
    def add(self, other) -> object:
        other = self.conv(other)
        
        if self.end < other.start or self.start > other.end:
            raise ValueError("other range must be overlap with this range")
        if self.start >= other.start and self.end <= other.end:
            return Range(other.start, other.end)
        if self.start >= other.start and self.end > other.end:
            return Range(other.start, self.end)
        if self.start < other.start and self.end <= other.end:
            return Range(self.start, other.end)
        if self.start < other.start and self.end > other.end:
            return Range(self.start, self.start)
        
    # convert other to a Range object.For example, [1, 5) is a Range object, [1, 5] is a list of 2 integers.
    # @param other - a Range object or a list of integers
    # @return - a Range object
    # @throws TypeError if other is not a Range object or a list of integers
    # @throws ValueError if other is not a list of 2 integers
    @classmethod
    def conv(self, other) -> object:
        if type(other) == list:
            if len(other) != 2:
                raise ValueError("list must have 2 elements")
            if type(other[0]) != int or type(other[-1]) != int:
                raise TypeError("other must be a Range object or a list of integers")
            return Range(other[0], other[-1])
        elif type(other) != Range:
            raise TypeError("other must be a Range object or a list of integers")
        
        return other