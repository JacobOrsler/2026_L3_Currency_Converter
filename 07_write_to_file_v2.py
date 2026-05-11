from datetime import date

calculations = ['10 NZD is 8.35 AUD', '40 NZD is 33.40 AUD',
                '20 NZD is 16.70 AUD', '50 NZD is 41.75 AUD',
                '30 NZD is 25.05 AUD', '60 NZD is 50.10 AUD']


# Oldest to newest
def ordered_list(listname):
    return listname


# Get current date for heading and filename
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# Create a dated filename for the export
file_name = f"currency_conversions_{year}_{month}_{day}"

# Create text file
write_to = f"{file_name}.txt"

# Write format the text file with header, date and history title
with open(write_to, "w") as text_file:
    text_file.write("*** Currency Conversions ***\n")
    text_file.write(f"Generated: {day}/{month}/{year}\n\n")
    text_file.write("Here is your calculation history (oldest to newest)\n")

    # Write the items to file using the reversed list
    for item in ordered_list(calculations):
        text_file.write(item)
        text_file.write("\n")
