mobiles = []


def add_mobile():
    print("\n--- Add Mobile ---")

    mobile_id = int(input("Enter Mobile ID: "))

    for mobile in mobiles:
        if mobile[0] == mobile_id:
            print("That ID is already in use.")
            return

    brand = input("Enter Brand: ")
    model = input("Enter Model: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    mobiles.append([mobile_id, brand, model, price, quantity])
    print("Mobile added.")


def display_mobiles():
    print("\n--- Mobile List ---")

    if not mobiles:
        print("No mobiles found.")
        return

    print("-" * 65)
    print(f"{'ID':<8}{'Brand':<15}{'Model':<20}{'Price':<12}{'Qty':<8}")
    print("-" * 65)

    for mobile in mobiles:
        print(
            f"{mobile[0]:<8}"
            f"{mobile[1]:<15}"
            f"{mobile[2]:<20}"
            f"{mobile[3]:<12.2f}"
            f"{mobile[4]:<8}"
        )

    print("-" * 65)


def search_mobile():
    print("\n--- Search Mobile ---")

    mobile_id = int(input("Enter Mobile ID: "))

    for mobile in mobiles:
        if mobile[0] == mobile_id:
            print("\nMobile found")
            print("ID       :", mobile[0])
            print("Brand    :", mobile[1])
            print("Model    :", mobile[2])
            print("Price    :", mobile[3])
            print("Quantity :", mobile[4])
            return

    print("Mobile not found.")


def update_mobile():
    print("\n--- Update Mobile ---")

    mobile_id = int(input("Enter Mobile ID: "))

    for mobile in mobiles:
        if mobile[0] == mobile_id:
            print("\nCurrent details")
            print("Brand    :", mobile[1])
            print("Model    :", mobile[2])
            print("Price    :", mobile[3])
            print("Quantity :", mobile[4])

            print("\nEnter new details")
            mobile[1] = input("Enter Brand: ")
            mobile[2] = input("Enter Model: ")
            mobile[3] = float(input("Enter Price: "))
            mobile[4] = int(input("Enter Quantity: "))

            print("Mobile updated.")
            return

    print("Mobile not found.")


def delete_mobile():
    print("\n--- Delete Mobile ---")

    mobile_id = int(input("Enter Mobile ID: "))

    for mobile in mobiles:
        if mobile[0] == mobile_id:
            print("\nBrand :", mobile[1])
            print("Model :", mobile[2])

            choice = input("Delete this mobile? (Y/N): ")

            if choice.lower() == "y":
                mobiles.remove(mobile)
                print("Mobile deleted.")
            else:
                print("Delete cancelled.")
            return

    print("Mobile not found.")


def dashboard():
    while True:
        print("\n" + "=" * 38)
        print("       MOBILE SHOP MANAGEMENT")
        print("=" * 38)
        print("1. Add Mobile")
        print("2. Display All Mobiles")
        print("3. Search Mobile")
        print("4. Update Mobile")
        print("5. Delete Mobile")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_mobile()
        elif choice == "2":
            display_mobiles()
        elif choice == "3":
            search_mobile()
        elif choice == "4":
            update_mobile()
        elif choice == "5":
            delete_mobile()
        elif choice == "6":
            print("Thank you for using Mobile Shop Management.")
            break
        else:
            print("Invalid choice.")


def main():
    dashboard()


if __name__ == "__main__":
    main()
