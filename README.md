# Delhi Metro Ticketing System Made by Python

A console-based transit planning and ticketing utility developed in Python. The system simulates passenger workflows across major Delhi Metro lines (Yellow, Blue, and Red), providing automated station selection, route display, distance-based slab fare calculation with peak-hour adjustments, and metro smart card transactions.

---

## Overview

The **Delhi Metro Ticketing System** replicates a digital ticketing kiosk for metro commuters. Built using simple, modular procedural programming without any complex classes or external libraries, the system organizes its operations into four Python scripts:

1. **Network Module (`stations.py`)**: Stores line corridors and provides case-insensitive station lookups.
2. **Route Planner Module (`route.py`)**: Computes paths, number of stops, and estimated travel duration using basic list slicing.
3. **Fare Engine Module (`fare.py`)**: Applies DMRC distance slab rates, detects peak rush hours, and handles smart card wallet deductions.
4. **Main Interface (`main.py`)**: Guides the user through choosing lines, selecting stations, calculating journeys, and issuing digital boarding passes.

---

## Features

- **Multi-Line Selection**: Choose to travel on the Yellow Line, Blue Line, or Red Line.
- **Case-Insensitive Input**: Type station names in lowercase, uppercase, or mixed case (e.g., `rajiv chowk`, `RAJIV CHOWK`, or `Rajiv Chowk`).
- **Bidirectional Traversal**: Automatically tracks journeys forward or in reverse order depending on your boarding and destination stations.
- **Slab-Based Fare Calculation**:
  - 1 to 2 stops: ₹10
  - 3 to 5 stops: ₹20
  - 6 to 7 stops: ₹30
  - 8+ stops: ₹40
- **Rush Hour Surcharge**: Automatically detects peak hours (08:00–10:00 and 17:00–20:00) and applies a 10% peak surcharge.
- **Metro Smart Card Payment**: Validates available balance, deducts trip fare, and prints an updated balance summary.

---

## Technologies/Tools Used

- **Programming Language**: Python 3.x
- **Built-in Functions & Data Types**: Lists, Dictionaries, Basic Loops (`for`, `while`), Conditional Statements (`if-elif-else`)
- **Execution Environment**: Any standard Terminal, Command Prompt, or Python IDE (VS Code, PyCharm, IDLE)

---

## Steps to Install & Run the Project

1. Download the ZIP file from GitHub.
2. Extract the downloaded ZIP file onto your computer.
3. Ensure all 4 Python files (`stations.py`, `route.py`, `fare.py`, and `main.py`) are located in the **same folder**.
4. Run `main.py` in your terminal or command prompt:
   ```bash
   python main.py


  </script>
</body>
</html>
