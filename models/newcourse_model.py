from faker import Faker

fake = Faker("Ru-ru")


class NewCourse:
    def __init__(
            self,
            full_name=None,
            short_name=None,
            description=None,
    ):
        self.full_name = full_name
        self.short_name = short_name
        self.description = description

    @staticmethod
    def random():
        full_name = fake.bs()
        short_name = full_name
        description = fake.text(max_nb_chars=300)

        return NewCourse(
            full_name,
            short_name,
            description,
        )
