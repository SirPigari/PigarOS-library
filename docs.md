# PigarOS Python Library Documentation

## Functions

### colorprint(text, color="reset", bold=False)
Prints text with color and formatting.
#### Example:
- `colorprint("Hello, World!", "blue", True)`

### covert_hex_to_rgb(hex_color='#ffffff')
Converts a hexadecimal color code to an RGB tuple.
#### Example:
- `print(covert_hex_to_rgb("#00ff00"))`

## Classes

### window
A class for creating GUI windows.

#### Methods
- `add_tab(title)`: Adds a tab to the window.
- `remove_tab(title)`: Removes a tab from the window.
- `show_mouse_coordinates(event)`: Displays mouse coordinates on right-click (Ctrl + Right-click for continuous display).
- `config(**kwargs)`: Configures the window.
- `add_button(title, function=None, x=None, y=None, **kwargs)`: Adds a button to the window.
- `add_checkbox(title, variable=None, function=None, x=None, y=None, **kwargs)`: Adds a checkbox to the window.
- `add_label(label, x=None, y=None, font=None, function=None, bg=None, fg=None)`: Adds a label to the window.
- `add_betterButton(title, function=None, x=None, y=None, **kwargs)`: Adds a themed button to the window.
- `add_Input(id=None, x=None, y=None)`: Adds an input field to the window.
- `add_BetterInput(id=None, x=None, y=None)`: Adds a themed input field to the window.
- `input_get(id)`: Retrieves text from an input field.
- `add_image(file, function=None, x=None, y=None, px=None, open=False)`: Adds an image to the window.
- `move_shape(shape_name, direction, px)`: Moves a shape on the canvas.
- `hide_checkbox(title)`: Hides a checkbox.
- `show_checkbox(title)`: Shows a hidden checkbox.
- `remove_checkbox(title)`: Removes a checkbox.
- `hide_label(label_text)`: Hides a label.
- `show_label(label_text)`: Shows a hidden label.
- `remove_label(label_text)`: Removes a label.
- `hide_image(name)`: Hides an image.
- `show_image(name)`: Shows a hidden image.
- `remove_image(name)`: Removes an image.
- `hide_button(name)`: Hides a button.
- `show_button(name)`: Shows a hidden button.
- `remove_button(name)`: Removes a button.
- `kill()`: Destroys the window.
- `exit()`: Quits the window.
- `run()`: Runs the window main loop.

### menu
A class for creating menus in GUI windows.

#### Methods
- `add_submenu(title, menu)`: Adds a submenu to the menu.
- `add_action(title, function)`: Adds an action to the menu.
- `add_bare_item(text)`: Adds a bare item to the menu.
- `add_checkbox(title, variable, function)`: Adds a checkbox to the menu.
- `add_array_item(options, function)`: Adds an array item to the menu.
- `show(x, y)`: Displays the menu at the specified position.
- `hide()`: Hides the menu.
- `add_menu(title, root, **kwargs)`: Adds a submenu to the menu.

### Random
A class for generating random values.

#### Methods
- `number(number1, number2)`: Generates a random integer between two numbers.
- `item(list)`: Selects a random item from a list.

### file
A class for file operations.

#### Methods
- `create(name, path='')`: Creates a file.
- `delete(name, path='')`: Deletes a file.
- `write_to_file(text)`: Writes text to the documentation file.


## Examples

### Colorprint

```python
from PigarOS import *

# Actually colorprint something
colorprint("Hello, World!", "blue")
```


### Window
```python
from PigarOS import window

def button_click():
    print("Button clicked!")

# Create a window
win = window.create("My Window", "400x300")

# Add a button to the window
win.add_button("Click Me", function=button_click)

# Run the window
win.run()
```

### File
```python
from PigarOS import file

# Create file 'example.txt'
file.create("example.txt")
# Delete file 'example.txt'
file.delete("example.txt")
```

### Random
```python
from PigarOS import Random

# Generate random number
random_number = Random.number(1, 100)
# Select radnom item from a list
random_item = Random.item(["apple", "banana", "orange"])
# print random number and random item
print(random_number, random_item)
```
