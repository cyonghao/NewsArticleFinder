from newsapi import NewsApiClient
from tokenconfig import TOKEN

def main():
    # User input for country of source
    country = str(input("Enter the country of choice:  "))

    # User input for language of source
    # language = str(input("Enter the language of choice:  "))

    # Displays list of sources based on country of choice
    avail_sources = newsapi.get_sources(country=country)
    avail_sources = avail_sources['sources']
    for avail_source in avail_sources:
        print(avail_source['id'])

if __name__ == "__main__":
    # Init
    newsapi = NewsApiClient(api_key=TOKEN)

    main()