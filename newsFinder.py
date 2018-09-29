from newsapi import NewsApiClient
from tokenconfig import TOKEN

def main():
    # User input for country of source
    country = str(input("Enter the country of choice:  "))

    # Displays list of sources based on country of choice
    avail_sources = newsapi.get_sources(country=country)
    avail_sources = avail_sources['sources']
    for avail_source in avail_sources:
        print(avail_source['id'])

    # User input for selected sources
    selected_sources = str(input("Enter the source(s) of your choice, each separated with a comma:   "))
    selected_sources = selected_sources.strip().replace(" ","").lower()

    # User input for selected keywords/ phrases
    keywords = str(input("Enter keywords/ phrases to search for (use the AND / OR / NOT keywords, and optionally group these with parenthesis. Eg: crypto AND (ethereum OR litecoin) NOT bitcoin):  "))
    # keywords = ",".join([keyword.strip().lower() for keyword in keywords.split(",")])
    
    # User input for period of article 
    # from_date = str(input("Enter the oldest date (period of article) of your choice, in YYYY-MM-DD format:  "))
    # to_date = str(input("Enter the latest date (period of article) of your choice, in YYYY-MM-DD format (if none, leave blank):  "))

    # Returns articles
    # if to_date == "" or " ":
    #     all_articles = newsapi.get_everything(q=keywords, sources=selected_sources, from_param=from_date, sort_by="relevancy")
    # else:
    #     all_articles = newsapi.get_everything(q=keywords, sources=selected_sources, from_param=from_date, to_param=to_date, sort_by="relevancy")

    all_articles = newsapi.get_everything(q=keywords, sources=selected_sources, sort_by="relevancy")
    print(all_articles)

if __name__ == "__main__":
    # Init
    newsapi = NewsApiClient(api_key=TOKEN)

    main()