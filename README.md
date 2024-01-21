# Description
This project is used to calculate the rangelist related operations.
RangeList is a Python class that provides the add method for adding new compartments to it. Like what

    rl = RangeList()
    # add a range
    rl.add([1, 5])
    print(rl.toString()) # [1, 5)

The remove method is also provided for a specific interval of the interval. Like what

    rl.add([2, 3])
    print(rl.toString()) # [1, 2) [3, 5)
