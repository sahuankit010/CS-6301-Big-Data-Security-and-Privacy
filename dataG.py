import pandas as pd
import numpy as np  
from faker import Faker
import random
 
data = pd.DataFrame(columns=['text', 'sensitive'])
faker = Faker()
 
sensitive_data = [
    faker.iban,
    faker.credit_card_number,
    faker.password,
    faker.ssn,
    faker.address,
    faker.postcode,
    faker.name
]
 
for i in range(500000):
 
    text = faker.paragraph()
    if np.random.rand() < 0.15:
        sensitive = 1
 
        # Pick a random insertion point  
        rand_index = random.randint(0, len(text))
        # Insert sensitive data at random point
        text = text[:rand_index] + faker.random_element(sensitive_data)() + text[rand_index:]
 
    else:  
        sensitive = 0
 
    data.loc[i] = [text, sensitive]
print(data.sample(1))
data.to_csv('finalDataset1.csv', index=False)