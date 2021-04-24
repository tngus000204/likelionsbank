# from main import account_list


def create_account():
    account_number = int(input("계좌번호: "))
    name = input("이름: ")
    deposit = int(input("예금: "))
    return (account_number, name, deposit)
