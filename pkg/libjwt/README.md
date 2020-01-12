<h1 style="text-align:center">libjwt</h1>

> 这是一个python的 `json web token` 的精简实现, 可直接被用于认证

+ [使用说明](#Examples)

+ [理论基础](#Theory)

  

## Examples

```python
from libjwt import Jwt

# create object
Judge = Jwt()

# singn to json, default use HS256
# Cryptographically signed token = xxxxxx.xxxxxx.xxxxxx
token = Judge.sign({
    "id": 1,
    "name": "root",
    "exp": 60,
    "create_at": 28337838
})

# if isPass == False; decoded = None
# else decodee = {"id":1, "name":"root","exp": 60,"create_at": 28337838}
decoded,isPass = Judge.verify(token)
```



## Theory

### constructor

+ 第一部分我们称它为头部（header),

+ 第二部分我们称其为载荷（payload, 类似于飞机上承载的物品)，

+ 第三部分是签证（signature).



### 1.header

**header由库内部提供了创建， 使用HS256**

jwt的头部承载两部分信息：

- 声明类型，这里是jwt
- 声明加密的算法 通常直接使用 HMAC SHA256

```json
{
  "typ": "JWT",
  "alg": "HS256"
}
```



### 2.playload

jwt的playload是自定义保存的内容

```json
{
    "id": 1,
    "name": "root",
    "exp": 60,
    "create_at": 28337838
}
```



### 3.signature
```
token = SIGN(str, publicSecret)

str = VERIFY(token, privateSecret)
```


- str = base64(header) + '.' +base64(payload)
- publicSecret(公钥) 用于加密
- privateSecret(私钥) 用于解密