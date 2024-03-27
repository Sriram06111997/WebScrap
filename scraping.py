import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    try:

        response = requests.get(url)
        

        
        if response.status_code == 200:
            
            soup = BeautifulSoup(response.text, 'html.parser')


            headings = soup.find_all('li')
            extracted_data = [heading.text.strip() for heading in headings]

            
            cleaned_data = clean_data(extracted_data)

            
            return cleaned_data
        else:
            print(f'Failed to fetch the webpage. Status code: {response.status_code}')
            return None
    except Exception as e:
        print(f'An error occurred: {str(e)}')
        return None

def clean_data(data):
    
    cleaned_data = [item for item in data if item.strip()]
    return cleaned_data


import csv

def save_to_csv(data, filename):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title'])
            for item in data:
                writer.writerow([item])
        print(f'Data saved to {filename} successfully.')
    except Exception as e:
        print(f'An error occurred while saving data: {str(e)}')


if __name__ == "__main__":
    url = 'https://www.flipkart.com/mobile-phones-store?fm=neo%2Fmerchandising&iid=M_e7f90cd9-8512-466b-902b-edb440bf1c0c_1_372UD5BXDFYS_MC.ZRQ4DKH28K8J&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Mobiles_ZRQ4DKH28K8J&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L0_view-all&cid=ZRQ4DKH28K8J'
    data = scrape_website(url)
    if data:
        # Save the data to a CSV file
        save_to_csv(data, 'scraped_data.csv')


    
