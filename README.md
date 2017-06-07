teambition-client
-----------------

a simple client of teambition API for python

## Installation

```bash
pip install git+https://github.com/jackeyGao/teambition-client
```

## QuickStart

```python
from teambition import Teambition

client_id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
client_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

sdk = Teambition(client_id, client_secret)
print(sdk.get_authorize_url(redirect_url))

# 访问上面的地址获取code

access_token = sdk.get_access_token(code)
sdk.set_token(token)
sdk.get('users/me')  # 个人信息接口
```
