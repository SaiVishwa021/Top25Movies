# Top 25 Movies Flask App

## Overview

This application uses web scraping techniques to retrieve the top 25 movies for a specified year from IMDB. Web scraping involves extracting data from websites by simulating human browsing behavior. In this app, we use `Requests` to make HTTP requests and `BeautifulSoup` to parse and extract relevant movie information from the HTML content.

## What is Web Scraping?

Web scraping is a technique used to extract data from websites. It involves fetching a web page's content and then parsing and processing the HTML to obtain the desired information. This process simulates human browsing behavior to gather data that is not readily available through traditional means.

### How It Works

1. **Send HTTP Request:**
   The application sends an HTTP GET request to the IMDB page that lists the top movies for the specified year.

2. **Parse HTML Content:**
   The HTML response is then parsed using `BeautifulSoup`. This library allows us to navigate the HTML structure and extract the desired data.

3. **Extract Movie Information:**
   The application searches for the movie elements within the HTML content. It retrieves details such as the movie title, rank, and other relevant information.

4. **Save Data:**
   After extracting the movie details, the data is saved to a CSV file in the `dataset` folder. This CSV file can be used for further analysis or reference.

### Dependencies

- **Requests:** Used for sending HTTP requests to retrieve the web page content.
- **BeautifulSoup4:** Used for parsing and extracting data from HTML content.


## Features

- Scrape movie data from IMDB from 1950.
- Save the retrieved movie information to a dataset folder.
- Simple and intuitive user interface.
- Input a specific year to fetch the top 25 movies from the user.


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SaiVishwa021/Top25Movies.git
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
## Example
To fetch the top 25 movies for the year 2023, enter 2023 in the input field and click "Submit". The app will display the top 25 movies and save the data to dataset/top_25_movies_2023.csv.

## Acknowledgements
- IMDB for movie data.
- Flask for the web framework.
- Requests and BeautifulSoup for web scraping.

Feel free to adjust the content to fit any additional specifics about your project!


