"""

    Person - a class to represent a person with attributes like name, age, and gender.
    Car - a class to represent a car with attributes like make, model, year, and color.
    Animal - a class to represent an animal with attributes like species, weight, and habitat.
    BankAccount - a class to represent a bank account with attributes like account number, balance, and owner.
    Employee - a class to represent an employee with attributes like name, job title, and salary.
    
"""

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_name(self):
        print(self.name)
        
    def get_age(self):
        print(self.age)
        
    def get_gender(self):
        print(self.gender)
    

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year
    
    def get_color(self):
        return self.color
    
    def start_engine():
        print("The engine has been turned on.")
    
    def stop_engine():
        print("The engine has been turned off.")


class Animal:
    def __init__(self, species, weight, habitat):
        self.species = species
        self.weight = weight
        self.habitat = habitat
        
    def get_species(self):
        return self.species
    
    def get_weight(self):
        return self.weight
    
    def get_habitat(self):
        return self.habitat
    
    def get_sound(self):
        if (self.species == "bird"):
            print("Chirp! Chirp! Chirp!")
        elif (self.species == "cat"):
            print("Purrrr....purrr...")
        else:
            print("What does the fox say?")
    
    
class BankAccount:
    def __init__(self, acct_num, balance, owner):
        self.acct_num = acct_num
        self.balance = balance
        self.owner = owner
    
    def get_acct_num(self):
        return self.acct_num
    
    def get_balance(self):
        return self.balance
    
    def get_owner(self):
        return self.owner
    
    def deposit(self):
        print('Your current balance is: ', self.balance)
        x = int(input("Enter an amount to deposit: "))
        self.balance += x
        print("Your new balance is: ", self.balance)
        
    def withdraw(self):
        print('Your current balance is: ', self.balance)
        x = int(input("Enter an amount to withdraw: "))
        self.balance -= x
        print("Your new balance is: ", self.balance)

# my_bank = BankAccount(182333, 100, "Ben")
# my_bank.deposit()
# my_bank.withdraw()


class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title
        self.salary = salary
    
    def get_name(self):
        return self.name
    
    def get_job_title(self):
        return self.job_title
    
    def get_salary(self):
        return self.salary
    
    def promote(self):
        print("Previous title: ", self.job_title)
        self.job_title = "Vice President"
        print("Congratulations! You are now ", self.job_title)
        
    def raise_salary(self):
        print("Current salary: ", self.salary)
        self.salary += 10000
        print("New Salary: ", self.salary)    

# emp1 = Employee("Ben", "Manager", 98000)
# emp1.promote()
# emp1.raise_salary()


class Book:
    def __init__(self, title, author, pub_year):
        self.title = title
        self.author = author
        self.pub_year = pub_year
        
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_pub_year(self):
        return self.pub_year
    
    def borrow(self):
        print(f"You borrow {self.title}, of which {self.author} is the author.")
        
    def return_book(self):
        print(f"You return {self.title}.")
    
# book1 = Book("Dancing with Wolves", "Ben Clark", 1995)    
# book1.borrow()
# book1.return_book()
        
class Circle:
    def __init__(self, radius, diameter):
        self.radius = radius
        self.diameter = diameter
   
    def get_radius(self):
       return self.radius
   
    def get_diameter(self):
       return self.diameter
    
    def get_circumference(self):
        return(2 * 3.14159 * self.radius)
        
    def get_area(self):
        return(3.14159 * self.radius ** 2)
        
# my_circle = Circle(5, 10)    
# print(my_circle.get_circumference())
# print(my_circle.get_area())


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
  
    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
    
    def get_perimeter(self):
        return((2 * self.width) + (2 * self.length))
    
    def get_area(self):
        return(self.length * self.width)
    
# my_rectangle = Rectangle(10, 20)
# print(my_rectangle.get_perimeter())
# print(my_rectangle.get_area())
        
    
class Movie:
    def __init__(self, title, director, release_date):
        self.title = title
        self.director = director
        self.release_date = release_date
        
    def get_title(self):
        return self.title
    
    def get_director(self):
        return self.director
    
    def get_release_date(self):
        return self.release_date
    
    def watch(self):
        print(f"You place '{self.title}' into your dvd player and watch it.")
        
    def stop_watching(self):
        print(f"You stop watching '{self.title}.'")
        
# my_movie = Movie("Deadliest Catch", "Benjamin", 2020)
# my_movie.watch()
# my_movie.stop_watching()        
        

class Course:
    def __init__(self, name, instructor):
        self.name = name
        self.instructor = instructor
        self.students = list()
        
    def get_name(self):
        return self.name
    
    def get_instructor(self):
        return self.instructor
    
    def get_students(self):
        return self.students
    
    def add_student(self):
        x = input("Add Student name: ")
        self.students.append(x)
        
    def remove_student(self):
        x = input("Remove Student name: ")
        self.students.remove(x)
    

# compSci = Course("Computer Science", "Dr. PhD")
# print(compSci.get_students())
# compSci.add_student()
# print(compSci.get_students())
# compSci.add_student()
# print(compSci.get_students())
# compSci.remove_student()
# print(compSci.get_students())
    
    
    
"""
    Book - a class to represent a book with attributes like title, author, and publication year.
    Circle - a class to represent a circle with attributes like radius and diameter.
    Rectangle - a class to represent a rectangle with attributes like length and width.
    Movie - a class to represent a movie with attributes like title, director, and release date.
    Course - a class to represent a course with attributes like name, instructor, and students.
"""

