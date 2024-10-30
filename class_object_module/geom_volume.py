import math
import geom_area

class volume:

    def __init__(self, rad):
        self.rad = rad

    def cylinder_volume(self, ht):
        return geom_area.area(self.rad).circle_area()*ht
        


if __name__ == "__main__":

    R = eval(input("Enter the radius\n"))
    H = eval(input("Enter the height of the cylinder\n"))
    print(f"Volume of the cylinder = {volume(R).cylinder_volume(H)}")
