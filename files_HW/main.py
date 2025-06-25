from grades import avg_grade
import rich

grades = []

grade = int(input("enter grade: "))
while grade != -1:
    grades.append(grade)
    grade = int(input("enter grade: "))

avg = avg_grade(grades)

rich.print(f"[bold magenta]Average:[/] [green]{avg}[/]")