print("--- SCRIPT START ---", flush=True)


x = []
x.append(("Alice", 90, 95))
x.append(("Bob", 80, 75))
x.append(("Charlie", 0, 100))
x.append(("Dave", 75, 80))
x.append(("Ellen", 77, 78))

x.sort(
    key=lambda student: (
        (student[1] + student[2]) / 2,
        min(student[1], student[2]),
        student[1],
    ),
    reverse=True,
)

for student in x:
    print(student[0])
