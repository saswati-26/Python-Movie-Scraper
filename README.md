Repository Title:

  Python Movie Scraper

README.md:

Python Movie Scraper
  This repository contains a Python web scraper for fetching movie data from IMDb and displaying it on a web page using Flask.

Description:

  This project consists of two main components:

  IMDb Web Scraper (imdb_scrape.py):
    Utilizes BeautifulSoup and Requests libraries to scrape movie data from IMDb pages.
    Retrieves movie names, genres, images, and descriptions.
    Returns the scraped data in JSON format.
    Web Application (app.py):
    
  Uses Flask to create a web application.
    Retrieves movie data from the IMDb scraper and passes it to an HTML template for display.
    Renders an HTML page that showcases movie information, including name, genre, image, and description.
    
Usage:

Clone the repository:
  bash
  Copy code
    git clone https://github.com/your-username/python-movie-scraper.git
    
Install dependencies:
  Copy code
    pip install -r requirements.txt
    
Run the Flask application:
  Copy code
    python app.py
    
Open your web browser and navigate to http://localhost:4000 to view the movie information.

Note:

  Make sure to have Python installed on your system.
  
This project utilizes external libraries such as BeautifulSoup, Requests, Flask, and Jinja2. Make sure to install them using the provided requirements.txt file.

Contributing:

  Contributions are welcome! Feel free to open an issue or submit a pull request with any improvements or additional features you'd like to see.

License:

  This project is licensed under the MIT License. See the LICENSE file for details.
  
