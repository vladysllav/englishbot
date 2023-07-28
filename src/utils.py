from typing import List
from faker import Faker
from src.user_statistics import UserStatistics


def fake_user_data() -> List[UserStatistics]:
    fake = Faker()
    num_users = 100
    user_data = []
    for i in range(num_users):
        id = fake.random_int(min=1, max=1000)
        first_name = fake.first_name()
        last_name = fake.last_name()
        points = fake.random_int(min=0, max=100)
        user = UserStatistics(id=id, first_name=first_name, last_name=last_name, points=points)
        user_data.append(user)
    return user_data
