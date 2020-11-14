# Ulauncher Currency Extension

> [Ulauncher](https://ulauncher.io/) Extension to convert an amount between currencies. Conversion rates provided by [Fixer](https://fixer.io/).

## Demo

![demo](demo.gif)

## Requirements

* [ulauncher](https://ulauncher.io/)
* Python >= 3
* An account and respective API key from [Fixer.io](https://fixer.io/quickstart).

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

## ## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 💛 Support the project

If this project was useful to you in some form, I would be glad to have your support.  It will help to keep the project alive and to have more time to work on Open Source.

The sinplest form of support is to give a ⭐️ to this repo.

You can also contribute with [GitHub Sponsors](https://github.com/sponsors/brpaz).

[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Sponsor%20Me-red?style=for-the-badge)](https://github.com/sponsors/brpaz)

Or if you prefer a one time donation to the project, you can simple:

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

## 📝 License

Copyright © 2020 [Bruno Paz](https://github.com/brpaz).

This project is [MIT](https://opensource.org/licenses/MIT) licensed.
