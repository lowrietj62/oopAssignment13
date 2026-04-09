# oopAssignment13

Repository for Assignment 13 - Object Oriented Programming with a ski rental system.

## Overview

The assignment is to create a ski rental shop system using Object Oriented Principles (OOP) in Python. The system manages customers, inventory, skis, and snowboards through a set of well-defined classes.

## Classes

- Rental: Represents the rental object
- Rental Shop: The main class for handling anything to do with the ski rental shop
- Inventory: Base class for tracking available rental equipment
- Equipment: Base class for skis and snowboards
- Skis: Class for handling anything to do with skis seperately
- Snowboards: Class for handling anything to do with snowboards seperately

## Data for each Class

- Rental: equipment_type, quantity, period_type, duration, coupon_code
- Rental_Shop: Instance of Inventory class, List of active rentals
- Inventory: Available Skis/Snowboards
- Equipment: equipment_id, rental_rate_hourly, rental_rate_daily, rental_rate_weekly
- Skis: Hard-coded rates
- Snowboards: Hard-coded rates

## Methods each class has

- Rental: calculate_bill() [This is where the best price logic lives, family discount and coupon discount checks as well]
- Rental_Shop: display_inventory(), process_rental(...), return_rental(rental object) [This will trigger billing]
- Inventory: check_availability(type, quantity), update_stock(type, quantity)
- Equipment: get_rates(), equipment_type()
- Skis: Override equipment_type()
- Snowboards: Override equipment_type()

## Relationships between classes

- Rental: Its own object (represents the rental item)
- Rental Shop: Pulls from Inventory
- Inventory: Base class for rental shop
- Equipment: Base class for skis and snowboards
- Skis: Pulls from equipment
- Snowboards: Pulls from equipment


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