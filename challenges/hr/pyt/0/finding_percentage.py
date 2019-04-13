# 20190319

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        #print(name)
        #print(*line)
        scores = list(map(float, line))
        #print("scores", scores)
        student_marks[name] = scores
        #print(student_marks)
    query_name = input()
    #print(query_name)
    #print(student_marks[query_name])
    #print(sum(student_marks[query_name])/3)
    print(format(sum(student_marks[query_name])/3, '.2f')) # key: return a number in 2f format