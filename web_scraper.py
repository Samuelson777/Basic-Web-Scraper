import requests
from bs4 import BeautifulSoup

# Function to scrape data from a website
def scrape_website(url):
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all article titles (modify the selector based on the website structure)
        titles = soup.find_all('h3')  # Example: assuming titles are in <h3> tags
        
        # Save the titles to a file
        with open('titles.txt', 'w') as file:
            for title in titles:
                file.write(title.get_text() + '\n')
        
        print("Titles have been saved to titles.txt")
    else:
        print(f"Failed to retrieve the website. Status code: {response.status_code}")

if __name__ == "__main__":
    url = input("Enter the URL of the website to scrape: ")
    scrape_website(url)