"""Ulauncher extension main  class"""

import logging
import requests
import re
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
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

    def convert_currency(self, amount, from_currency, to_currency):
        """ Converts an amount from one currency to another """

        params = {'access_key': self.preferences['api_key'], 'symbols': '%s,%s' % (
            from_currency, to_currency)}

        r = requests.get("%s/latest" % CONVERTER_API_BASE_URL, params=params)
        response = r.json()

        if r.status_code != 200:
            raise ConversionException(
                "Error connecting to conversion service.")

        if not response['success']:
            raise ConversionException(response['error']['info'])

        # Calculate the amount from the conversion rates.
        # Fixer.io base Currency is Eur.
        rates = response['rates']

        result = (float(amount) / rates[from_currency]) * rates[to_currency]

        return str(round(result, 2))


class KeywordQueryEventListener(EventListener):
    """ Handles Keyboard input """

    def on_event(self, event, extension):
        """ Handles the event """
        items = []

        query = event.get_argument() or ""

        matches = re.findall(REGEX, query, re.IGNORECASE)

        if not matches:
            items.append(ExtensionResultItem(icon='images/icon.png',
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

            value = extension.convert_currency(
                amount, from_currency, to_currency)

            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name="%s %s" % (
                                                 value, to_currency),
                                             highlightable=False,
                                             on_enter=CopyToClipboardAction(value)))

            return RenderResultListAction(items)

        except ConversionException as e:
            items.append(ExtensionResultItem(icon='images/icon.png',
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
