import pymongo
from flask import Flask
import requests
from flask_apscheduler import APScheduler
# import schedule

# Initialize app
app = Flask(__name__)
scheduler = APScheduler()

URL = "https://objectivismrelativism.myshopify.com"
ACCESS_TOKEN = "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"
SECRET_KEY = "b5bc98ad3199589679bd85781661a86f"
API_KEY = "e892c944852691aca4b235bf7ec67ae4"
MONGO_CONNECTION_URI = 'mongodb+srv://JashanpreetSingh-dev:Jashan04$@cluster0.urbakzt.mongodb.net/?retryWrites=true&w=majority'


@app.route("/")
def hello_world():
    return get_all_products()


def write_data():
    Db_Client = pymongo.MongoClient(MONGO_CONNECTION_URI)
    db = Db_Client.get_database('prototype')
    collection = db.get_collection('orders')
    list_of_docs = get_all_products()['data']['orders']["edges"]
    # dict = {"name": "Jashan", "Work": "Hacker"}
    collection.insert_many(list_of_docs)


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


# if __name__ == '__main__':
#     scheduler.add_job(id='Scheduled task', func=write_data, trigger='interval', seconds=10)
#     scheduler.start()
#     app.run()
