# oopAssignment13

Repository for Assignment 13 - Object Oriented Programming with a ski rental system.

## Overview

The assignment is to create a ski rental shop system using Object Oriented Principles (OOP) in Python. The system manages customers, inventory, skis, and snowboards through a set of well-defined classes.

## Classes

- Customer: Represents the customer
- Ski Rental Shop: The main class for handling anything to do with the ski rental shop
- Inventory: Base class for tracking available rental equipment
- Skis: Class for handling anything to do with skis seperately
- Snowboards: Class for handling anything to do with snowboards seperately
- Main


## Data for each Class

- Customer: Current items in cart, current # of rented skis and snowboards, current rental period type, best price recommendation, and bill
- Ski Rental Shop: Family Rental Promotion and coupon code
- Inventory: Maximum # of skis and snowboards, and current # of skis and snowboards
- Skis: hourly, daily and weekly rate
- Snowboards: hourly, daily and weekly rate
- Main


## Methods each class has



## Relationships between classes

Ski Rental Shop: Pulls from Inventory
Skis: Pulls from Inventory
Snowboards: Pulls from Inventory
Customer: Pulls from Ski Rental Shop
Main: Pulls from Skis, Snowboards, and Customer


## Progress

| Task | Status |
|------|--------|
| Identify the classes needed for this system | Done! |
| Determine the data each class should store | In Progress |
| Determine the methods each class should have | In Progress |
| Design relationships between the classes, if any | In Progress |
| Write and test those classes | In Progress |
| Write a README.md file for the assignment | In Progress |

** Please note: In progress CAN mean that it's finished, but will NOT been set as DONE until ALL team members review changes and agree that it's ready or considered finished.

## Requirements

- Python 3.x (Doesn't matter which version of Python you use to run this so long as it's Python Version 3)
- No external dependencies

## Usage

```bash
python main.py
```