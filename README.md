# Pokemon Card Price Checker
This program uses a [Pokemon Card Price Charting website](https://www.pricecharting.com/) 
to scrape pricing information for a Pokemon card based on user input.

## Set up
Make sure to have the external packages:
```python
pip install beautifulsoup4

pip install requests
```

## Usage
Inputs are a string of comma-separated values:

`pokemon name, number on bottom left of card, grade (optional)`

Examples:

- `Jolteon, TG04, Ungraded`
- `Arceus VSTAR, 184, 10`
- `Riolu, 178`
