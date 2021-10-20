"""
https://developer.scb/#/documents/documentation/qr-payment/payment-confirmation.html
"""

from typing import Literal, Optional, Union
from fastapi import FastAPI, Request, Body
from pydantic import BaseModel, Field
from fastapi_utils.api_model import APIModel
from enum import Enum
app = FastAPI()

class PaymentConfirmation(APIModel):
    transaction_id: str = Field(..., description='Transaction ID generated by source system',)
    amount: str = Field(..., description='Amount of Transaction',)
    transaction_date_and_time: str = Field(..., alias='transactionDateandTime', description='Date and Time of transaction in ISO 8601 format SCB EASY App Payment (BP), SCB EASY App Payment (CCFA), SCB EASY App Payment (IPP), QR30, Alipay, WeChatPay : Time in GMT+7 QRCS : Time in GMT')
    currency_code: str = Field(..., description="Code to define currency for transaction based on ISO 4217 for transactionAmount. Thai Baht is ‘764’")
    transaction_type: Union[str]

    merchant_id: Optional[str] = None
    terminal_id: Optional[str] = None
    qr_id: Optional[str] = None
    merchant_pan: Optional[str] = None
    consumer_pan: Optional[str] = None
    trace_no: Optional[str] = None
    authorize_code: Optional[str] = None

    payee_proxy_type: Optional[str] = None
    payee_proxy_id: Optional[str] = None
    payee_account_number: Optional[str] = None
    payee_name: Optional[str] = None

    payer_proxy_id: Optional[str] = None
    payer_proxy_type: Optional[str] = None
    payer_name: Optional[str] = None
    payer_account_name: Optional[str] = None
    payer_account_number: Optional[str] = None

    bill_payment_ref1: Optional[str] = None
    bill_payment_ref2: Optional[str] = None
    bill_payment_ref3: Optional[str] = None
    sending_bank_code: Optional[str] = None
    receiving_bank_code: Optional[str] = None
    channel_code: Optional[str] = None

    payment_method: Optional[str] = None
    tenor: Optional[str] = None
    ipp_type: Optional[str] = None
    product_code: Optional[str] = None

    exchange_rate: Optional[str] = None
    equivalent_amount: Optional[str] = None
    equivalent_currency_code: Optional[str] = None
    company_id: Optional[str] = None

    invoice: Optional[str] = None
    note: Optional[str] = None

@app.post("/v1/scb")
async def handle_scb_callback(confirmation:PaymentConfirmation):

    return {
        "resCode": "00",
        "resDesc ": "success",
        "transactionId": confirmation.transaction_id,
        "confirmId" : "abc00confirm"
    }