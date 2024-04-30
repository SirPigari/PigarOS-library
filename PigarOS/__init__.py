import tkinter as tk
from tkinter import Tk, Label, simpledialog, messagebox, filedialog, colorchooser, ttk, commondialog
from PIL import Image, ImageTk
import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame
import time
import logging
import webbrowser
import datetime
import sys

Neither = not (True or False)
Maybe = random.choice((True, True, True, False))
IDontKnow = random.choice((True, False, None))

pigaros = """
██████╗ ██╗ ██████╗  █████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██║██╔════╝ ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██████╔╝██║██║  ███╗███████║██████╔╝██║   ██║███████╗
██╔═══╝ ██║██║   ██║██╔══██║██╔══██╗██║   ██║╚════██║
██║     ██║╚██████╔╝██║  ██║██║  ██║╚██████╔╝███████║
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
"""
if pigaros.startswith("\n"):
    pigaros = pigaros[1:]

startprint = True

def covert_hex_to_rgb(hex_color='#ffffff'):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def colorprint(text, color="reset", bold=False):
    colors = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "purple": "\033[35m",
        "pink": "\033[38;2;255;105;180m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }

    if color.startswith("#"):
        colors[color] = f"\033[38;2;{int(color[1:3], 16)};{int(color[3:5], 16)};{int(color[5:], 16)}m"
    if bold:
        text = "\033[1m" + text

    print(f"{colors[color]}{text}{colors['reset']}")





def wait(seconds):
    time.sleep(seconds)

def printfile(filename=None):
    if filename:
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            raise Exception(f"File '{filename}' not found.")
        except Exception as e:
            raise Exception(e)
    elif not filename:
        raise Exception('No filename entered.')

class Random:
    @staticmethod
    def number(number1, number2):
        return random.randint(number1, number2)

    @staticmethod
    def item(list):
        return random.choice(list)

class message:
    @staticmethod
    def info(title, message, **kwargs):
        messagebox.showinfo(title, message, **kwargs)

    @staticmethod
    def error(title, message, **kwargs):
        messagebox.showerror(title, message, **kwargs)

    @staticmethod
    def warning(title, message, **kwargs):
        messagebox.showwarning(title, message, **kwargs)


class askfile:
    @staticmethod
    def openfile(**kwargs):
        path = filedialog.askopenfile(**kwargs)
        return path

    @staticmethod
    def savefile(**kwargs):
        path = filedialog.asksaveasfile(**kwargs)
        return path


def choosecolor(**kwargs):
    return colorchooser.Chooser(**kwargs)

def inputbox(title, prompt, **kwargs):
    return simpledialog.askstring(title, prompt, **kwargs)


def passwordbox(title, prompt, **kwargs):
    return simpledialog.askstring(title, prompt, show='*', **kwargs)

def commonmessage(**kwargs):
    return commonmessage(**kwargs)


class bind:
    def __init__(self, root):
        self.root = root
        self.key_actions = {}
        self.button_actions = {}

    def key(self, key, action):
        self.key_actions[key] = action
        self.root.bind(key, action)

    def button(self, button, action):
        self.button_actions[button] = action
        self.root.bind("<Button-{}>".format(button), action)


class Documentation:
    def __init__(self, filename='documentation.txt'):
        self.filename = filename

    def setup(self, name):
        with open(self.filename, 'a') as file:
            file.write(f"--Documentation for {name}--\n")
            file.write(f"Created on: {datetime.datetime.now()}\n\n")

    def write_to_file(self, text):
        timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        with open(self.filename, 'a', encoding='utf-8') as file:  # Specify encoding as utf-8
            file.write(f"{timestamp} {text}\n")

    def clear(self):
        with open(self.filename, 'w') as file:
            pass


doc = Documentation()


