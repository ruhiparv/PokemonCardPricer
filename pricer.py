import re
import requests
from bs4 import BeautifulSoup

'''
This function takes the information of the pokemon card, searches the Price Charting website
for the correct card, scrapes the website for pricing information, and returns the price

Input: pokemon name (string), number of card (string), grade you want to check price (string)
Output: price of card (string)

This function also prints the Pokemon page's url for easy verification that the correct card
is being searched.
'''
def get_price(pokemon_name, num, grade):
    baseURL = "https://www.pricecharting.com/search-products?type=prices&q="
    url = baseURL + pokemon_name.replace(" ","+") + "+" + num + "&go=Go"
    print(url)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    grade_string = "Ungraded"
    if grade != "Ungraded":
        if grade == "10":
            grade_string = "PSA 10"
        else:
            grade_string = "Grade " + grade

    try:
        grade_row = soup.find('td', string=grade_string).parent
        price = grade_row.find('td', class_='price js-price').text.strip()
    except:
        return "Could not find pokemon card"


    return price

'''
This function takes user input of the Pokemon card of interest and outputs the result of 
the function get_price
If input format is incorrect it will indicate that to user and fail.
'''
def main():
    print("-------------------------------------------------------------")
    pokemon_info = input("Separated by commas, enter\nPokemon name, number on card, and grade (optional): ")

    try:
        name, number, *grade = re.split(r',\s*|,', pokemon_info.strip())
        number = number.lstrip('0')

        grade = grade[0] if grade else "Ungraded"

        price = get_price(name, number, grade)
        print(price)

    except ValueError:
        print("Wrong input format, please try again")

'''
This will continue to call the main function and ask for input, in order to have a continuosly running
price checker.
'''
if __name__ == "__main__":
    while True:
        main()

