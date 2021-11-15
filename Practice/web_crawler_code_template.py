import logging, sys, requests, re, csv

#______________________________________________________________________

def get_category_list(content):
    
    """get_category_list takes content of home plage and returns 
    a list of categories and their urls"""
    
    pass
#______________________________________________________________________

def get_book_list(content):
    
    """get_book_list takes content of a book list page
    and returns a list of books (name and url)"""
    
    pass

#______________________________________________________________________

def get_product_details(content):
    
    """get_product_details takes content of a product page, 
    parses the page and returns details about a product"""
    
    pass

#______________________________________________________________________

def get_page_content(url):
    
    """get_page_content takes a url and returns the content of the page"""
    
    pass

#______________________________________________________________________

def get_next_page(content):
    
    """checks the content of a book list page and returns 
    link of the next page, return None, if there is no more next page"""
    
    pass

#______________________________________________________________________

def scrape_book_info(book_info, category_name):
    
    """gets the content of a book details page,
    and parses different components and stores the info"""
    
    pass

#______________________________________________________________________

def crawl_category(category_name, category_url):
    
    """crawls a particular category of books"""
    
    while True:
        
        content = get_page_content(category_url)
        
        book_list = get_book_list(content)
        
        for book in book_list:
            
            scrape_book_info(book, category_name)
            
            if get_next_page(content) is None:
                
                break
    
#______________________________________________________________________

def crawl_website():
    
    """This is the main function that coordinates the whole crawling task"""
    
    url = "http://books.toscrape.com/index.html"
    
    host_name = "books.toscrape.com"
    
    content = get_page_content(url)
    
    category_list = get_category_list(content)
    
    for category in category_list:
        
        category_name, category_url = category
        
        crawl_category(category_name, category_url)
        
#______________________________________________________________________
    
if __name__ == '__main__':
    
    logging.basicConfig(format='%(asctime)s %(message)s', 
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        filename="bookstore_crawler.log", 
                        level=logging.DEBUG)
    
    with open("book_list.csv", "w") as csvf:
        
        csv_writer = csv.DictWriter(csvf, fieldnames=["Name", "Category", "UPC", "URL", "ImageURL", "Price", "Availability", "Description"])
        
        csv_writer.writeheader()
        
        crawl_website()