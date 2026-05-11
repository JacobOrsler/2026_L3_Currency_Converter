from tkinter import *


class Converter:
    """
    NZD currency converter tool
    """

    def __init__(self):
        """
        Currency converter GUI
        """

        # Creating a frame to display the currency converter section
        self.currency_frame = Frame(padx=10, pady=10)
        self.currency_frame.grid()

        # Heading that displays currency converter section
        self.currency_heading = Label(self.currency_frame,
                                      text="NZD Currency Converter",
                                      font=("Arial", "16", "bold"))
        self.currency_heading.grid(row=0)

        instructions = ("Please select what currency you want to convert NZD to from the dropdown box, "
                        "enter the amount to be converted and press the converter button:")

        # Quick instructions explaining what the currency convert does
        self.currency_instructions = Label(self.currency_frame,
                                           text=instructions,
                                           wraplength=250, width=40,
                                           justify="left")
        self.currency_instructions.grid(row=1)

        # Dropdown list for all conversion pairs
        self.currency_options = [
            "NZD to AUD",
            "NZD to USD",
            "NZD to GBP",
            "NZD to EUR"
        ]

        # Store selected option
        self.selected_conversion = StringVar()

        # Default dropdown option
        self.selected_conversion.set(self.currency_options[0])

        # Creates dropdown menu and gets the different options
        self.conversion_menu = OptionMenu(self.currency_frame,
                                          self.selected_conversion,
                                          *self.currency_options)
        self.conversion_menu.grid(row=2, padx=10, pady=10)

        # Entry box where the user types the amount to convert
        self.currency_entry = Entry(self.currency_frame,
                                    font=("Arial", "14")
                                    )
        self.currency_entry.grid(row=3, padx=18, pady=10)

        # Default message
        default_message = "Please enter the amount to be converted"

        # Label that displays the conversions or error message
        self.answer_error = Label(self.currency_frame, text=default_message,
                                  fg="#9C0000")
        self.answer_error.grid(row=4)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.currency_frame)
        self.button_frame.grid(row=5)

        # Make the single column expand so the convert button centres
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)

        # Convert button (centered across both columns)
        convert_button = Button(
            self.button_frame,
            text="CONVERT", bg="#990099",
            fg="#FFFFFF", font=("Arial", "12", "bold"),
            width=12
        )
        convert_button.grid(row=2, column=0, columnspan=2, pady=5)

        # List to hold buttons once they have been made
        self.button_ref_list = [convert_button]

        # Button list (button text | bg colour |command | row | column)
        button_details_list = [
            ["Help / Info", "#CC6600", lambda: None, 1, 0],
            ["History / Export", "#004C99", lambda: None, 1, 1]
        ]

        # Loop to create help and export buttons
        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("NZD Currency Converter")
    Converter()
    root.mainloop()
