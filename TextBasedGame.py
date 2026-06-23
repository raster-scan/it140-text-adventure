# Randy Cornetta
# IT 140 Project - Text Based Game
# Updated version with normalized user input
# Fixed a game over bug
# Update 6/23/26


def show_instructions():
    # Display the game title, goal, and available commands.
    print("IT Support Escape Game")
    print("Collect all 6 IT items before entering the Server Room.")
    print("If you enter the Server Room before collecting all items, System Crash wins.")
    print()
    print("Move commands: go North, go South, go East, go West")
    print("Get item command: get <item name>")
    print("Example: get Diagnostic Cable")
    print("Type exit to quit the game.")
    print("-" * 50)


def show_status(current_room, inventory, rooms):
    # Display the player's current room, room description, inventory, and room item.
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
    # Run the main gameplay loop.
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

        # Store the original input, then normalize a copy for command checking.
        command = input("Enter your move: ").strip()
        normalized_command = command.lower()

        # Validate blank input before checking for commands.
        if normalized_command == "":
            print("Please enter a command.")

        # Let the player quit the game.
        elif normalized_command == "exit":
            print("Thanks for playing the game. Hope you enjoyed it.")
            game_over = True

        # Validate a bare go command with no direction.
        elif normalized_command == "go":
            print("Please enter a direction after go.")

        # Handle movement commands.
        elif normalized_command.startswith("go "):
            direction_input = normalized_command[3:].strip()

            valid_move = None
            for direction in rooms[current_room]:
                if direction.lower() == direction_input:
                    valid_move = direction

            if valid_move is not None:
                current_room = rooms[current_room][valid_move]

                # Check for win/lose immediately upon entering a new room
                if current_room == villain_room:
                    if len(inventory) == required_items:
                        print()
                        print("Congratulations! You collected all items and stopped System Crash!")
                    else:
                        print()
                        print("System Crash was too strong. GAME OVER!")
                    print("Thanks for playing the game. Hope you enjoyed it.")
                    game_over = True
            else:
                print("You cannot go that way!")

        # Validate a bare get command with no item.
        elif normalized_command == "get":
            print("Please enter an item name after get.")

        # Handle item collection commands.
        elif normalized_command.startswith("get "):
            item_name = command[4:].strip()

            if "item" in rooms[current_room]:
                room_item = rooms[current_room]["item"]

                if item_name.lower() == room_item.lower():
                    inventory.append(room_item)
                    del rooms[current_room]["item"]
                    print(f"{room_item} retrieved!")  # Uses official item name casing
                else:
                    print("Cannot get that item!")
            else:
                print("There is no item to get in this room.")

        # Handle all other invalid commands.
        else:
            print("Invalid command!")

# Added the dunder name to be more inline with Python standards
if __name__ == "__main__":
    main()