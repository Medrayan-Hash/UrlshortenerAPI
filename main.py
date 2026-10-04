import string
import random

characters=string.ascii_letters+string.digits

token=[]

for c in range(5):
    character=random.choice(characters)
    token.append(character)


short_code="".join(token)

