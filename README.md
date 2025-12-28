# Student Gradebook System
A developed student grade input system that gathers a list of students, takes the average of each student of their inputted grades, and uses a heap algorithms for student ranking regarding their grade performance. Once all calculations are made and the needed information is gathered for the gradebook, it is then saved for viewing as a .txt file after full program execution.

The main goal of this project is to maintain understanding of computer science fundamentals regarding data structures and algorithms, saving data to a file, and python syntax.


# Deeper Analysis
## Time and Space Complexity

n = number of students

m = average number of grades per student

g = n × m = total number of grades entered


### Detecting student names
```
detect_list_of_students(student_input)
```
.replace() scans the input string → O(n)
.split() scans again → O(n)
List comprehension loops through names → O(n)

### Entering grades
```
for student in students:
    while True:
        grade = input(...)
```
Each student enters m grades:
Total grades processed = n × m = g
Each append is O(1)

So:

O(nm) = O(g)

### Building the heap (ranking)
```
heapq.heappush(ranking, (-avg, name))
```
Each push = O(log n)
For n students → O(n log n)

### Sorting ranking
```
sorted(ranking)
```
Sorting n students → O(n log n)

### Writing to a file
Also recomputes sums:

→ O(nm)

## Total Time Complexity
O(nm) + O(n log n) = O(nm)
linear in the total number of grades.

## Space Complexity

| Structure              | Space     |
| ---------------------- | --------- |
| `students` list        | O(n)      |
| `gradebook` dictionary | O(n) keys |
| All grade lists        | O(nm)     |
| `ranking` heap         | O(n)      |

total space - O(nm)
