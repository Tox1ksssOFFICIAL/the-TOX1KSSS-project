import random
import time


class Card:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.cards = []

    def add_card(self):
        q = input("Введи вопрос: ")
        a = input("Введи ответ: ")
        self.cards.append(Card(q, a))
        print("Карточка добавлена!")

    def show_random_card(self):
        if not self.cards:
            print("Карточек нет!")
            return
        card = random.choice(self.cards)
        print("Вопрос:", card.question)
        input("Нажми Enter чтобы показать ответ...")
        print("Ответ:", card.answer)

    def quiz(self):
        if not self.cards:
            print("Нет карточек для викторины!")
            return

        print("Начинаем викторину! На ответ 10 секунд.")
        score = 0

        for card in self.cards:
            print("\nВопрос:", card.question)
            start = time.time()
            ans = input("Ответ: ")
            end = time.time()

            if end - start > 10:
                print("Время вышло!")
            elif ans.lower() == card.answer.lower():
                print("Правильно!")
                score += 1
            else:
                print("Неверно! Правильный ответ:", card.answer)

        print("\nРезультат:", score, "/", len(self.cards))


print("=== Регистрация ===")
reg_login = input("Придумай логин: ")
reg_password = input("Придумай пароль: ")

user = User(reg_login, reg_password)

print("\n=== Вход ===")
while True:
    log = input("Логин: ")
    pas = input("Пароль: ")
    if log == user.login and pas == user.password:
        print("Вход успешен!\n")
        break
    print("Неверно! Попробуй снова.\n")

while True:
    print("\nМеню:")
    print("1 — Добавить карточку")
    print("2 — Показать случайную карточку")
    print("3 — Викторина")
    print("4 — Выход")

    choice = input("Выбери пункт: ")

    if choice == "1":
        user.add_card()
    elif choice == "2":
        user.show_random_card()
    elif choice == "3":
        user.quiz()
    elif choice == "4":
        print("До встречи")