# Python 3.7.2
# Level 1
# Return a string where for every character in the original there are three characters

def paper_doll(text):
    result = ''
    for char in text:
        result += char*3
    return result

if __name__ == "__main__":
    print(paper_doll('Hello'))

# key: result = ''
# key: result += char*3