def wwesti_zadachi():
    zadachi = []
    while True:
        try:
            id= int(input("введите id задачи"))
            zadacha=input("введите задачу")
            status=False
            zadachi.append((id, zadacha, status))
            print(f"Задача '{zadacha}' (ID: {id}) добавлена.")
        except ValueError:
            print("неверный формат данных")
            continue
        status=False
        user_choice = input("\n (Введите любую цифру для выхода, или нажмите Enter для продолжения): ")
        if user_choice.isdigit():
            break
    return zadachi

if __name__ == "__main__":
    my_tasks = wwesti_zadachi()
    print("\n--- Все добавленные задачи ---")
    for task_id, task_description, task_status in my_tasks:
        status_str = "Выполнено" if task_status else "Не выполнено"
        print(f"ID: {task_id}, Описание: {task_description}, Статус: {status_str}")

    while True:
        try:
            task_to_change_id = int(input("\nВведите ID задачи, в которой хотите изменить статус (или 0 для выхода): "))
            if task_to_change_id == 0:
                break

            found = False
            for i, task in enumerate(my_tasks):
                if task[0] == task_to_change_id:
                    my_tasks[i] = (task[0], task[1], not task[2])
                    print(
                        f"Статус задачи ID {task_to_change_id} изменен на {'Выполнено' if my_tasks[i][2] else 'Не выполнено'}.")
                    found = True
                    break
            if not found:
                print(f"Задача с ID {task_to_change_id} не найдена.")

        except ValueError:
            print("Неверный формат данных. ID задачи должен быть числом.")

    print("\n--- Задачи после возможных изменений ---")
    for task_id, task_description, task_status in my_tasks:
        status_str = "Выполнено" if task_status else "Не выполнено"
        print(f"ID: {task_id}, Описание: {task_description}, Статус: {status_str}")






