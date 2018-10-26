import json
import random
import string

import requests


def auth_api(token):
    res = requests.post(url=' https://serene-wildwood-35121.herokuapp.com/oauth/getDetails', data={
        'token': token,
        'secret': '40e05b687fe391deef99f10aced9ebc9096cd0410190ae5ef4fc797c02df9ce0cf7455b3be59baa0810e855dce66f80f4cb81d0a2d84dfa95877d46c3c15c861'
    })

    res = json.loads(res.content)
    email = res['student'][0]['Student_Email']
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    print(email, password)

    return email, password
