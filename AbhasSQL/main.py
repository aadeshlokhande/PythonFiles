import sqlite3

sqlaa = sqlite3.connect("Students.db")
sql = sqlaa.cursor()

# sql.execute("""CREATE TABLE Departments (
#     dept_id INT PRIMARY KEY,
#     dept_name VARCHAR(10)
# );""")

# sql.execute("""INSERT INTO Departments (dept_id, dept_name) VALUES
# (1, 'HR'),
# (2, 'IT'),
# (3, 'Finance');""")


# a = sql.execute("select * from Departments;")

# sql.execute("""CREATE TABLE Employees (
#     emp_id INT PRIMARY KEY,
#     emp_name VARCHAR(10),
#     salary INT,
#     dept_id INT,
#     FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
# );""")

# sql.execute("""
# INSERT INTO Employees (emp_id, emp_name, salary, dept_id) VALUES
# (1, 'Aadesh', 50000, 2),
# (2, 'Rahul', 45000, 2),
# (3, 'Sneha', 60000, 3),
# (4, 'Komal', 40000, 1),
# (5, 'Priya', 60000, 3);

# """)

# a = sql.execute(""" SELECT emp_name
# FROM Employees
# WHERE dept_id IN (
#     SELECT dept_id
#     FROM Employees
#     GROUP BY dept_id
#     HAVING AVG(salary) > 50000
# );
#  """)

a = sql.execute("""
    

""")
# sqlaa.commit()
for i in a:
    print(i)