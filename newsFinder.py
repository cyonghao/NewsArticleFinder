from newsapi import NewsApiClient
from tokenconfig import TOKEN

def main():
    # # User input for country of source
    # country = str(input("Enter the country of choice:  "))

    # # Displays list of sources based on country of choice
    # avail_sources = newsapi.get_sources(country=country)
    # avail_sources = avail_sources['sources']
    # for avail_source in avail_sources:
    #     print(avail_source['id'])

    # # User input for selected sources
    # selected_sources = str(input("Enter the source(s) of your choice, each separated with a comma:   "))
    # selected_sources = selected_sources.strip().replace(" ","").lower()

    # User input for selected keywords/ phrases
    keywords = str(input("Enter keywords/ phrases to search for, each separated with a comma:  "))
    keywords = ",".join([keyword.strip().lower() for keyword in keywords.split(",")])
    
    


if __name__ == "__main__":
    # Init
    newsapi = NewsApiClient(api_key=TOKEN)

    main()