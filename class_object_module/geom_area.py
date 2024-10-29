import math
class area:
    
#    import math

    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return math.pi*self.radius**2

    def cylinder_area(self, height):
        return (2*area(self.radius).circle_area())+2*math.pi*self.radius*height 

    def sphere_area(self):
        return (4/3)*math.pi*self.radius**3


if __name__ == "__main__":
    
    shape = int(input("Enter 1, 2, 3, for circle, cylinder, sphere respectively:\n"))

    r = eval(input("Enter the radius\n"))

    if shape == 1:
        print(f"area of the circle = {area(r).circle_area()}")

    elif shape == 2:
        h = eval(input("Enter the height of the cylinder\n"))
        print(f"area of the cylinder = {area(r).cylinder_area(h)}")

    elif shape == 3:
        print(f"area of the sphere = {area(r).sphere_area()}")

    else:
        print("Wrong input")

