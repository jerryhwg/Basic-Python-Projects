# Python 3.7.2
# Level 1
# Capitalize the first and fourth letters of a name

def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()

if __name__ == "__main__":
    print(old_macdonald('macdonald'))

# key: split name into two parts
