import figures
from figures import triangle_perimeter
print(dir(figures))
figures.circle_area()
figures.square_perimeter()
figures.square_area()
figures.triangle_area()
triangle_perimeter()
r = int(input("Ввести радиус круга: "))
figures.circle_perimeter(r)
