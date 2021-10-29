def calc_new_height():
    height = dw * ch / cw
    return height


cw = int(input("Enter the current width: "))
ch = int(input("Enter the current height: "))
dw = int(input("Enter the desired width: "))
print("The corresponding height is: ", calc_new_height())
print(calc_new_height())
