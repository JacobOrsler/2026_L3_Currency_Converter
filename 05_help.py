from tkinter import *
from functools import partial  # To prevent unwanted windows


def to_help(self):
    """
    Opens help dialogue box and disables help button (so that users can't create multiple help boxes)
    """
    DisplayHelp(self)


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

        # Creating help button
        self.to_help_button = Button(self.currency_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg="#FFFFFF",
                                     font=("Arial", "14", "bold"), width=12,
                                     command=partial(to_help, self)
                                     )
        self.to_help_button.grid(row=1, padx=5, pady=5)


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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("NZD Currency Converter")
    Converter()
    root.mainloop()
