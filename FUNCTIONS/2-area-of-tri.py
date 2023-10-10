"""
Create a function that calculates the area of a rectangle given its length and width.the parameters must have some default values.
"""

def calculate_rectangle_area(length=1, width=1):
    return length * width

area1 = calculate_rectangle_area()       
area2 = calculate_rectangle_area(3, 4) 
area3 = calculate_rectangle_area(5)

print(area1)  
print(area2)  
print(area3)  