from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    return main()


URL = "https://objectivismrelativism.myshopify.com"
ACCESS_TOKEN = "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"
SECRET_KEY = "b5bc98ad3199589679bd85781661a86f"
API_KEY = "e892c944852691aca4b235bf7ec67ae4"
PASSWORD = "Jashan04$"
COMBINED_URL = f"https://{API_KEY}:{PASSWORD}@objectivismrelativism.myshopify.com/admin/api/2022-07"


def get_all_products():
    query = """{
  orders(first: 10) {
    edges {
      node {
        name
        customer {
          id
          numberOfOrders
        }
        currentSubtotalPriceSet {
          shopMoney {
            amount
          }
        }
        cartDiscountAmountSet {
          shopMoney {
            amount
          }
        }
        currentSubtotalPriceSet {
          shopMoney {
            amount
          }
        }
        totalShippingPriceSet {
          shopMoney {
            amount
          }
        }
        totalTaxSet {
          shopMoney {
            amount
          }
        }
        currentTotalPriceSet {
          shopMoney {
            amount
          }
        }
        createdAt
      }
    }
  }
}
"""

    url = f'{URL}/admin/api/2022-07/graphql.json'
    r = requests.post(url, auth=(API_KEY, ACCESS_TOKEN), json={"query": query})
    return r.json()


def main():
    return get_all_products()


if __name__ == '__main__':
    main()
