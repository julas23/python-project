from dataclasses import dataclass
from typing import Optional

@dataclass
class Job:
    title: str
    salary: int

@dataclass
class Person:
    name: str
    age: int
    email: str
    job: Job | None = None

if __name__ == "__main__":
    name = input("Digite o nome da pessoa: ")
    age = int(input(f"Digite a idade de {name}: "))
    email = input(f"Digite o e-mail de {name}: ")

    has_job = input(f"{name} tem um emprego? (s/n): ").strip().lower()

    if has_job == 's':
        title = input("Digite o título do emprego: ")
        salary = int(input("Digite o salário: "))
        job = Job(title=title, salary=salary)
        person = Person(name=name, age=age, email=email, job=job)
    elif has_job == 'n':
        title = input("Com o que quer trabalhar: ")
        salary = int(input("Digite o salário desejado: "))
        job = Job(title=title, salary=salary)
        person = Person(name=name, age=age, email=email, job=job)
    else:
        print(f"{name} Voce e um Vagabundo!")
        person = Person(name, age, email)

    print(person)