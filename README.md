# oopAssignment13

Repository for Assignment 13 - Object Oriented Programming with a ski rental system.

## Concepts Used
Object Oriented Programming (OOP)

## Overview

The assignment is to create a ski rental shop system using Object Oriented Principles (OOP) in Python. The system manages inventory, skis, and snowboards through a set of well-defined classes with support for hourly, daily, and weekly rentals, best-price logic, family discounts, and coupon codes.

## Project Structure

```
oopAssignment13/
├── main.py
├── README.md
└── classes/
    ├── equipment.py
    ├── inventory.py
    ├── rental.py
    ├── rental_shop.py
    ├── skis.py
    └── snowboards.py
```

## Classes

- **Equipment** (`classes/equipment.py`): Abstract base class for rental equipment; stores hourly, daily, and weekly rates
- **Ski** (`classes/skis.py`): Concrete subclass of Equipment with hard-coded ski rates
- **Snowboard** (`classes/snowboards.py`): Concrete subclass of Equipment with hard-coded snowboard rates
- **Inventory** (`classes/inventory.py`): Tracks available skis and snowboards; handles stock checks and updates
- **Rental** (`classes/rental.py`): Represents a single rental transaction; handles billing, discounts, and bill printing
- **Rental_Shop** (`classes/rental_shop.py`): Main shop class; coordinates inventory and active rentals

## Data for each Class

- **Equipment**: `hourly_rate`, `daily_rate`, `weekly_rate`
- **Ski**: Hard-coded rates — $15/hr, $50/day, $200/week
- **Snowboard**: Hard-coded rates — $10/hr, $40/day, $160/week
- **Inventory**: `skis_available`, `snowboards_available`
- **Rental**: `item_type`, `quantity`, `rental_type`, `duration`, `coupon_code`
- **Rental_Shop**: Instance of `Inventory`, list of active `Rental` objects

## Methods per Class

- **Equipment**: `get_hourly_rate()`, `get_daily_rate()`, `get_weekly_rate()`, `get_rates()`, `equipment_type()` (abstract)
- **Ski / Snowboard**: Override `equipment_type()` → returns `"Ski"` or `"Snowboard"`
- **Inventory**: `get_stock()`, `check_availability(type, quantity)`, `update_stock(type, quantity, rent=True)`, `display_inventory()`
- **Rental**: `get_equipment_type()`, `get_quantity()`, `get_detail()`, `calculate_bill()`, `print_bill()`
- **Rental_Shop**: `display_inventory()`, `process_rental(rental)`, `return_rental(rental)`, `get_active_rentals()`, `get_inventory()`

## Pricing Logic

Billing lives in `Rental.calculate_bill()` and applies the following rules in order:

1. **Best price** — automatically selects the cheapest rate for the rental duration:
   - Hourly: compared against the daily rate (cheaper at 4+ hours)
   - Daily: full weeks are priced at the weekly rate when it saves money
   - Weekly: straight weekly rate × duration
2. **Family discount** — 25% off when renting 3–5 items total
3. **Coupon discount** — 10% off when the coupon code ends in `BBP` (e.g. `SKIBBP`, `MYBBP`)
4. Discounts **stack** when both apply

## Relationships Between Classes

- `Rental_Shop` → contains an `Inventory` instance and a list of `Rental` objects
- `Rental_Shop` delegates stock management to `Inventory`
- `Ski` and `Snowboard` → extend `Equipment`
- `Rental` → standalone transaction object consumed by `Rental_Shop`

## Requirements

- Python 3.x
- No external dependencies

## Usage

```bash
python main.py
```

> **Note:** `main.py` is currently used as a test driver to verify class behavior. It exercises rentals, returns, inventory updates, edge cases (insufficient stock), family discounts, coupon codes, and stacked discounts.

## Progress

| Task | Status |
|------|--------|
| Identify the classes needed for this system | Done |
| Determine the data each class should store | Done |
| Determine the methods each class should have | Done |
| Design relationships between the classes | Done |
| Write and test those classes | Done |
| Write a README.md file for the assignment | Done |

> **Note:** "In Progress" means the work may be functionally complete but has not yet been reviewed and signed off by all team members.