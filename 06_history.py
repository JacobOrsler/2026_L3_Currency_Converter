from tkinter import *
from functools import partial  # To prevent unwanted windows
from datetime import date


def to_history(self):
    """
    Opens history dialogue box and disables history button (so that users can't create multiple history boxes)
    """
    HistoryExport(self, self.all_calculations_list)


class Converter:
    """
    NZD currency converter tool
    """

    def __init__(self):
        """
        Currency converter GUI
        """

        self.all_calculations_list = ['10 NZD is 8.35 AUD', '40 NZD is 33.40 AUD',
                                      '20 NZD is 16.70 AUD', '50 NZD is 41.75 AUD',
                                      '30 NZD is 25.05 AUD', '60 NZD is 50.10 AUD']

        # Creating a frame
        self.currency_frame = Frame(padx=10, pady=10)
        self.currency_frame.grid()

        # Creating history button
        self.to_history_button = Button(self.currency_frame,
                                        text="History / Export",
                                        bg="#CC6600",
                                        fg="#FFFFFF",
                                        font=("Arial", "14", "bold"), width=12,
                                        command=partial(to_history, self)
                                        )
        self.to_history_button.grid(row=1, padx=5, pady=5)


class HistoryExport:
    """
    Displays history dialogue box
    """

    def __init__(self, partner, calculations):

        self.history_box = Toplevel()

        # Disable history button
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at top, closes help and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # Background colour and text for calculation area
        if len(calculations) <= 5:
            calc_back = "#D5E8D4"
            calc_amount = "all your"
        else:
            calc_back = "#ffe6cc"
            calc_amount = (f"your recent calculations - "
                           f"showing {5} / {len(calculations)}")

        # Strings for 'long' labels
        recent_intro_txt = f"Below are {calc_amount} calculations: "

        # Create string from calculations list (the newest calculations first)
        newest_first_string = ""
        newest_first_list = list(reversed(calculations))

        # Last item added in outside the for loop so that the spacing is correct
        if len(newest_first_list) <= 5:

            for item in newest_first_list:
                newest_first_string += item + "\n"

        # If we have more than five items
        else:
            for item in newest_first_list[:5]:
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
