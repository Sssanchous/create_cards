import file_operations

import random

import os

from faker import Faker


FAKE = Faker("ru_RU")

SKILLS = [
    "Стремительный прыжок", "Электрический выстрел", "Ледяной удар",
    "Стремительный удар", "Кислотный взгляд", "Тайный побег",
    "Ледяной выстрел", "Огненный заряд"
]

LETTERS_MAPPING = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}


def sort_text():
    for i in range(len(SKILLS)):
        for y in SKILLS[i]:
            if y in LETTERS_MAPPING:
                SKILLS[i] = SKILLS[i].replace(y, LETTERS_MAPPING[y])


def create_cards():
    unique_skills = random.sample(SKILLS, 3)
    context = {
        "first_name": FAKE.first_name_male(),
        "last_name": FAKE.last_name_male(),
        "job": FAKE.job(),
        "town": FAKE.city(),
        "strength": random.randint(3, 18),
        "agility": random.randint(3, 18),
        "endurance": random.randint(3, 18),
        "intelligence": random.randint(3, 18),
        "luck": random.randint(3, 18),
        "skill_1": unique_skills[0],
        "skill_2": unique_skills[1],
        "skill_3": unique_skills[2]
        }
    return context


def main():
    os.makedirs('output/svg', mode=0o777, exist_ok=True)
    sort_text()
    for i in range(10):
        context = create_cards()
        file_operations.render_template(
            "src/charsheet.svg",
            f"output/svg/result-{i+1}.svg",
            context)


if __name__ == '__main__':
    main()
