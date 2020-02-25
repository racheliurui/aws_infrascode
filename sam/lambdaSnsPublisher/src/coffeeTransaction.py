'''
{
 "orderId": "UUID",
 "timestamp": "YYYYMMDDHHMMSSSSSS",
 "orderItems": [{
 "coffeeName": "SageBrew | ElasticBean | CoffeeFormation",
 "number": 1,
 "size": "L"
 },
 {
 "coffeeBrandName": "ElesticBean",
 "number": 1,
 "size": "S"
 }
 ],
 "orderPayable": 10.4
 "channel": "alexa | web | connect| button"
}
'''

import uuid
import random
import json
from datetime import datetime, timedelta

##Global Config
coffeeNameList=["SageBrew","ElasticBean","CoffeeFormation"]
coffeeProductList=["Flatwhite","Longblack","Espresso"]
sizeList=["S","M","L"]
channels =["alexa","web","connect","button"]

def getProductFullList():

    productList=[]
    for coffeeName in coffeeNameList:
        for size in sizeList:
            for coffeeProductName in coffeeProductList:
              product={
                  "coffeeName":coffeeName,
                  "coffeeProductName": coffeeProductName,
                  "size":size
              }
              productList.append(product)
    return productList

productFullList=getProductFullList()

def getDummyCoffeeOrder():
    orderId=str(uuid.uuid4())
    now = datetime.now() + timedelta(seconds=random.randint(0,60))
    message={
     "orderId": str(uuid.uuid4()),
     "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
     "orderItems": getDummyItems(),
     "channel" : random.choice(channels),
     "orderPayable": 10.4
    }
    return message

def getDummyItems():
    orderItemList=random.sample(productFullList, random.randint(1,5))
    dummyItems=[]
    for orderItem in orderItemList:
        dummyItem=getDummyItem(orderItem["coffeeName"],orderItem['coffeeProductName'],orderItem["size"])
        dummyItems.append(dummyItem)
    return dummyItems

def getDummyItem(coffeeName,coffeeProductName, size):
    numberOfCups=[1,2,3,4]
    orderItem={
    "coffeeName": coffeeName,
    "coffeeProductName": coffeeProductName,
    "number": random.choice(numberOfCups),
    "size": size
    }
    return orderItem
