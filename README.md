# LinkedIn-Jobs-Scraper
This Python program is designed to scrape job postings from LinkedIn based on specific criteria.
# Usage
Install the required packages by running:
    pip install requests beautifulsoup4 pandas
# Run the script to scrape LinkedIn job postings.

# Script Description
This script scrapes job postings from LinkedIn for the search query "machine learning" in New Zealand.
# Script Features
get_page(page): Function to extract web pages using requests and BeautifulSoup.
transform_page(sp): Function to transform extracted web pages into structured data.
Loop through Pages: The script loops through multiple pages of job listings on LinkedIn.
Data Storage: Scraped job listings are stored in a Pandas DataFrame and saved to a CSV file.

# Note
Make sure to replace 'ML_jobs_in_NewZealand.csv' with your desired file name.
Adjust the search query and location in the LinkedIn URL (url2) as needed.

# Sample output 
![Sample_Output](https://github.com/aminuali/LinkedIn-Jobs-Scraper/assets/56072102/05c9d774-c748-4fff-b430-288546c65836)
