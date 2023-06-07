import jwt

secret_key = 'Thejourneyofathousandmilesbeginswithasinglestep'


def api_response(message="something went wrong. try again later.", data=None, status_code=400):
    return {
        "message": message,
        "data": {} if data is None else data,
        "status_code": status_code
    }


# Generate a JWT token
def create_jwt_token(payload):
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token


# Verify and decode the JWT token
def verify_jwt_token(token):
    try:
        jwt.decode(token, secret_key, algorithms=['HS256'])
        return True
    except jwt.InvalidTokenError:
        return False
