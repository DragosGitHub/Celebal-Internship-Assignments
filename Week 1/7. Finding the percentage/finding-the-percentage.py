if __name__ == '__main__':
    n = int(input())  # Number of students
    student_marks = {}

    # Reading student records
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))  # Converting marks to floats
        student_marks[name] = scores

    query_name = input()  # Name of the student to query

    # Calculating average marks for the queried student
    average = sum(student_marks[query_name]) / len(student_marks[query_name])

    # Printing average formatted to 2 decimal places
    print(f"{average:.2f}")
