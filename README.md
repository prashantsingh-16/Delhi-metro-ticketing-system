# Delhi Metro Ticketing System Made by Python

A console-based transit route planning and ticketing application developed in Python. The system simulates commuter interactions across key Delhi Metro corridors (Yellow Line, Blue Line, and Red Line), offering corridor exploration, automated station matching, slab-based fare computation with peak rush-hour adjustments, and metro smart card transactions.

---

## Overview of the Project

The **Delhi Metro Ticketing System** serves as a terminal-based self-service kiosk for metro passengers. Built using clean, procedural programming principles without classes or external libraries, the application is divided into four distinct files:

- **`stations.py`**: Manages the metro line topology, stores station datasets, and handles case-insensitive station lookups.
- **`route.py`**: Computes station paths, stop counts, and estimated travel duration using bidirectional list slicing.
- **`fare.py`**: Calculates DMRC distance slab fares, checks for peak rush hours, and handles smart card balance deductions.
- **`main.py`**: Serves as the primary driver program handling the console UI, input validation, and transaction flow.

---

## Features

- **Corridor Selection**: Choose between major routes including the Yellow Line, Blue Line, and Red Line.
- **Case-Insensitive Input Handling**: Enter station names in lowercase, uppercase, or mixed case (e.g., `rajiv chowk`, `RAJIV CHOWK`, or `Rajiv Chowk`).
- **Bidirectional Traversal**: Automatically detects and handles forward and reverse journeys along the corridor.
- **Slab-Based Fare Calculation**:
  - 1–2 stops: ₹10
  - 3–5 stops: ₹20
  - 6–7 stops: ₹30
  - 8+ stops: ₹40
- **Rush Hour Surcharges**: Applies a 10% peak surcharge for trips taken during morning (08:00–10:00) and evening (17:00–20:00) rush hours.
- **Metro Smart Card Simulation**: Validates balances, executes fare deductions, and generates a formatted digital boarding token.

---

## Technologies/Tools Used

- **Programming Language**: Python 3.x
- **Core Concepts Used**: Lists, Dictionaries, Loops (`for`, `while`), Conditional Statements (`if-elif-else`), Custom Modular Functions
- **External Dependencies**: None (relies entirely on Python's built-in standard library)
- **Environment**: Any standard terminal, Command Prompt, or Python IDE (VS Code, IDLE, PyCharm)

---

## Steps to Install & Run the Project

1. Download the project ZIP file from GitHub.
2. Extract the downloaded ZIP file onto your computer.
3. Ensure that all 4 Python files (`stations.py`, `route.py`, `fare.py`, and `main.py`) are located in the **same folder**.
4. Open your command prompt or terminal, navigate to the folder, and run:
   ```bash
   python main.py
   ```

---

## Instructions for Testing

Run through the following test scenarios to verify system features:

### Test Case 1: Standard Route & Case-Insensitive Matching
- **Action**: Choose option `1` (Plan Journey & Buy Ticket).
- **Line Selection**: Select `1` (Yellow Line).
- **Boarding Station**: Type `new delhi` (lowercase).
- **Destination Station**: Type `saket` (lowercase).
- **Travel Hour**: Enter `14` (2:00 PM, off-peak).
- **Expected Result**:
  - Successfully resolves stations to `New Delhi` and `Saket`.
  - Displays 5 total stops with an estimated duration of ~10 minutes.
  - Base Fare: ₹20 | Rush Charge: ₹0 | Total Fare: ₹20.

### Test Case 2: Rush-Hour Peak Pricing
- **Action**: Select option `1`, choose Yellow Line (`1`).
- **Boarding Station**: `Kashmere Gate`.
- **Destination Station**: `Hauz Khas`.
- **Travel Hour**: Enter `9` (9:00 AM peak hour).
- **Expected Result**:
  - Base slab fare: ₹30.
  - Surcharge: 10% peak fee (+₹3.00), bringing the total fare to ₹33.00.

### Test Case 3: Reverse Corridor Journey
- **Action**: Select option `1`, choose Blue Line (`2`).
- **Boarding Station**: `Noida Electronic City`.
- **Destination Station**: `Karol Bagh`.
- **Travel Hour**: Enter `12`.
- **Expected Result**:
  - Route path prints in reverse order from Noida toward Karol Bagh.

### Test Case 4: Insufficient Balance Handling
- **Action**: Proceed to the smart card payment prompt (`y`).
- **Card Balance Input**: Enter a balance less than the trip fare (e.g., `5.00` when the fare is `20.00`).
- **Expected Result**:
  - Displays `Payment Failed: Not enough balance in card!` and returns safely to the main menu without deducting funds.

---

## Screenshots

### 1. Main Menu & Line Selection Screen
```text
*** DELHI METRO TICKETING SYSTEM ***
1. Plan Journey & Buy Ticket
2. View All Lines & Stations
3. Exit
Enter your choice (1-3): 1

--- Available Metro Lines ---
1. Yellow Line
2. Blue Line
3. Red Line
-----------------------------
Select the line you want to travel on (1-3): 1

--- Stations on Yellow Line ---
1 . Samaypur Badli
2 . Kashmere Gate
3 . Chandni Chowk
4 . New Delhi
5 . Rajiv Chowk
6 . Central Secretariat
7 . INA
8 . Hauz Khas
9 . Saket
10 . Huda City Centre
----------------------------------------

Enter Boarding Station: new delhi
Enter Destination Station: saket
Enter travel time (Hour 0 to 23): 14
```

### 2. Journey Details Screen
```text
--- YOUR JOURNEY DETAILS ---
Metro Line      : Yellow Line
Route Path      :
  1 -> New Delhi
  2 -> Rajiv Chowk
  3 -> Central Secretariat
  4 -> INA
  5 -> Hauz Khas
  6 -> Saket
Total Stops     : 5
Estimated Time  : 10 minutes
Base Fare       : Rs 20
Rush Hour Charge: Rs 0 (Normal hours)
Total Fare      : Rs 20
----------------------------

Do you want to pay with Smart Card? (y/n): y
Enter Card Number: DMRC-10928
Enter Current Balance (Rs): 100
```

### 3. Digital Metro Pass Screen
```text
=============================
     DELHI METRO PASS        
=============================
Line      : Yellow Line
Card No   : DMRC-10928
From      : New Delhi
To        : Saket
Fare Paid : Rs 20.0
Remaining : Rs 80.0
Status    : PAYMENT SUCCESSFUL
=============================
```
