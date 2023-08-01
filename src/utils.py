from typing import List

from factory import Factory, Faker as FactoryFaker

from src.user_statistics import UserStatistics


class UserStatisticsFactory(Factory):
    class Meta:
        model = UserStatistics

    id = FactoryFaker('random_int', min=1, max=1000)
    first_name = FactoryFaker('first_name')
    last_name = FactoryFaker('last_name')
    points = FactoryFaker('random_int', min=0, max=100)


def fake_user_data() -> List[UserStatistics]:
    num_users = 100
    user_data = [UserStatisticsFactory() for _ in range(num_users)]
    return user_data
