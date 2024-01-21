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

from rangelist.range import Range

class Tools(object):          
        
    # search the index of the range which contains the value.First value is the index of the range where to compare with the value, 
    # second value is True if the range contains the value, False otherwise.  
    # @param ranges - the list of ranges
    # @param value - the value to search
    # @param start_index - the start index of the ranges to search
    # @return the index of the range where to compare with the value, True if the range contains the value, False otherwise
    @staticmethod
    def search(ranges, value, start_index = 0):
        if start_index < 0:
            start_index = 0
        end_index = len(ranges) - 1
        while start_index <= end_index:
            mid = (start_index + end_index) // 2
            if ranges[mid].start <= value and ranges[mid].end >= value:
                return (mid, True)
            elif ranges[mid].end < value:
                start_index = mid + 1
            else:
                end_index = mid - 1
        
        return (end_index, False)
    
    # search the index of the ranges which overlap with the search range.
    # First value is the index of the range where to compare with the value, second value is True if the range contains the value,
    # False otherwise.
    # @param ranges - the list of ranges
    # @param search_range - the range to search
    # @return a list of (index, overlap) of the ranges which overlap with the search range
    @staticmethod
    def search_overlap(ranges, search_range):
        start = Tools.search(ranges, search_range.start)
        end = Tools.search(ranges, search_range.end, start[0])
        index_list = [start]
        for i in range(start[0]+1, end[0]+1):
            index_list.append((i, True))
        return index_list

    