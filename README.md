# Seeking Alpha Scraper
This is a cloud function that fetches the stock price and percentage change of a given ticker from the Seeking Alpha website and returns the values as a json dictionary.

## How to deploy the function
To deploy this function on DigitalOcean, follow these steps:

1. Create a new cloud function on your DigitalOcean account.
2. Copy the contents of the craper.py file and paste it into the "Function code" section of the cloud function.
3. Save the changes and test the function by providing a JSON input like {"ticker": "AAPL"}.
4. If the function runs successfully, you can configure it to be triggered by events like HTTP requests or schedule it to run at specific intervals.

## How to run the function
To run the function, you can send an HTTP request to the endpoint of the deployed cloud function with the ticker parameter in the JSON body. Here's an example using the curl command:

```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL"}' \
  https://<function_endpoint_url>
```

Replace <function_endpoint_url> with the URL of the deployed cloud function.

The function will return a JSON response with the stock ticker, price, and percentage change, like this:

```
{
    "body": {
        "ticker": "AAPL",
        "price": "$125.91",
        "change": "-0.01 (-0.01%)"
    }
}
```

That's it! You can use this cloud function to fetch stock information for any ticker listed on Seeking Alpha.