from faker import Faker
import pandas as pd


fake = Faker()

#Used for fake data generation
df = pd.DataFrame({"Names": [fake.name() for i in range(10)]})
