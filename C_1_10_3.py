class Customer:

    def __init__(self, name= "", balance=0):
        self.name = name
        self.balance = balance

    def data(self):
        self.name = str(input("Введите фамилию, имя и отчество: "))
        self.balance = float(input("Ваш баланс: "))
        return f"Клиент: {self.name}. Баланс: {self.balance}."

    def clientData(self):
            return f"Клиент: {self.name}. Баланс: {self.balance}."
while True:
    value = input("Введите 1, чтобы добавить клиента или 2, чтобы вывести данные о клиенте: ")
    if value == '1':
        client = Customer("", 0)
        print(client.data())
        break
    elif value == '2':
        client = Customer("Иванов Иван Иванович", 500)
        print(client.clientData())
        break
    else:
        print("Значение введено некорректно")
        continue