class file:
    @staticmethod
    def create(name, path=''):
        file_path = os.path.join(path, name)
        if not os.path.exists(file_path):
            with open(file_path, 'w'):
                pass
        else:
            colorprint(f"File '{name}' already exists.", 'red')
            raise FileExistsError

    @staticmethod
    def delete(name, path=''):
        file_path = os.path.join(path, name)
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            colorprint(f"File '{name}' does not exist.", 'red')
            raise FileExistsError


class TerminalLogger:
    def __init__(self, log_file):
        self.log_file = log_file

    def write(self, message):
        sys.__stdout__.write(message)
        doc.write_to_file(message)

    def flush(self):
        pass


sys.stdout = TerminalLogger(doc.filename)


class get:
    @staticmethod
    def mouse_x(root):
        return root.winfo_pointerx()

    @staticmethod
    def mouse_y(root):
        return root.winfo_pointery()

    @staticmethod
    def name():
        return os.path.basename(__file__)

    @staticmethod
    def path():
        return os.path.dirname(__file__)


class play:
    @staticmethod
    def sound(file):
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

    @staticmethod
    def stop_sound():
        pygame.mixer.quit()


class menu:
    def __init__(self, root, title, bg=None, fg=None):
        self.parent = root
        self.menu = tk.Menu(root.root, tearoff=0, bg=bg, fg=fg)
        root.root.config(menu=self.menu)
        self.submenus = {}
        self.actions = {}
        self.checkbox_variables = {}
        self.array_items = {}

    def add_submenu(self, title, menu):
        submenu = tk.Menu(self.menu, tearoff=0)
        self.submenus[title] = submenu
        self.menu.add_cascade(label=title, menu=submenu)
        return submenu

    def add_action(self, title, function):
        self.actions[title] = function
        self.menu.add_command(label=title, command=function)

    def add_bare_item(self, text):
        self.menu.add_command(label=text)

    def add_checkbox(self, title, variable, function):
        self.checkbox_variables[title] = variable
        self.menu.add_checkbutton(label=title, variable=variable, command=function)

    def add_array_item(self, options, function):
        submenu = tk.Menu(self.menu, tearoff=0)
        for option in options:
            submenu.add_command(label=option, command=lambda opt=option: function(opt))
        self.menu.add_cascade(label="Array Item", menu=submenu)

    def show(self, x, y):
        self.menu.post(x, y)

    def hide(self):
        self.menu.unpost()

    def add_menu(self, title, root, **kwargs):
        return menu(root, title, **kwargs)


class MouseCoordinateWindow:
    def __init__(self, root):
        self.popup = tk.Toplevel(root)
        self.popup.overrideredirect(True)  # Removes window decorations
        self.label = tk.Label(self.popup, text="")
        self.label.pack()
        self.update_position()

    def update_position(self):
        self.popup.geometry(f"+{self.popup.winfo_pointerx() + 10}+{self.popup.winfo_pointery() + 10}")
        self.popup.after(100, self.update_position)  # Update position every 100ms

    def update_coordinates(self, x, y):
        self.label.config(text=f"Mouse coordinates: ({x}, {y})")


