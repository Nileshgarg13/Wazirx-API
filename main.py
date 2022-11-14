
import pandas as pd
import requests

URL="https://api.wazirx.com/sapi/"

def apiHelpers(endpoint):
    headers={
            "Content-Type": "application/x-www-form-urlencoded",
        }
    response = requests.get(URL+endpoint, headers)
    if response.status_code==200:
        return response.json()
    else:
        print("Something went wrong !")
        quit()

def dataParser(data, options):
    if data:
        dataset = pd.DataFrame(data)
        if len(options):
            options="|".join(options)
            return dataset.loc[dataset['symbol'].str.contains(options,regex=True)]
        else:
            print("Coin Pair Names not Found !")
            quit()
    else:
        print("Data not found !")
        quit()

def writeFile(fileName, data):
    try:
        data.to_excel(fileName)
        print("Done")
    except:
        print("Writing to file went wrong !")


responseData = apiHelpers('v1/tickers/24hr')
coinPairs=["btcinr","ethinr","solinr","xrpinr","dogeinr"]
data=dataParser(responseData,coinPairs)
writeFile("priceData.xlsx",data)
