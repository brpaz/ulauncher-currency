"""Ulauncher extension main  class"""

import re
import locale
import logging
import requests
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

LOGGER = logging.getLogger(__name__)

CONVERTER_API_BASE_URL = 'http://data.fixer.io/api'
REGEX = r"(\d+\.?\d*)\s*([a-zA-Z]{3})\s(to|in)\s([a-zA-Z]{3})"


class CurrencyConverterExtension(Extension):
    """ Main extension class """
    def __init__(self):
        """ init method """
        super(CurrencyConverterExtension, self).__init__()
        LOGGER.info("Initialzing Currency Converter extension")
        locale.setlocale(locale.LC_ALL, '')
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

    def convert_currency(self, amount, from_currency, to_currency):
        """ Converts an amount from one currency to another """
        try:
            # Fetch the conversion rates with the specified base currency
            url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{from_currency.lower()}.json"
            r = requests.get(url)
            response = r.json()

            if r.status_code != 200:
                raise ConversionException("Error connecting to conversion service.")

            # Get the rate for the target currency
            to_rate = response[from_currency.lower()].get(to_currency.lower())

            if to_rate is None:
                raise ConversionException("Currency not found.")

            # Calculate the amount from the conversion rates
            result = float(amount) * to_rate

            return locale.format_string("%.2f", result, grouping=True)

        except Exception as e:
            raise ConversionException(f"An error occurred: {str(e)}")


class KeywordQueryEventListener(EventListener):
    """ Handles Keyboard input """
    def on_event(self, event, extension):
        """ Handles the event """
        items = []

        query = event.get_argument() or ""

        matches = re.findall(REGEX, query, re.IGNORECASE)

        if not matches:
            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='Keep typing your query ...',
                    description='It should be in the format: "20 EUR to USD"',
                    highlightable=False,
                    on_enter=HideWindowAction()))

            return RenderResultListAction(items)

        try:
            params = matches[0]

            amount = params[0]
            from_currency = params[1].upper()
            to_currency = params[3].upper()

            value = extension.convert_currency(amount, from_currency,
                                               to_currency)

            items.append(
                ExtensionResultItem(icon='images/icon.png',
                                    name="%s %s" % (value, to_currency),
                                    highlightable=False,
                                    on_enter=CopyToClipboardAction(value)))

            return RenderResultListAction(items)

        except ConversionException as e:
            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='An error ocurred during the conversion process',
                    description=e.message,
                    highlightable=False,
                    on_enter=HideWindowAction()))

            return RenderResultListAction(items)


class ConversionException(Exception):
    """ Exception thrown when there was an error calling the conversion API """
    pass


if __name__ == '__main__':
    CurrencyConverterExtension().run()
