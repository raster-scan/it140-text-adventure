# IT-140 Text Adventure Game: Confronting System Crash

## Overview

This project is a text-based adventure game created in Python for IT-140: Introduction to Scripting.

The player takes on the role of an IT technician responding to a critical system outage caused by the villain **System Crash**. To successfully resolve the issue, the player must navigate through different areas of the office, collect essential troubleshooting items, and confront the villain in the Server Room.

The project demonstrates the use of:

- Variables
- Conditional statements
- Loops
- Functions
- Dictionaries
- User input handling
- Inventory management

---

## Story

A major outage has struck the company network. Reports indicate that a mysterious force known as **System Crash** has brought down critical services.

As the lead technician, you must explore the office, gather the tools and information needed to diagnose the problem, and enter the Server Room fully prepared.

Collect all six required items before confronting System Crash, or risk losing the battle against the outage.

---

## Game Map

```text
                 Training Room
                       |
                 Network Closet

Inventory Room -- Help Desk -- Break Room
                                      |
                                 Server Room

                Front Entrance
                       |
                  Repair Lab
```

---

## Rooms and Items

| Room | Item |
|--------|--------|
| Help Desk | Diagnostic Cable |
| Inventory Room | Replacement SSD |
| Training Room | Knowledge Base Notes |
| Network Closet | Admin Keycard |
| Break Room | Coffee |
| Repair Lab | Toolkit |
| Server Room | System Crash (Villain) |

---

## Commands

### Move Between Rooms

```text
Go North
Go South
Go East
Go West
```

### Pick Up Items

```text
Get Diagnostic Cable
Get Replacement SSD
Get Knowledge Base Notes
Get Admin Keycard
Get Coffee
Get Toolkit
```

### Exit the Game

```text
Exit
```

---

## Win Condition

To win the game:

1. Explore every room.
2. Collect all six items.
3. Enter the Server Room with all required items.

If all items have been collected, System Crash is defeated and the network is restored.

---

## Lose Condition

Entering the Server Room without all required items results in defeat.

The outage remains unresolved, and System Crash wins.

---

## Technologies Used

- Python 3
- Dictionaries
- Lists
- Functions
- While Loops
- Conditional Logic

---

## Learning Objectives

This project was created to demonstrate:

- Dictionary-based room navigation
- Inventory tracking using lists
- Input validation
- Function creation and reuse
- Game loop design
- Basic software design principles

---

## Author

**Randy Cornetta**

Created as part of the IT-140 Introduction to Scripting course.
