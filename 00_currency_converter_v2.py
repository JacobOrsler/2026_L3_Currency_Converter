from tkinter import *
from functools import partial  # To prevent unwanted windows
import currency_conversion as cc
from datetime import date


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
            text="CONVERT", bg="#2563EB",
            fg="#FFFFFF", font=("Arial", "12", "bold"),
            width=12, command=self.check_amount
        )
        convert_button.grid(row=0, column=0, columnspan=2, pady=5)

        # List to hold buttons once they have been made
        self.button_ref_list = [convert_button]

        # Button list (button text | bg colour |command | row | column)
        button_details_list = [
            ["Help / Info", "#F59E0B", self.to_help, 1, 0],
            ["History / Export", "#6C32C7", self.to_history, 1, 1]
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

    def to_help(self):
        """
        Opens help dialogue box and disables help button (so that users can't create multiple help boxes)
        """
        Converter.DisplayHelp(self)

    def to_history(self):
        """
        Opens history dialogue box and disables history button (so that users can't create multiple history boxes)
        """
        Converter.HistoryExport(self, self.all_calculations_list)

    class DisplayHelp:
        """
        Displays help dialogue box
        """

        def __init__(self, partner):
            # Setup dialogue box and background colour
            background = "#ffe6cc"
            self.help_box = Toplevel()

            # Disable help button
            partner.to_help_button.config(state=DISABLED)

            # If users press cross at top, closes help and 'releases' help button
            self.help_box.protocol('WM_DELETE_WINDOW',
                                   partial(self.close_help, partner))

            # Frame for holding all help window content
            self.help_frame = Frame(self.help_box, width=300,
                                    height=200)
            self.help_frame.grid()

            # Heading label for the help window
            self.help_heading_label = Label(self.help_frame,
                                            text="Help / Info",
                                            font=("Arial", "14", "bold"))
            self.help_heading_label.grid(row=0)

            help_text = (
                "To use the converter, just pick which currency you want to change NZD into "
                "from the dropdown menu, then type in how much NZD you want to convert. "
                "Hit the CONVERT button and your result will pop up.\n\n"
                "The converter uses up‑to‑date exchange rates from the Frankfurter API. "
                "These rates update once a day, so the numbers you get will match the latest "
                "official values.\n\n"
                "You can only enter positive amounts up to 1,000,000 NZD.\n\n"
                "If you want to see your recent conversions or save them to a text file, "
                "click the 'History / Export' button."
            )

            # Display the help text inside the help window
            self.help_text_label = Label(
                self.help_frame,
                text=help_text,
                wraplength=350,
                justify="left"
            )
            self.help_text_label.grid(row=1, padx=10)

            # Create the dismiss button
            self.dismiss_button = Button(self.help_frame,
                                         font=("Arial", "12", "bold"),
                                         text="Dismiss", bg="#CC6600",
                                         fg="#FFFFFF",
                                         command=partial(self.close_help, partner))
            self.dismiss_button.grid(row=2, padx=10, pady=10)

            # List and loop to set background colour on everything except the buttons.
            recolour_list = [self.help_frame, self.help_heading_label, self.help_text_label]

            for item in recolour_list:
                item.config(bg=background)

        def close_help(self, partner):
            """
            Closes help dialogue box (and enables help button)
            """

            # Put help button back to normal
            partner.to_help_button.config(state=NORMAL)
            self.help_box.destroy()

    class HistoryExport:
        """
        Displays history dialogue box
        """

        def __init__(self, partner, calculations):

            # Max number of recent calculations
            self.max_items = 5

            self.history_box = Toplevel()

            # Disable history button
            partner.to_history_button.config(state=DISABLED)

            # If users press cross at top, closes help and 'releases' history button
            self.history_box.protocol('WM_DELETE_WINDOW',
                                      partial(self.close_history, partner))

            self.history_frame = Frame(self.history_box)
            self.history_frame.grid()

            # Background colour and text for calculation area
            if len(calculations) <= self.max_items:
                calc_back = "#D5E8D4"
                calc_amount = "all your"
            else:
                calc_back = "#ffe6cc"
                calc_amount = (f"your recent calculations - "
                               f"showing {self.max_items} / {len(calculations)}")

            # Strings for 'long' labels
            recent_intro_txt = f"Below are {calc_amount} calculations: "

            # Create string from calculations list (the newest calculations first)
            newest_first_string = ""
            newest_first_list = list(reversed(calculations))

            # Last item added in outside the for loop so that the spacing is correct
            if len(newest_first_list) <= self.max_items:

                for item in newest_first_list:
                    newest_first_string += item + "\n"

            # If we have more than five items
            else:
                for item in newest_first_list[:self.max_items]:
                    newest_first_string += item + "\n"

            newest_first_string = newest_first_string.strip()

            export_instruction_txt = ("Please push <Export> to save your calculations in "
                                      "file. If the filename already exists, it will be overwritten.")

            # Label list (label text | format | bg)
            history_labels_list = [
                ["History / Export", ("Arial", "16", "bold"), None],
                [recent_intro_txt, ("Arial", "11"), None],
                [newest_first_string, ("Arial", "14"), calc_back],
                [export_instruction_txt, ("Arial", "11"), None]
            ]

            # Create each history label and add it to the list
            history_label_ref = []
            for count, item in enumerate(history_labels_list):
                make_label = Label(self.history_frame, text=item[0], font=item[1],
                                   bg=item[2],
                                   wraplength=300, justify="left", pady=10, padx=20)
                make_label.grid(row=count)

                history_label_ref.append(make_label)

            # Retrieve export instruction label so that we can
            # configure it to show the filename if the user exports the file
            self.export_filename_label = history_label_ref[3]

            # Make frame to hold buttons (two columns)
            self.hist_button_frame = Frame(self.history_frame)
            self.hist_button_frame.grid(row=4)

            # Button list (button text | bg colour | command | row | column)
            button_details_list = [
                ["Export", "#0066CC", lambda: self.export_data(calculations), 0, 0],
                ["Close", "#666666", partial(self.close_history, partner), 0, 1],
            ]

            # Loop to create export and dismiss buttons
            for btn in button_details_list:
                self.make_button = Button(self.hist_button_frame,
                                          font=("Arial", "12", "bold"),
                                          text=btn[0], bg=btn[1],
                                          fg="#FFFFFF", width=12,
                                          command=btn[2])
                self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)

        def export_data(self, calculations):
            # Get current date for heading and filename
            today = date.today()

            # Get day, month and year as individual strings
            day = today.strftime("%d")
            month = today.strftime("%m")
            year = today.strftime("%Y")

            # Create a dated filename for the export
            file_name = f"currency_conversions_{year}_{month}_{day}"

            # Edit label so users know that their export has been done
            success_string = ("Export Successful! The file is called "
                              f"{file_name}.txt")
            self.export_filename_label.config(fg="#009900", text=success_string,
                                              font=("Arial", "12", "bold"))

            # Create text file
            write_to = f"{file_name}.txt"

            # Write format the text file with header, date and history title
            with open(write_to, "w") as text_file:
                text_file.write("*** Currency Conversions ***\n")
                text_file.write(f"Generated: {day}/{month}/{year}\n\n")
                text_file.write("Here is your calculation history (oldest to newest)\n")

                # Write the item to file
                for item in calculations:
                    text_file.write(item)
                    text_file.write("\n")

        def close_history(self, partner):
            """
            Closes history dialogue box (and enables history button)
            """

            # Put history button back to normal
            partner.to_history_button.config(state=NORMAL)
            self.history_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("NZD Currency Converter")
    Converter()
    root.mainloop()
