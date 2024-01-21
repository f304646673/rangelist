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

from rangelist.range import Range
from rangelist.tools import Tools

class RangeList(object):
    def __init__(self):
        self.ranges = []

    # add a range to the list.For example, [[1, 5)] add [2, 3) is [[1, 5)].[[1, 5)] add [6, 8) is [[1, 5) [6, 8)].
    # @param other - the other range to compare with
    # @return True if the other range is overlap with this range, False otherwise
    # @throws TypeError if other is not a Range object or a list of integers
    # @throws ValueError if other is not a list of 2 integers
    def add(self, other):
        other = Range.conv(other)
        
        indexes = Tools.search_overlap(self.ranges, other)
        del_start_index = -1
        for i in indexes:
            if i[1]:
                other = self.ranges[i[0]].add(other)
                if -1 == del_start_index:
                    del_start_index = i[0]
                    
        if -1 != del_start_index:
            del self.ranges[del_start_index : indexes[-1][0]+1]
            self.ranges.insert(del_start_index, other)
        else:
            self.ranges.insert(indexes[0][0]+1, other)
        
        return self
    
    # remove the other range from this range.For example, [[1, 5) [10, 14)]] remove [2, 3) is [[1, 2) [3, 5) [10, 14)]].
    # @param other - the other range to remove from this range
    # @return - the new range after removing
    # @throws TypeError if other is not a Range object or a list of integers
    # @throws ValueError if other is not a list of 2 integers
    def remove(self, other):
        other = Range.conv(other)
        
        indexes = Tools.search_overlap(self.ranges, other)
        del_start_index = -1
        range_list_from_remove_all = []
        for i in indexes:
            if i[1]:
                range_list_from_remove = self.ranges[i[0]].remove(other)
                if range_list_from_remove != None:
                    range_list_from_remove_all.extend(range_list_from_remove)
                if -1 == del_start_index:
                    del_start_index = i[0]
        
        if -1 != del_start_index:
            del self.ranges[del_start_index : indexes[-1][0]+1]
            self.ranges[del_start_index:del_start_index] = range_list_from_remove_all
        
        return self
    
    
    # string representation of the range list
    # @return - a string representation of the range list
    def toString(self):
        return " ".join([str(r) for r in self.ranges])