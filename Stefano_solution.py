"""
    Author: Stefano Veglia
    Student ID: 001270412
"""
import ast

"""
The list point will store the random generated point once they are created or imported from a text file.
The list quadrants has 4 nested lists to divide the points for each of the q.
"""
points = []
quadrants = [[], [], [], []]

# in the following lines of code the program took his inputs from a text file
with open("mock_test1.txt", "r") as points_file:
    for line in points_file:
        points.append(ast.literal_eval(line.strip()))


def sort_axis(point):
    """
    The function sort_axis will check in first place if the point is in the origin or on one the axis.
    If the point lays in the center we just skip it cause will not be a possible target.
    If the point lies on the y-axis we need to check the sign of the x. If positive we insert the point at the beginning
    of the quadrant[0] cause is angle is going to be 0. If negative we insert the point as first element of quadrant[2].
    Same procedure for the point on the x-axis.
    If not then will start to check in which of the quadrant is placed based on the combination of sign of x and y.
    Once we find in which quadrant the point lays we apply the function head_tail to place it in the right place.
    :param point:
    :return:
    """
    if point[0] == 0 or point[1] == 0:
        if point[0] == point[1] == 0:  # check if the point is in the origin
            pass

        elif point[0] == 0:  # check if the point on the y-axis
            if point[1] > 0:
                quadrants[0].insert(0, point)
            else:
                quadrants[2].insert(0, point)
        elif point[1] == 0:  # check if the point on the x-axis
            if point[0] > 0:
                quadrants[1].insert(0, point)
            else:
                quadrants[3].insert(0, point)
    else:
        if point[0] > 0 and point[1] > 0:  # check if the point is in the first quadrant.
            head_tail(point, quadrants[0])
        elif point[0] > 0 > point[1]:  # check if the point is in the second quadrant.
            head_tail(point, quadrants[1])
        elif point[0] < 0 and point[1] < 0:  # check if the point is in the third quadrant.
            head_tail(point, quadrants[2])
        elif point[0] < 0 < point[1]:  # check if the point is in the forth quadrant.
            head_tail(point, quadrants[3])


def check_ratio(point):
    """
    This function calculate the ratio between x and y. Base on the ratio we can sort the points in their quadrant list.
    :param point: Given point.
    :return: The ratio between x and y.
    """
    if point[1] == 0:
        return 0
    return point[0] / point[1]


def head_tail(value, quadrant):
    """
    This function is called by sort_axis and takes as argument a point and the list where it's been assigned.
    If the list is empty is going to place the point in the list straight away.
    The function also check if the ratio value of the point is less of the first value in the list, in the case place
    the point at the beginning of the list.
    Also check if the ratio value of the point is greater of the last value in the list, in the case place the point at
    the end of the list.
    :param value: the given point.
    :param quadrant: The nest list of quadrant where we are going to place the point.
    :return:
    """
    if not quadrant:
        quadrant.append(value)
    elif check_ratio(value) <= check_ratio(quadrant[0]):  # ratio less than the first point.
        quadrant.insert(0, value)  # stored at the beginning of the list.
    elif check_ratio(value) >= check_ratio(quadrant[-1]):  # ratio greater than the last point.
        quadrant.append(value)  # stored at the end of the list.
    else:
        binary_insertion_sort(quadrant, value)


def binary_insertion_sort(quadrant, value):
    """
    This is a recursive function that use the principal of binary search to find where to store the point correctly in
    the list in order base of their ratio between x and y.
    First we find the index of the point in the middle of the list and assign it to n.
    We check if the ratio of the point (value) is less or equal the ratio of n.
    If true we check if the ratio of the point (value) is greater or equal the ratio of n-1.
    If true we know we can place the point at index n in the list.
    if false we call recursively the function, this time with the second half of the list as an argument.
    If the ratio of the point (value) is not less or equal the ratio of n, we check if il less or equal of the ratio of
    n+1. If true we know we can place the point at index n+1 in the list.
    if false we call recursively the function, this time with the first half of the list as an argument.
    :param value: the given point.
    :param quadrant: The nest list of quadrant where we are going to place the point.
    :return:
       """
    n = int(len(quadrant) / 2)
    if check_ratio(value) <= check_ratio(quadrant[n]):  # r. of value < or = to r. of n
        if check_ratio(value) >= check_ratio(quadrant[n-1]):    # r. of value > or = to r. of n-1
            quadrant.insert(n, value)   # insert at index n
        else:
            binary_insertion_sort(quadrant[:n], value)  # recursively call the function with the second half of the list
    else:   # r. of value > of the r. of n
        if check_ratio(value) <= check_ratio(quadrant[n+1]):    # r. of value < or = to r. of n+1
            quadrant.insert(n+1, value)  # insert at index n+1
        else:
            binary_insertion_sort(quadrant[n:], value)  # recursively call the function with the first half of the list


def main(random_points):
    for each in random_points:
        sort_axis(each)
    return quadrants[0]+quadrants[1]+quadrants[2]+quadrants[3]


print(main(points))
