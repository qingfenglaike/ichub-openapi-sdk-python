from ichubOpenApi import client

app_id = '********************'
app_key = '********************'
sign_type = "MD5"

items = [
    {
        'sku': '111', 'brand': '', 'datecode': '', 'quality': '', 'date_of_delivery': '', 'moq': '',
        'coo': '', 'product_qty': 1, 'price_unit': '', 'price_interval': '', 'description': '', 'product_code': ''
    },
    {
        'sku': '222', 'brand': '', 'datecode': '', 'quality': '', 'date_of_delivery': '', 'moq': '',
        'coo': '', 'product_qty': 1, 'price_unit': '', 'price_interval': '', 'description': '', 'product_code': ''
    }
]
Client = client.Client(host='http://test.open.ichub.com', sign_type=sign_type, key=app_key, app_id=app_id)
print(Client.uploadsupply(currency_id="R", tax_rate="1.11", items=items))
