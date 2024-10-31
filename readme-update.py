from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import random
import logging
import os

class QuoteScraper:
    def __init__(self):
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        # Setup Chrome options
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        
        # Add random user agent
        ua = UserAgent()
        self.chrome_options.add_argument(f'user-agent={ua.random}')
        
        # Base URL
        self.base_url = "https://www.brainyquote.com/topics/success-quotes"
        
        # Retry settings
        self.max_retries = 3
        self.retry_delay = 30

    def setup_driver(self):
        """Initialize and return a Chrome WebDriver"""
        return webdriver.Chrome(options=self.chrome_options)

    def get_quote(self):
        """Get a random quote from BrainyQuote"""
        driver = None
        try:
            driver = self.setup_driver()
            
            # Generate random page and quote numbers
            page_number = random.randrange(1, 16, 1)
            quote_number = random.randrange(1, 67, 1)
            
            # Construct URL and quote ID
            url = f"{self.base_url}_{page_number}" if page_number > 1 else self.base_url
            id_quote = f'pos_{page_number}_{quote_number}'
            
            # Load page
            driver.get(url)
            
            # Wait for quote element
            wait = WebDriverWait(driver, 10)
            quote_element = wait.until(
                EC.presence_of_element_located((By.ID, id_quote))
            )
            
            # Check if it's an ad
            if 'm-ad-brick' in quote_element.get_attribute('class'):
                logging.info('Quote not found, retrying...')
                return self.get_quote()
            
            # Extract quote and author
            quote = quote_element.find_element(By.CLASS_NAME, 'b-qt').text.strip()
            author = quote_element.find_element(By.CLASS_NAME, 'bq-aut').text.strip()
            
            return quote, author
            
        except Exception as e:
            logging.error(f"Error getting quote: {str(e)}")
            return self.get_quote() if self.max_retries > 0 else (None, None)
            
        finally:
            if driver:
                driver.quit()

    def update_readme(self, file_path, quote, author):
        """Update README.md with new quote"""
        try:
            with open(file_path, "r") as f:
                content = f.readlines()
                
            for i, line in enumerate(content):
                if line.startswith("```html"):
                    content[i+1] = f"\"{quote}\"\n"
                    content[i+2] = f"<!-- {author} -->\n"
                    break
                    
            with open(file_path, "w") as f:
                f.writelines(content)
                
            logging.info("README.md updated successfully")
            
        except Exception as e:
            logging.error(f"Error updating README: {str(e)}")

def main():
    scraper = QuoteScraper()
    quote, author = scraper.get_quote()
    
    if quote and author:
        scraper.update_readme("README.md", quote, author)
        logging.info(f"Updated quote: {quote} - {author}")
    else:
        logging.error("Failed to get quote")

if __name__ == "__main__":
    main()