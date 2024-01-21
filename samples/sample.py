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
from rangelist.rangelist import RangeList

def main():
    # create a RangeList object
    rl = RangeList()

    # add a range
    rl.add([1, 5])
    print(rl.toString())

    # add another range
    rl.add([10, 20])
    print(rl.toString())

    # add another range
    rl.add([20, 20])
    print(rl.toString())

    # add another range
    rl.add([20, 21])
    print(rl.toString())

    # add another range
    rl.add([2, 4])
    print(rl.toString())

    # add another range
    rl.add([3, 8])
    print(rl.toString())

    # remove a range
    rl.remove([10, 10])
    print(rl.toString())

    # remove a range
    rl.remove([10, 11])
    print(rl.toString())

    # remove a range
    rl.remove([15, 17])
    print(rl.toString())

    # remove a range
    rl.remove([3, 19])
    print(rl.toString())

    # remove a range
    rl.remove([3, 21])
    print(rl.toString())
    
if __name__ == '__main__':
    main()