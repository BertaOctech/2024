from encryption import Encryption
from utils import convert_key, convert_iv

encrypted_email = "JFNKPSVfvNhhIRPSFNaH4JBZTmZFk54f+c3tN/gSoffZ3DrrvxvcQAtDXJSuZBu7axRLGCE+HD+ismHtMnrnYtbCpQZxwclovn0H5BY06rE27xh40/uJTa1K6UCFBM/5oN7xbxJXxHQ209P6F6fRt7aCtn+AGA4ke1dGAqbcmjHl71GNdWWxqiRW6W1Dak6+jlUfm685FHfeUt2pSOKzDAmkb8qRcnCBOPRKDtroqjqxpMJCAf6cs/M4tu7xizOWJlrd0qRH2/qyoD2wuJ7X9/Y53o+v1KMxsWoL0t/7UJ7SOYwykNIxhwd7jrGT08ubKZfa0/8uYb0/qi5vRvl9oov5XxOBXwvaa1/yFy+giidR/ORsjN3xgTm5JuNJelQnY12qW3VX0w+N6srhqDGyMa31Sj//SPIEPHJApHMoGEWNKODJ1mevKgt4kJY6oXdZjefT08vQX3YdYadlNnnqm2ieR5Z/49LGo1tI11+PcSmQ3sTQMqhM4WRSijCFuA339wi2o7drz27QploRkENu8z47xi5rOoGFfIN9xiQsvsDeGVfhQq1P7ooT4daYkirvIhaDiPjgIRiydAKKL0jGt6QX2A841XI1aV+8hNpLhP7rbcNYsUTxkWZT0LKX2We/EKz/6LvewF4ZXxJo+yCntfYhxJsHKVwINm2owkbMJplH/BDBJmpousnQcPzMvpUFvE8u+LN6zCTf4s/stcen3wVcCjWiInFAPJCjSqU8xXy0Y6B7ReK50M+HCfuW+AM/FozOVD76En+7E15BBHmVZQwGsJlBrKKhniXFBiAelSM7KMSdXvYl1TMUSPqh0NlXrnqLPCWp3rMoE8fhhqawZ7oHAvdKQWQqtUY5Cb/IbN61mPLPaPLnBAKxxXLSQMf4b7iQnKc764w99o4hgs9lq9s6NFs80OT1ex54Lp49M7lN9Rxg6VtxDraA22G4j+rdBKryoxDd5K4f1avS1PJ9bTmmgjb+26VDMtrJ5bWIPuW0EroZCZgtQwzGeoXOQ3dP93rLyw9ytcQiJSB3OLs7LPj0wW/Y8HWsV6FhV9C75397owaQAarPg6R1SU6osoOJDAHqYC+WRzVwnl28w1YYBmiMvsNimmq0Z4lmHdtZKY5VSNas1cuSXUj0RCH5SHi6gZKKxMGpHJmHZ7lqbfOQlyUQVyJ7yg9rBWYvDzkZLe/t1VdllenbYv1KMkkcoCkF5sNKE1x8CjU6d99XF5fCSjj/S74joAcm1OW8RGJIUQis4DweJy+0Us/NU7lzyYdlBkPND7kQ+fO/wwCs4PmBf5zHIZirLsFy2kJ8x6s3ky/FEkx+iiXWZ896JPd5kbUeL9DC1aMZ9BOww0unjIrEk/nH619TokSW11A5DL4o5Q1ofjIkSq/PbfKhsq8B7OznDUcNu4896t/4/59S1BK84nrJErgZyQ0fEwlVlcd89os="

key = convert_key('Advent Of Craft')
iv = convert_iv('2024')
encryption_instance = Encryption(key, iv)

decripted_email = encryption_instance.decrypt(encrypted_email)

print(decripted_email)