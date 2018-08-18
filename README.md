# Ulauncher Currency Extension

> [Ulauncher](https://ulauncher.io/) Extension to convert an amount between currencies. Conversion rates provided by [Fixer](https://fixer.io/).

## Demo

![demo](demo.gif)

## Requirements

* [ulauncher](https://ulauncher.io/)
* Python >= 2.7

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```https://github.com/brpaz/ulauncher-currency```

After installing the extension, go to the extension settings and input your Fixer Access Token. You can get one from [Fixer](https://fixer.io/) website.
The free plan is enough for this extension to work. It has a limit of 1000 requests per month which should be more than enough for you.

## Example Usage

```currency 20 USD TO EUR ```

```currency 100 GBP TO XOF ```

## Development

```
make link
```

To see your changes, stop ulauncher and run it from the command line with: ```ulauncher -v```.

## License

MIT
