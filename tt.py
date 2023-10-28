import pandas as pd

def get_country_economic_data(country_code):
    try:
        # URL for World Bank's data API
        url = f'https://api.worldbank.org/v2/country/{country_code}?format=json'

        # Fetch the data
        response = pd.read_json(url)

        # Extract relevant economic data
        country_name = response[1][0]['name']
        gdp = response[1][0]['indicators']['NY.GDP.MKTP.CD'][0]['value']
        inflation = response[1][0]['indicators']['FP.CPI.TOTL.ZG'][0]['value']
        unemployment = response[1][0]['indicators']['SL.UEM.TOTL.ZS'][0]['value']

        return {
            'Country': country_name,
            'GDP (in USD)': gdp,
            'Inflation Rate': inflation,
            'Unemployment Rate': unemployment
        }
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Replace 'USA' with the country code of the country you want to assess
    country_code = 'USA'

    result = get_country_economic_data(country_code)
    if isinstance(result, dict):
        print("Economic Data for", result['Country'])
        print("GDP:", result['GDP (in USD)'])
        print("Inflation Rate:", result['Inflation Rate'], "%")
        print("Unemployment Rate:", result['Unemployment Rate'], "%")
    else:
        print(result)
