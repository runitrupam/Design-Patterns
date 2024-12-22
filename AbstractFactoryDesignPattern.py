'''
Abstract Factory Design Pattern  --->
1. Families of products (e.g., Button, Checkbox)
2. More structured and hierarchical
3. WindowsFactory and MacFactory create multiple products 
    (Button, Checkbox)



'''

from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowButton: # inherit from Button interface if required
    def render(self):
        return f"Rendering the Window Button"

class MacButton:
    def render(self):
        return f"Rendering the Mac Button"


class WindowCheckbox:
    def render(self):
        return f"Rendering the Window Checkbox"

class MacCheckbox:
    def render(self):
        return f"Rendering the Mac Checkbox"
        
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

        
class WindowFactory(GUIFactory):
    def create_button(self): # Factory Design Pattern
        return WindowButton()

    def create_checkbox(self): # Factory Design Pattern
        return WindowCheckbox()

        
class MacFactory(GUIFactory):
    def create_button(self): # Factory Design Pattern
        return MacButton()

    def create_checkbox(self): # Factory Design Pattern
        return MacCheckbox()
        
        
if __name__ == '__main__':
    print('Abstract Factory Design Pattern ---> ')

    wf = WindowFactory()
    b1 = wf.create_button()
    c1 = wf.create_checkbox()
    print(b1.render())
    print(c1.render())
    print()
    
    mf = MacFactory()
    b1 = mf.create_button()
    c1 = mf.create_checkbox()
    print(b1.render())
    print(c1.render())
    print('\n\n')

'''
Factory Design Pattern -->
Single product (e.g., Button)
Simpler and less hierarchical
create_button in each factory

Factory Design Pattern as a Subset

The Factory Design Pattern can be considered a specialized version of the Abstract Factory where:
	•	The focus is on a single product, not a family of products.
	•	Each method in the Abstract Factory (e.g., create_button, create_checkbox)
	    acts like a simple factory for its corresponding product.

'''
print('Factory Design Pattern --->')
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class ButtonFactory:
    @staticmethod
    def create_button(os_type: str) -> Button:
        if os_type == "Windows":
            return WindowButton()
        elif os_type == "Mac":
            return MacButton()
        else:
            raise ValueError("Unsupported OS type")

# Usage
factory = ButtonFactory()
button = factory.create_button("Windows")
print(button.render())  # Output: Rendering Windows Button
print()


'''  
Output:-
Abstract Factory Design Pattern ---> 
Rendering the Window Button
Rendering the Window Checkbox

Rendering the Mac Button
Rendering the Mac Checkbox



Factory Design Pattern --->
Rendering the Window Button


'''
