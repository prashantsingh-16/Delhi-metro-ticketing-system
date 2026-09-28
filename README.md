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



<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Download README.md</title>
</head>
<body style="font-family: Arial, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 80vh; background-color: #f7f9fa;">

  <div style="background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center; max-width: 450px;">
    <h2 style="color: #333; margin-bottom: 10px;">Delhi Metro Ticketing System</h2>
    <p style="color: #666; font-size: 14px; margin-bottom: 25px;">Click the button below to download your generated <code>README.md</code> file.</p>
    
    <button id="downloadBtn" style="background-color: #007bff; color: white; border: none; padding: 12px 24px; font-size: 15px; font-weight: bold; border-radius: 6px; cursor: pointer; transition: background 0.2s;">
      📥 Download README.md
    </button>
  </div>

  <script>
    const markdownContent = `# Delhi Metro Ticketing System Made by Python

A console-based transit route planning and ticketing application developed in Python. The system simulates commuter interactions across key Delhi Metro corridors (Yellow Line, Blue Line, and Red Line), offering corridor exploration, automated station matching, slab-based fare computation with peak rush-hour adjustments, and metro smart card transactions.

---

## Overview of the Project

The **Delhi Metro Ticketing System** serves as a terminal-based self-service kiosk for metro passengers. Built using clean, procedural programming principles without classes or external libraries, the application is divided into four distinct files:

- **\`stations.py\`**: Manages the metro line topology, stores station datasets, and handles case-insensitive station lookups.
- **\`route.py\`**: Computes station paths, stop counts, and estimated travel duration using bidirectional list slicing.
- **\`fare.py\`**: Calculates DMRC distance slab fares, checks for peak rush hours, and handles smart card balance deductions.
- **\`main.py\`**: Serves as the primary driver program handling the console UI, input validation, and transaction flow.

---

## Features

- **Corridor Selection**: Choose between major routes including the Yellow Line, Blue Line, and Red Line.
- **Case-Insensitive Input Handling**: Enter station names in lowercase, uppercase, or mixed case (e.g., \`rajiv chowk\`, \`RAJIV CHOWK\`, or \`Rajiv Chowk\`).
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
- **Core Concepts Used**: Lists, Dictionaries, Loops (\`for\`, \`while\`), Conditional Statements (\`if-elif-else\`), Custom Modular Functions
- **External Dependencies**: None (relies entirely on Python's built-in standard library)
- **Environment**: Any standard terminal, Command Prompt, or Python IDE (VS Code, IDLE, PyCharm)

---

## Steps to Install & Run the Project

1. Download the project ZIP file from GitHub.
2. Extract the downloaded ZIP file onto your computer.
3. Ensure that all 4 Python files (\`stations.py\`, \`route.py\`, \`fare.py\`, and \`main.py\`) are located in the **same folder**.
4. Open your command prompt or terminal, navigate to the folder, and run:
   \`\`\`bash
   python main.py
   \`\`\`

---

## Instructions for Testing

Run through the following test scenarios to verify system features:

### Test Case 1: Standard Route & Case-Insensitive Matching
- **Action**: Choose option \`1\` (Plan Journey & Buy Ticket).
- **Line Selection**: Select \`1\` (Yellow Line).
- **Boarding Station**: Type \`new delhi\` (lowercase).
- **Destination Station**: Type \`saket\` (lowercase).
- **Travel Hour**: Enter \`14\` (2:00 PM, off-peak).
- **Expected Result**:
  - Successfully resolves stations to \`New Delhi\` and \`Saket\`.
  - Displays 5 total stops with an estimated duration of ~10 minutes.
  - Base Fare: ₹20 | Rush Charge: ₹0 | Total Fare: ₹20.

### Test Case 2: Rush-Hour Peak Pricing
- **Action**: Select option \`1\`, choose Yellow Line (\`1\`).
- **Boarding Station**: \`Kashmere Gate\`.
- **Destination Station**: \`Hauz Khas\`.
- **Travel Hour**: Enter \`9\` (9:00 AM peak hour).
- **Expected Result**:
  - Base slab fare: ₹30.
  - Surcharge: 10% peak fee (+₹3.00), bringing the total fare to ₹33.00.

### Test Case 3: Reverse Corridor Journey
- **Action**: Select option \`1\`, choose Blue Line (\`2\`).
- **Boarding Station**: \`Noida Electronic City\`.
- **Destination Station**: \`Karol Bagh\`.
- **Travel Hour**: Enter \`12\`.
- **Expected Result**:
  - Route path prints in reverse order from Noida toward Karol Bagh.

### Test Case 4: Insufficient Balance Handling
- **Action**: Proceed to the smart card payment prompt (\`y\`).
- **Card Balance Input**: Enter a balance less than the trip fare (e.g., \`5.00\` when the fare is \`20.00\`).
- **Expected Result**:
  - Displays \`Payment Failed: Not enough balance in card!\` and returns safely to the main menu without deducting funds.

---

## Screenshots

### 1. Main Menu & Line Selection Screen
\`\`\`text
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
\`\`\`

### 2. Journey Details Screen
\`\`\`text
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
\`\`\`

### 3. Digital Metro Pass Screen
\`\`\`text
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
\`\`\`
`;

    document.getElementById('downloadBtn').addEventListener('click', () => {
      const blob = new Blob([markdownContent], { type: 'text/markdown;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'README.md');
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(url);
    });
  </script>
</body>
</html>
