# Randy Cornetta
# IT 140 Project - Text Based Game
# Updated 6/21/26

def show_instructions():
    #Display the game title, goal, and available commands.
    print("IT Support Escape Game")
    print("Collect all 6 IT items before entering the Server Room.")
    print("If you enter the Server Room before collecting all items, System Crash wins.")
    print()
    print("Move commands: go North, go South, go East, go West")
    print("Get item command: Get <item name>")
    print("Example: Get Diagnostic Cable")
    print("-" * 50)


def show_status(current_room, inventory, rooms):
    #Display the player's current room, room description, inventory, and room item.
    print()
    print("You are in the", current_room)
    print(rooms[current_room]["description"])
    print("Available directions:",
          ", ".join(direction for direction in rooms[current_room]
                    if direction not in ["item", "description"]))
    print()

    if inventory:
        print("Inventory:")
        for item in inventory:
            print("-", item)
    else:
        print("Inventory: []")

    if "item" in rooms[current_room]:
        print("You see a", rooms[current_room]["item"])

    print("-" * 50)


def main():
    #Run the main gameplay loop.
    rooms = {
        "Front Entrance": {
            "North": "Help Desk",
            "East": "Repair Lab",
            "description": "The front doors are locked behind you. Warning lights flash across the lobby."
        },
        "Help Desk": {
            "North": "Training Room",
            "South": "Front Entrance",
            "East": "Break Room",
            "West": "Inventory Room",
            "item": "Diagnostic Cable",
            "description": "Open support tickets cover the screens. The system failure is spreading fast."
        },
        "Inventory Room": {
            "East": "Help Desk",
            "item": "Replacement SSD",
            "description": "Shelves of spare parts line the walls. A storage bin is open near the workbench."
        },
        "Training Room": {
            "South": "Help Desk",
            "East": "Network Closet",
            "item": "Knowledge Base Notes",
            "description": "Training computers sit in rows. Troubleshooting notes are scattered on the desks."
        },
        "Network Closet": {
            "West": "Training Room",
            "item": "Admin Keycard",
            "description": "Switches blink rapidly in the rack. Access cards hang near the network equipment."
        },
        "Break Room": {
            "West": "Help Desk",
            "North": "Server Room",
            "item": "Coffee",
            "description": "The room smells like old coffee. You may need energy before the final repair."
        },
        "Repair Lab": {
            "West": "Front Entrance",
            "item": "Toolkit",
            "description": "Workbenches are covered with tools, cables, and half-repaired devices."
        },
        "Server Room": {
            "South": "Break Room",
            "description": "The server racks are overheating. System Crash is waiting in the darkness."
        }
    }

    inventory = []
    current_room = "Front Entrance"
    required_items = 6
    villain_room = "Server Room"
    game_over = False

    show_instructions()

    while not game_over:
        show_status(current_room, inventory, rooms)

        command = input("Enter your move: ").strip().title()

        # Validate blank input before checking for commands.
        if command == "":
            print("Please enter a command.")

        # Validate a bare go command with no direction.
        elif command == "Go":
            print("Please enter a direction after go.")

        # Handle movement commands.
        elif command.startswith("Go "):
            direction = command[3:]

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You cannot go that way!")

        # Validate a bare get command with no item.
        elif command == "Get":
            print("Please enter an item name after get.")

        # Handle item collection commands.
        elif command.startswith("Get "):
            item_name = command[4:]

            if "item" in rooms[current_room]:
                room_item = rooms[current_room]["item"]

                if item_name == room_item:
                    inventory.append(room_item)
                    del rooms[current_room]["item"]
                    print(room_item, "retrieved!")
                else:
                    print("Cannot get that item!")
            else:
                print("There is no item to get in this room.")

        # Handle all other invalid commands.
        else:
            print("Invalid command!")

        # Check for the win or lose condition after each command.
        if current_room == villain_room:
            if len(inventory) == required_items:
                print()
                print("Congratulations! You collected all items and stopped System Crash!")
                print("Thanks for playing the game. Hope you enjoyed it.")
            else:
                print()
                print("System Crash was too strong. GAME OVER!")
                print("Thanks for playing the game. Hope you enjoyed it.")

            game_over = True


main()
