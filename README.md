# Python Design Patterns Repository

This repository contains Python implementations of common design patterns:

- **Factory**
- **Abstract Factory**
- **Builder**
- **Adapter**
- **Singleton**
- **Observer**

---

## Design Patterns Overview

### 1. Factory
**Purpose**: Encapsulates object creation logic to promote loose coupling.  
**Example Use Case**: Create various animal types (`Dog`, `Cat`) using a single `create_animal` function.  


---

### 2. Abstract Factory
**Purpose**: Provides an interface to create families of related or dependent objects without specifying their concrete classes.  
**Example Use Case**: Create GUI components (`Button`, `Checkbox`) for different platforms (`Windows`, `MacOS`).  


---

### 3. Builder
**Purpose**: Separates object construction from its representation to construct complex objects step by step.  
**Example Use Case**: Construct a customizable `Pizza` with different sizes and toppings.  


---

### 4. Adapter
**Purpose**: Converts the interface of a class into another interface that clients expect, enabling integration of incompatible systems.  
**Example Use Case**: Wrap a legacy `Printer` class to work with modern `PrinterClient`.  


---

### 5. Singleton
**Purpose**: Ensures that a class has only one instance and provides a global point of access to it.  
**Example Use Case**: Manage global configurations using a single `ConfigManager` instance.  


---

### 6. Observer
**Purpose**: Defines a dependency between objects so that when one changes state, all its dependents are notified.  
**Example Use Case**: Notify multiple `Subscriber` objects when a `NewsPublisher` publishes news.  


---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Design-Patterns.git
   cd Design-Patterns
