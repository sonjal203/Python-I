def rectangle_area(l,w):
    return round(l * w, 4)

length = float(input("Length: "))
width = float(input("Width: "))

area = rectangle_area(length,width)

print("Area:", area)