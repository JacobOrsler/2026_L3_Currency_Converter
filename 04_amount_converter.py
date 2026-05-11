from tkinter import *
import currency_conversion as cc


class Converter:
    """
    NZD currency converter tool
    """

    def __init__(self):
        """
        Currency converter GUI
        """

        self.all_calculations_list = []

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
                                    font=("Arial", "14"))
        self.currency_entry.grid(row=3, padx=18, pady=10)

        # Default message
        default_message = "Please enter the amount to be converted"

        # Label that displays the conversions or error message
        self.answer_error = Label(self.currency_frame, text=default_message,
                                  fg="#004C99")
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
            width=12, command=self.check_amount
        )
        convert_button.grid(row=0, column=0, columnspan=2, pady=5)

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

        # Retrieve to_help button
        self.to_help_button = self.button_ref_list[1]

        # Retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[2]
        self.to_history_button.config(state=DISABLED)

    def check_amount(self):
        """
        Checks if amount is valid and either invokes calculation function or shows a custom error
        """

        # Retrieve amount to be converted
        amount = self.currency_entry.get()

        # Reset label and entry box (if we had an error)
        self.answer_error.config(fg="#004C99")
        self.currency_entry.config(bg="#FFFFFF")

        # Check amount is a number and between 0 and 1,000,000
        try:
            amount = float(amount)
            if amount <= 0:
                error = "Amount must be greater than 0"
            elif amount > 1000000:
                error = "Amount must not be greater than $1,000,000"
            else:
                error = ""
                self.convert_currency(amount)

        except ValueError:
            error = "Please enter a valid number"

        # Display the error if necessary
        if error:
            self.answer_error.config(text=error, fg="#9C0000")
            self.currency_entry.config(bg="#F4CCCC")
            self.currency_entry.delete(0, END)

    def convert_currency(self, amount):
        """
        Converts amounts and updates answer label. Also stores calculations for Export / History feature
        """

        # Get the full dropdown text and get the currency code
        pair = self.selected_conversion.get()
        target = pair[-3:]

        # Calls the 'currency_conversion' file to convert the amount
        converted = cc.convert_nzd(amount, target)

        # Formatted answer
        answer_statement = f"{amount} NZD = {converted} {target}"

        # Enable history export button as soon as we have a valid calculation
        self.to_history_button.config(state=NORMAL)

        # Configures the converted answer, adds it the list and prints it out on the console
        self.answer_error.config(text=answer_statement)
        self.all_calculations_list.append(answer_statement)
        print(self.all_calculations_list)


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("NZD Currency Converter")
    Converter()
    root.mainloop()
