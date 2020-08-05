import sqlite3



def main_menu():
    print('------------------------------')
    print('1- Inserir uma nova conta')
    print('2- Vizualizar as contas salvas')
    print('3- Recuperar uma senha')
    print('4- Editar uma conta')
    print('5- Excluir uma conta')
    print('0- Sair')
    print('------------------------------')


def clear_terminal():
    return print('\x1b[2J')

def save_data(app_n, app_p):
    cursor.execute(f"""
                    INSERT INTO passwords (name, password) VALUES (?, ?)
                   ;""", (app_n, app_p))
    connect.commit()

def show_name_apps():
    cursor.execute("""
                    SELECT name FROM passwords
                   ;""")

def recover_password(name):
    cursor.execute(f"""
                    SELECT name, password FROM passwords WHERE name = '{name}'
                  ;""")

def edit_account(app_n, new_pass):
    cursor.execute(f"""
                   UPDATE passwords SET password = '{new_pass}' WHERE name = '{app_n}'
                   ;""")

def delete_account(app_n):
    cursor.execute(f"""
                   DELETE FROM passwords WHERE name = '{app_n}'
                   ;""")

#Connect to database
connect = sqlite3.connect('passkey.db')
cursor = connect.cursor()


while True:

    clear_terminal()
    main_menu()
    a = input('Opção: ')

    if a == '1': # Input of new app and password
        app_name = input('Insira o nome do app: ')
        app_password = input('Insira a senha: ')
        save_data(app_name, app_password)

    elif a == '2':
        show_name_apps()# Show all app's saved
        print('--------------------------')
        print('*****APPS CADASTRADOS*****')

        for name in cursor.fetchall():
            print(name[0])
        print('--------------------------')
        input('Aperte enter para continuar...')
    elif a == '3': # Show all app's saved and edit app password
        show_name_apps()
        names = []
        for name in cursor.fetchall():
            names.append(name[0])
            print(name[0])
        while True:
            account_name = input('Digite o nome da conta que você deseja recuperar a senha: ')
            if account_name in names:
                recover_password(account_name)
                data = cursor.fetchone()
                print(f'A senha da conta {data[0]} é {data[1]}')
                input('Aperte enter pra continuar...')
                break
    
    elif a == '4':
        show_name_apps()
        apps = []
        for app in cursor.fetchall():
            apps.append(app[0])
            print(app[0])
        print('------------------------------')
        print('Só é permitido alterar a senha')
        while True:
            account_name = input('Digite o nome da conta que você deseja editar a senha: ')
            if account_name in apps:
                new_pass = input(f'Digite a nova senha para a conta {account_name}: ')
                edit_account(account_name, new_pass)
                break
    elif a == '5':
        show_name_apps()
        apps = []
        for app in cursor.fetchall():
            apps.append(app[0])
            print(app[0])
        print('-----------------------------')
        while True:
            account_name = input('Digite o nome da conta que será deletada: ')
            if account_name in apps:
                delete_account(account_name)
                break

    elif a == '0': # End software
        break
connect.close()
print('Software Finalizado')
