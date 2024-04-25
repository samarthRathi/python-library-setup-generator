import csv
import requests
from bs4 import BeautifulSoup

# URL of the page containing the library headings
url = "https://www.datacamp.com/blog/top-python-libraries-for-data-science"

# Define headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

try:
    # Send a GET request to the URL with headers
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the headings (h3 tags) containing the library names
    headings = soup.find_all("h3")

    # Extract the text of the headings and save them as a list
    library_headings = [heading.get_text() for heading in headings]

    # Save the library headings to a CSV file
    with open("library_headings.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Library Headings"])
        for heading in library_headings:
            writer.writerow([heading])

    print("Library headings saved to library_headings.csv")

except Exception as e:
    print(f"An error occurred: {e}")
