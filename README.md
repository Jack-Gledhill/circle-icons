# Circle Icons

These are a set of open-source icons designed by [Liam Doherty](https://github.com/dohliam/elegant-circles) and released for personal & commercial use under the GPL v2 license.

This repo is a fork of the designer's own, with an extra script that converts them into various sizes and formats. It's released under the same license.

## Accessing the icons online

Like the original repo, this one hosts all of the files via GitHub Pages, so that people can access them via URLs rather than having to download them and store them in their project manually.

The icons can be accessed at [jack-gledhill.github.io/circle-icons](https://jack-gledhill.github.io/circle-icons).

## Running the script

Make sure you have Python 3 installed, then install the dependencies with:

```shell
pip install -r requirements.txt
```

CairoSVG also requires several extra packages that change depending on your OS. For macOS, do the following:

```shell
brew install cairo libffi
```

For Windows and Linux, see the [CairoSVG documentation](https://cairosvg.org/documentation/#installation).