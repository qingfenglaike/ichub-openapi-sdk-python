from ichubOpenApi import client

app_id = '2916ce5c8c31bbcf9d34954e0a98cbb3'
app_key = 'W0ZkINUqP9gm0D0n'
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
Client = client.Client(sign_type=sign_type, key=app_key, app_id=app_id)
Client.uploadsupply(currency_id="R", items=items)