import sqlite3
with sqlite3.connect('person.db') as conn:
    c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS Departments''')
c.execute('''DROP TABLE IF EXISTS Employees''')

c.execute('''CREATE TABLE IF NOT EXISTS Departments(
DepartmentID INTEGER NOT NULL,
DepartmentName NOT NULL)''')

c.execute('''CREATE TABLE IF NOT EXISTS Employees(
EmployeeID INTEGER,
FirstName NOT NULL,
LastName NOT NULL,
DepartmentID INTEGER NOT NULL,
FOREIGN KEY(DepartmentID) REFERENCES Departments(DepartmentID))''')

c.execute('''INSERT INTO Departments(DepartmentID, DepartmentName)
VALUES (101, 'HR'), (102, 'IT'), (103, 'Salary')''')

c.execute('''INSERT INTO Employees(EmployeeID,FirstName, LastName, DepartmentID)
VALUES (1,'ERZHAN','AKMATALIEV', 101), (2,'ELBAK', 'GULAMIDINOV', 101),
(3,'MUSI', 'ERMA', 102), (4,'AZIZ', 'ERMA', 102),
(5,'BUSU', 'JUNUS', 103), (6,'MIRBA', 'JUNUS',103)''')

c.execute('''SELECT Employees.EmployeeID, Employees.FirstName, Employees.LastName, Departments.DepartmentName
FROM Employees
JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID''')

print('все работающие')
for i in c.fetchall():
    print(i)

c.execute('''SELECT Employees.EmployeeID, Employees.FirstName, Employees.LastName, Departments.DepartmentName
FROM Employees
JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
WHERE Departments.DepartmentName = 'IT' ''')

print('работающие в  IT')
for i in c.fetchall():
    print(i)









