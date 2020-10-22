import requests

presidents = []


# Get the requests from the url provided in the main
def getRequest(url):
    return requests.get(url).json()


#
def parseResponse(response):
    data = []
    for element in response['RelatedTopics']: # loop through the RelatedTopics
        # this function grabs the the first url,
        # splits it based on the / character, gets the last element and replaces the '_' with blank '' spaces
        data.append(element['FirstURL'].split('/')[-1].replace('_', ' '))

    print(data)
    return data


def displayResults(results):
    for element in results:
        print(element)


def main():
    URL = 'https://api.duckduckgo.com/?q=presidents%20of%20the%20united%20states&format=json&pretty=1%22'
    response = getRequest(URL)
    presidents = parseResponse(response)
    displayResults(presidents)


if __name__ == '__main__':
    main()
