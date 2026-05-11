from tkinter import *


class Converter:

    def __init__(self, parent):

        # Creating a frame
        self.listbox_frame = Frame(parent, padx=10, pady=10)
        self.listbox_frame.grid()

        Label(self.listbox_frame, text="NZD Currency Converter - Listbox").grid(row=0)

        # List of all conversion pairs
        self.currency_options = [
            "NZD to AUD",
            "NZD to USD",
            "NZD to GBP",
            "NZD to EUR"
        ]

        # Create Listbox
        self.currency_listbox = Listbox(self.listbox_frame,
                                        height=4,
                                        font=("Arial", 12),
                                        activestyle="dotbox")
        self.currency_listbox.grid(row=1, pady=10)

        # Insert items into Listbox
        for item in self.currency_options:
            self.currency_listbox.insert(END, item)


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("NZD Currency Converter (Listbox Trial)")
    Converter(root)
    root.mainloop()
