employees = [
    ("Asha", "IT", 60000),
    ("Ravi", "HR", 45000),
    ("Meena", "IT", 75000),
    ("Sita", "HR", 50000),
    ("Kiran", "Finance", 55000)
]

grouped = {}

for name, department, salary in employees:
    if department not in grouped:
        grouped[department] = []

    grouped[department].append((name, salary))

average = {
    department: sum(salary for name, salary in employees) / len(employees)
    for department, employees in grouped.items()
}


highest_paid = {
    department: max(employees, key=lambda x: x[1])[0]
    for department, employees in grouped.items()
}


sorted_departments = sorted(
    average,
    key=lambda x:x[1],
    reverse=True
)

# Print results
print("Grouped:", grouped)
print("Average:", average)
print("highest Paid:", highest_paid)
print("Sorted:", ", ".join(sorted_departments))