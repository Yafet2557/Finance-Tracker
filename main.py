from dotenv import load_dotenv
import os

from fastapi import FastAPI

app = FastAPI()

load_dotenv()
PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")


@app.get("/auth")
async def read_root():
    return {"Message": " Hello World"}

@app.get("/transactions")
async def get_transactions():
    return {"Message": "Transactions"}

@app.get("/balance")
async def get_balance():
    return {"Message": "Balance"}

@app.get("/accounts")
async def get_accounts():
    return {"Message": "Accounts"}



