import requests


def round_ans(val):
    """
    Rounds values to two decimal places
    :param val: Number to be rounded
    :return: Number rounded to two decimal places
    """

    return f"{val:.2f}"


def get_live_rate(target_currency):
    """
    Fetches the live exchange rate from NZD to the target currency.
    Uses the Frankfurter API: https://api.frankfurter.dev/v1/latest
    :param target_currency: 'AUD', 'USD', 'GBP', 'EUR'
    :return: exchange rate as float
    """

    url = "https://api.frankfurter.dev/v1/latest"
    params = {
        "from": "NZD",
        "to": target_currency
    }

    # Get data from the API and turn it into a Python dictionary
    response = requests.get(url, params=params)
    data = response.json()

    # Get the rate for the chosen currency
    return data["rates"][target_currency]


def convert_nzd(amount, target_currency):
    """
    Converts NZD to the selected currency using live rates.
    :param amount: amount in NZD
    :param target_currency: 'AUD', 'USD', 'GBP', 'EUR'
    :return: converted amount as a 2dp string
    """

    # Convert the amount and round the final value to 2dp
    rate = get_live_rate(target_currency)
    converted = amount * rate
    return round_ans(converted)
