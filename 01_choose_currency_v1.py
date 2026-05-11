from tkinter import *


class Converter:

    def __init__(self, parent):

        # Creating a frame
        self.dropdown_frame = Frame(parent, padx=10, pady=10)
        self.dropdown_frame.grid()

        Label(self.dropdown_frame, text="NZD Currency Converter - OptionMenu").grid(row=0)

        # Dropdown list for all conversion pairs
        self.currency_options = [
            "NZD to AUD",
            "NZD to USD",
            "NZD to GBP",
            "NZD to EUR"
        ]

        # Store selected option
        self.selected = StringVar()

        # Default dropdown option
        self.selected.set(self.currency_options[0])

        # Creates dropdown menu and gets the different options
        self.dropdown = OptionMenu(self.dropdown_frame,
                                   self.selected,
                                   *self.currency_options)
        self.dropdown.grid(row=1, pady=10)


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("NZD Currency Converter")
    Converter(root)
    root.mainloop()
