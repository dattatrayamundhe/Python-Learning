# Python program to find opposite face of dice
def opposite_face_of_dice(n):
    if n == 1:
        print(6)
    elif n == 2:
        print(5)
    elif n == 3:
        print(4)
    elif n == 4:
        print(3)
    elif n == 5:
        print(2)
    else:
        print(1)

if __name__ == "__main__":
  n = 2
  opposite_face_of_dice(n)
