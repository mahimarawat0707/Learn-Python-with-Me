# Classes in Python

## What is a Class?
- A **class** is a **blueprint** for creating objects.  
- It defines **attributes (variables)** and **methods (functions)** that describe how an object behaves.  
- Classes help organize code, making it more **modular**, **reusable**, and **object-oriented**.

---

## The `__init__()` Method
- The `__init__()` method is called **automatically** when an object is created from a class.  
- It’s known as the **constructor**.  
- Used to **initialize** object properties.  
- The keyword **`self`** represents the **current instance** of the class.

---

## Example Concept: The Dog Class
- A `Dog` class might have:
  - **Attributes** like `name` and `legs`.  
  - **Methods** like `speak()` that define actions the dog can perform.  
- When a new dog is created (an object), it automatically gets the properties defined in the class.

---

## 🔹 Objects and Instances
- Each **object** is a **separate instance** of a class.  
- Example Concepts:  
  - `my_dog` could be `"Rover"`  
  - `another_dog` could be `"Fluffy"`  
- Both are **different objects**, but created from the **same class**.

---

## 🔹 Method Behavior
- The `speak()` method in the `Dog` class makes each dog “speak.”  
- When called, it uses the dog’s name and prints a message like:
  - **Rover Says: Bark**  
  - **Fluffy Says: Bark**

---

## 🧠 Key Takeaways
- A **class** is a template; an **object** is an instance.  
- Use `__init__()` to initialize attributes.  
- Use `self` to refer to the current object.  
- Each object can use the same method but maintain its own unique data.  
- Classes are the foundation of **Object-Oriented Programming (OOP)** in Python.

---
