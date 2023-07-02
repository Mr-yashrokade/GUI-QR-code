# GUI-QR-code

1. Introduction:
The QR Code Generator is a graphical user interface (GUI) application built using the Tkinter library in Python. It allows users to generate QR codes by entering a link and customizing various options such as foreground color and background color. The generated QR code can be saved as a PNG image file.

2. Application Features:
The QR Code Generator application provides the following features:

GUI Design: The application uses the Tkinter library to create a user-friendly interface.![Screenshot (106)](https://github.com/Mr-yashrokade/GUI-QR-code/assets/136175560/d8e28742-4798-4fba-9d17-331ecaa5b7a2)

Fullscreen Mode: The application runs in fullscreen mode to provide a distraction-free experience.
Always-on-Top Window: The application window remains on top of other windows for convenient access.
Tool Window: The application window is set as a tool window, which gives it a compact appearance in the taskbar.
QR Code Generation: The application generates a QR code based on the entered link using the pyqrcode library.
Foreground Color Selection: Users can select a custom foreground color for the QR code.
Background Color Selection: Users can choose a custom background color for the QR code.
Color Chooser Dialog: The application provides a color chooser dialog to facilitate color selection.
QR Code Preview: The generated QR code is displayed within the application's designated frame.
Save QR Code: Users can save the generated QR code as a PNG image file using the file dialog.
3. Code Explanation:
The code begins by importing the necessary modules and libraries required for the application, such as Tkinter, pyqrcode, and PIL.

Next, the Tkinter root window is initialized, and various window attributes such as background color, title, fullscreen mode, topmost status, and tool window status are configured.

The code defines several functions used in the application:

generate(): This function is called when clicking the "Generate QR Code" button. It retrieves the link name and link from the respective entry fields, generates a QR code using pyqrcode, and saves it as a PNG image file. The generated QR code image is displayed in the QR code label.
choose_foreground_color(): This function opens the color chooser dialog and sets the selected color as the foreground color for the QR code.
choose_background_color(): This function opens the color chooser dialog and sets the selected color as the background color for the QR code.
save_qr_code(): This function opens the file dialog to select a file path for saving the generated QR code image.
The code then creates a canvas within the root window to hold the application elements.

Label and entry widgets are created for entering the link name and link. Two StringVar variables (fore_color and back_color) are used to store the selected foreground and background colors.

Buttons are created for selecting the foreground color, and background color, generating the QR code, and saving the QR code image.

A frame is created to hold the QR code image, and a label is placed inside the frame to display the image.

Finally, the code sets the main loop for the Tkinter window to handle user interactions and events.

4. Conclusion:
The QR Code Generator application provides a convenient and user-friendly way to generate QR codes for various purposes. It allows users to customize the QR code's appearance by selecting different foreground and background colors. The application's fullscreen mode and always-on-top window feature enhance the user experience. Users can save the generated QR code as a PNG image file for further use. Overall, the application demonstrates the capabilities of the Tkinter library in creating GUI applications in Python.

