def calculate_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return areas

radius_input = input("Enter the radius of the circle: ")
radius = int(radius_input)

circle_area = calculate_area(radius)
print("The area of the circle is:", circle_area)


'''
    The first bug is on the line return areas. The variable areas is not defined in the function. 
    The correct variable name is area.

    The second bug is on the line radius = int(radius_input). If the user enters a non-integer value, 
    this line will raise a ValueError. To fix this, you should use a try-except block to handle the error.

    The third bug is on the line print("The area of the circle is:", circle_area). 
    If the calculate_area function raises an error (for example, because of the first bug), this line will not be executed, and the user will not see any output. To fix this, you should move the print statement inside a try-except block, so that it is executed even if there is an error.

    '''
