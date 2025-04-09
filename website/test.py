from intasend import APIService

API_PUBLISHABLE_KEY = 'ISPubKey_test_e4014510-95df-488f-b2f8-f5ca520ffdf7'
API_TOKEN = 'ISSecretKey_test_a2112bbf-70f4-4315-8121-3c72ea48ec17'

service = APIService(
    token=API_TOKEN,
    publishable_key=API_PUBLISHABLE_KEY,
    test=True  # Mode test
)

# Format correct : indicatif pays sans '+' et sans espaces
# Remplacer temporairement l'appel à IntaSend par un mock
create_order = {
    'invoice': {
        'state': 'complete'
    },
    'id': 'TEST_PAYMENT_ID_123456'
}


print(create_order)