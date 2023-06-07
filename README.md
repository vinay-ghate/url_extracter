# Website Link Extractor

This script allows you to extract links from a website by providing its URL. It utilizes the `requests` and `bs4` libraries to retrieve the source code of the website and parse it to extract the URLs.

## Usage

1. Import the required libraries:

   ```python
   import requests
   import bs4
   ```

2. Prompt the user for input:

   ```python
   url = input("Enter the URL (starting with https://): ")
   ```

   The user needs to provide the URL of the website from which they want to extract the links.

3. Define the `extract_links` function:

   ```python
   def extract_links(url):
       site_data = requests.get(url)
       data = bs4.BeautifulSoup(site_data.text, "lxml")
       links = data.find_all('a')
       for link in links:
           print(link['href'])
   ```

   This function takes a URL as input, retrieves the source code of the website using `requests.get()`, and then parses it using `BeautifulSoup` from `bs4`. It selects all the `<a>` tags in the website and prints the URLs found in their `href` attributes.

4. Call the `extract_links` function with the provided URL:

   ```python
   extract_links(url)
   ```

   This will execute the function and print the extracted URLs.

## Requirements

Before running the script, make sure you have the following libraries installed:

- requests
- bs4

You can install them by running the following command:

```
pip install requests bs4
```

## Author

This script was created by [Vinay Ghate](https://github.com/vinay-ghate).