class window:
    def __init__(self, title, size, icon=None):
        self.root = tk.Tk()
        self.root.title(title)
        if size == 'fullscreen':
            self.root.attributes('-fullscreen', True)
        else:
            self.root.geometry(size)
        if icon:
            self.root.iconbitmap(icon)
        else:
            try:
                self.root.iconbitmap('PigarOS/pigarOS_icon.ico')
            except Exception as e:
                pass
        self.checkboxes = {}
        self.labels = {}
        self.images = {}
        self.buttons = {}
        self.key_actions = {}
        self.inputs = {}

        self.root.bind("<Button-3>", self.show_mouse_coordinates)
        self.root.bind("<Control-Button-3>", self.hide_mouse_coordinates)
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Flag to keep track of Ctrl key state
        self.ctrl_pressed = False

        self.tabs = {}

    def add_tab(self, title):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)
        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text=title)
        self.tabs[title] = frame  # Store reference to tab frame
        return frame

    def remove_tab(self, title):
        if title in self.tabs:
            index = list(self.tabs.keys()).index(title)
            self.notebook.forget(index)
            del self.tabs[title]

    def show_mouse_coordinates(self, event):
        if self.ctrl_pressed:
            if hasattr(self, 'coordinate_window'):
                self.coordinate_window.update_coordinates(event.x_root, event.y_root)
            else:
                self.coordinate_window = MouseCoordinateWindow(self.root)
                self.coordinate_window.update_coordinates(event.x_root, event.y_root)

    def add_shape(self, shape, id=None, color='blue', size=(50, 50), x=0, y=0, function=None):
        x0, y0 = x, y
        x1, y1 = x + size[0], y + size[1]
        if shape == 'rect':
            shape_id = self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        elif shape == 'oval':
            shape_id = self.canvas.create_oval(x0, y0, x1, y1, fill=color)
        elif shape == 'triangle':
            points = [x0, y0, x1, y1, x0, y1]
            shape_id = self.canvas.create_polygon(points, fill=color)
        else:
            raise PigarOSCustomException("Invalid shape type. Use 'rect', 'oval', or 'triangle'.")

        if id:
            self.canvas.itemconfig(shape_id, tags=id)

        if function:
            self.canvas.tag_bind(shape_id, '<Button-1>', function)

    def after(self, milliseconds, function=None):
        self.root.after(milliseconds, function)

    def update(self):
        self.root.update()

    def collision(self, shape1_id, shape2_id, function=None):
        shape1_coords = self.canvas.coords(shape1_id)
        shape2_coords = self.canvas.coords(shape2_id)

        if (shape1_coords[2] >= shape2_coords[0] and shape1_coords[0] <= shape2_coords[2]) and \
           (shape1_coords[3] >= shape2_coords[1] and shape1_coords[1] <= shape2_coords[3]):
            if function:
                function()

    def hide_mouse_coordinates(self, event):
        self.ctrl_pressed = False

    def config(self, **kwargs):
        self.root.config(**kwargs)

    def add_button(self, title, function=None, x=None, y=None, **kwargs):
        button = tk.Button(self.root, text=title, command=function, **kwargs)
        if x is None and y is None:
            button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Place at center
        else:
            if x is not None:
                button.place(x=x)
            if y is not None:
                button.place(y=y)
        self.buttons[title] = button

    def add_checkbox(self, title, variable=None, function=None, x=None, y=None, **kwargs):
        checkbox = tk.Checkbutton(self.root, text=title, variable=variable, command=function, **kwargs)
        if x is not None:
            checkbox.place(x=x)
        if y is not None:
            checkbox.place(y=y)
        else:
            checkbox.pack()
        self.checkboxes[title] = checkbox

    def add_label(self, label, x=None, y=None, font=None, function=None, bg=None, fg=None):
        label_widget = tk.Label(self.root, text=label, font=font, bg=bg, fg=fg)
        if function:
            label_widget.bind("<Button-1>", function)
        if x is not None:
            label_widget.place(x=x)
        if y is not None:
            label_widget.place(y=y)
        else:
            label_widget.pack()
        self.labels[label] = label_widget

    def add_betterButton(self, title, function=None, x=None, y=None, **kwargs):
        button = ttk.Button(self.root, text=title, command=function, **kwargs)
        if x is None and y is None:
            button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Place at center
        else:
            if x is not None:
                button.place(x=x)
            if y is not None:
                button.place(y=y)
        self.buttons[title] = button

    def add_Input(self, id=None, x=None, y=None):
        entry = tk.Entry(self.root)
        entry.pack()
        if x is not None:
            entry.place(x=x)
        if y is not None:
            entry.place(y=y)
        self.inputs[id] = entry  # Store reference to the entry widget with its ID
        return entry

    def add_BetterInput(self, id=None, x=None, y=None):
        entry = ttk.Entry(self.root)
        entry.pack()
        if x is not None:
            entry.place(x=x)
        if y is not None:
            entry.place(y=y)
        self.inputs[id] = entry  # Store reference to the entry widget with its ID
        return entry

    def input_get(self, id):
        if id in self.inputs:
            return self.inputs[id].get()  # Retrieve text from the entry widget with the given ID
        else:
            raise PigarOSCustomException(f"Input with ID '{id}' not found.")

    def add_image(self, file, function=None, x=None, y=None, px=None, open=False):
        global image

        def open_image(event):
            url = os.path.abspath(file)
            webbrowser.open(f"file://{url}")

        try:
            image = Image.open(file)
        except Exception as e:
            colorprint(f'Exception in PigarOS: {e}', 'red')
        if px:
            width, height = map(int, px.split("x"))  # Split px and convert to integers
            image = image.resize((width, height))  # Resize image
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.root, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        if open:
            label.bind("<Button-3>", open_image)
        if function is not None:
            label.bind("<Button-1>", function)
        if x is not None:
            label.place(x=x)
        if y is not None:
            label.place(y=y)
        else:
            label.pack()
        self.images[file] = label

    def move_shape(self, shape_name, direction, px):
        """
        Move a shape by a specified number of pixels in a specified direction.

        Parameters:
            shape_name (str): The name of the shape to move.
            direction (str): The direction to move the shape ('up', 'down', 'left', 'right').
            px (int): The number of pixels to move the shape by.
        """
        shape_id = self.canvas.find_withtag(shape_name)
        if not shape_id:
            raise PigarOSCustomException(f"Shape '{shape_name}' not found.")
        if direction == 'up':
            self.canvas.move(shape_id, 0, -px)
        elif direction == 'down':
            self.canvas.move(shape_id, 0, px)
        elif direction == 'left':
            self.canvas.move(shape_id, -px, 0)
        elif direction == 'right':
            self.canvas.move(shape_id, px, 0)
        else:
            raise PigarOSCustomException("Invalid direction. Use 'up', 'down', 'left', or 'right'.")

    def hide_checkbox(self, title):
        if title in self.checkboxes:
            self.checkboxes[title].pack_forget()

    def show_checkbox(self, title):
        if title in self.checkboxes:
            self.checkboxes[title].pack()

    def remove_checkbox(self, title):
        if title in self.checkboxes:
            self.checkboxes[title].destroy()
            del self.checkboxes[title]

    def hide_label(self, label_text):
        if label_text in self.labels:
            self.labels[label_text].pack_forget()

    def show_label(self, label_text):
        if label_text in self.labels:
            self.labels[label_text].pack()

    def remove_label(self, label_text):
        if label_text in self.labels:
            self.labels[label_text].destroy()
            del self.labels[label_text]

    def hide_image(self, name):
        if name in self.images:
            self.images[name].pack_forget()

    def show_image(self, name):
        if name in self.images:
            self.images[name].pack()

    def remove_image(self, name):
        if name in self.images:
            self.images[name].destroy()
            del self.images[name]

    def hide_button(self, name):
        if name in self.buttons:
            self.buttons[name].pack_forget()

    def show_button(self, name):
        if name in self.buttons:
            self.buttons[name].pack()

    def remove_button(self, name):
        if name in self.buttons:
            self.buttons[name].destroy()
            del self.buttons[name]

    def kill(self):
        self.root.destroy()

    def exit(self):
        self.root.quit()

    def run(self):
        self.root.mainloop()

    def create(title, size, icon=None):
        return window(title, size, icon)


class CustomError(Exception):
    pass


class PigarOSException(CustomError):
    def __init__(self):
        self.message = 'Exception in PigarOS'
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class PigarOSCustomException(CustomError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"

class PigarOS:
    @staticmethod
    def config(print=True):
        startprint = print
        if startprint:
            colorprint("(C) PigarOS library", "blue", True)

    @staticmethod
    def hello(text=None):
        if not text:
            colorprint(pigaros, "blue", True)
        elif text == 'world':
            colorprint('Hello world!', 'green')
        else:
            print(text)