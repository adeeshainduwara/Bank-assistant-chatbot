from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import requests
import db_helper

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def handle_request(request: Request):
    payload = await request.json()
    intent = payload['queryResult']['intent']['displayName']
    output_contexts = payload['queryResult']['outputContexts']
    parameters = output_contexts[0]['parameters']
    parameters2 = payload['queryResult']['parameters']

    intent_handler_dict = {
        'check-balance': check_balance,
        'interest-rate': interest_rate
    }

    print(intent, parameters, sep="\n")
    return intent_handler_dict[intent](parameters)


def check_balance(parameters):
    account_number = parameters['Account_Number']
    balance = db_helper.get_balance(account_number)
    fulfillment_text = f"Your account balance is Rs {balance}"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

def interest_rate(parameters):
    account_number = parameters['Account_Number']
    interest_rate = db_helper.get_interest_rate(account_number)
    fulfillment_text = f"Interest rate of your account is {interest_rate}%"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })
