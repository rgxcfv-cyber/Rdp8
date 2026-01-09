import random
import os
import time

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    print("-----ENJOY THIS SCRIPT----  Version: 1.0 | OWNER:@TELEADDERO")
    print("-THIS SOFTWARE IS SUCCESSFULLY CREATED BY @TELEADDERO-")
    print()

def menu():
    print("SELECT A OPTION:")
    print("EXIT OPTIONS:")
    print("[01] GENERATE NEW TELEGRAM ACCOUNT")
    print("[02] EXIT")
    print("[03] CLEAR")
    print()

def telegram_message(code):
    print("Login code:", code)
    print("Do not give this code to anyone, even if they say they are from Telegram!")
    print("! This code can be used to log in to your Telegram account.")
    print("We never ask it for anything else.")
    print("If you didn't request this code by trying to log in on")
    print("another device, simply ignore this message.")
    print("No messages found in chat history.")

def generate_account():
    while True:
        clear()
        banner()

        print("GENERATING NEW ACCOUNT... ACCOUNT NUMBER:")
        print()

        account_number = "+880" + str(random.randint(1000000000, 1999999999))
        login_code = random.randint(10000, 99999)

        print("ACCOUNT NUMBER:", account_number)
        print("PRESS ENTER AFTER SENDING OTP")
        input()

        print()
        telegram_message(login_code)
        print()
        telegram_message(login_code)

        input("\nPRESS ENTER TO GET NEW ACCOUNT: ")

def main():
    while True:
        clear()
        banner()
        menu()
        choice = input("Enter your choice: ")

        if choice in ["1", "01"]:
            generate_account()
        elif choice in ["2", "02"]:
            print("EXIT")
            break
        elif choice in ["3", "03"]:
            clear()
        else:
            print("INVALID OPTION")
            time.sleep(1)

if __name__ == "__main__":
    main()
