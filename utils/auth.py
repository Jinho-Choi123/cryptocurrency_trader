import os
from dotenv import load_dotenv
import jwt
import uuid

load_dotenv()

API_ACCESS_KEY = os.environ.get('ACCESS_KEY')
API_SECRET_KEY = os.environ.get('SECRET_KEY')


def payload(query_hash = '', query_hash_alg = ''):
    if(query_hash == '' and query_hash_alg == ''):
        return {
        'access_key': API_ACCESS_KEY,
        'nonce': str(uuid.uuid4()),
        }
    else:
        return {
        'access_key': API_ACCESS_KEY,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': query_hash_alg,   
        }


def headers(query_hash = '', query_hash_alg = ''):
    payload_ = payload(query_hash, query_hash_alg)
    jwt_token = jwt.encode(payload_, API_SECRET_KEY)
    authorization_token = 'Bearer {}'.format(jwt_token)
    return {"Authorization": authorization_token}


