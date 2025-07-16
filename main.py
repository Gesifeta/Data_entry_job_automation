from data import Zillow

from data_entry import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://google.com'
}
while True:
    print("1. Rentals")
    print("2. Exit")
    print("--"*50)
    selection = int(input("Enter your choice: "))
    if int(selection) == 4:
        break
    else:
        city = input("Enter your city:")
        if selection == 1:
            text = Zillow(category="rentals",city=city,headers=headers)
            text.get_data()
            links= text.hrefs
            addresses= text.address
            info= text.info
            enter_data = DataEntry()
            enter_data.submit_form(address=addresses,info=info,link=links)
        elif selection == 2:
            break
