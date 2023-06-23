import tkinter as tk
import pyautogui

def take_screenshot():
    # Get the screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Capture the screenshot
    screenshot = pyautogui.screenshot()

    # Save the screenshot
    screenshot.save("screenshot.png")
    print("Screenshot saved!")

# Create the main window
window = tk.Tk()
window.title("Screenshot GUI")

# Create a button to take the screenshot
screenshot_button = tk.Button(window, text="Take Screenshot", command=take_screenshot)

# Add the button to the window
screenshot_button.pack()

# Start the GUI event loop
window.mainloop()
