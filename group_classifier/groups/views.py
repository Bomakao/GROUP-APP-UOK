import random
import json
from django.http import JsonResponse
from .models import Student, Group

def create_groups(request):
    # Get all students and shuffle them
    students = list(Student.objects.all())
    random.shuffle(students)

    # Clear existing groups
    Group.objects.all().delete()

    # Create groups
    group_size = 5
    groups = []
    for i in range(0, len(students), group_size):
        group = Group.objects.create(name=f"Group {i // group_size + 1}")
        group.students.add(*students[i:i+group_size])
        groups.append({
            "group_name": group.name,
            "students": [student.name for student in students[i:i+group_size]],
        })

    # Save groups to a JSON file
    with open("groups.json", "w") as file:
        json.dump(groups, file)

    return JsonResponse({"message": "Groups created successfully!", "groups": groups})
