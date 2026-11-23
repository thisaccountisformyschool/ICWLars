import datetime

def read_from_file():
    diary = []
    try:
        with open("diary.txt", "r") as diary_file:
            diary_text = diary_file.read()
            diary_split = diary_text.split("\n")
            diary_split.pop(-1)
        for entry in diary_split:
            entry_split = entry.split(": ")
            diary.append({"date":entry_split[0],"text":entry_split[1]})
        print(diary)
        return diary
    except FileNotFoundError:
        diary_file = open("diary.txt","x")
        return diary



diary = read_from_file()

# diary = [
#     {"date":"09/11/2026","text":"Ik ben wakker geworden in een vliegtuig"},
#     {"date":"01/01/2001","text":"Vliegtuig lessen gegeven"}
# ]

def menu():
    print("")
    print("1) Add diary entry \n2) Show diary \n3) Delete entry \n4) Close program")
    try:
        choice = int(input())
    except ValueError:
        choice = 2
    if choice == 1:
        add_diary_entry()
    elif choice == 2:
        show_dairy()
    elif choice == 3:
        delete_entry()
    elif choice == 4:
        exit()

def delete_entry():
    date = input("Date: ")
    amount = 0
    diary_dated = []
    for entry in diary:
        if date == entry["date"]:
            diary_dated.append(entry)
            amount += 1
    if amount > 1:
        for entry in diary_dated:
            print(f"{entry["date"]}: {entry["text"]}")
            delete = input("Delete? (y/n) ")
            if delete == "y":
                diary.remove(entry)
            if delete == "n":
                pass

    elif amount == 1:
        diary.remove(diary_dated[0])
    elif amount == 0:
        print("No entry on that date")

    write_to_file()

def show_dairy():
    print("")
    for item in diary:
        print(f"{item["date"]}: {item["text"]}")
    input("(Press enter to continue)")

def add_diary_entry():
    print("")
    datum = input("Date: ")
    tekst = input("Text: ")
    diary.append({"date":datum,"text":tekst})
    write_to_file()

def write_to_file():
    with open("diary.txt","w") as diary_file:
        for entry in diary:
            diary_file.write(f"{entry["date"]}: {entry["text"]}\n")

while True:
    menu()