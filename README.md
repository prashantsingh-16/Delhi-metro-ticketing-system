# Delhi-metro-ticketing-system
Python project on delhi metro ticketing system

A modular, console-based transit planning and ticketing utility developed in Python. The system simulates passenger workflows across major Delhi Metro lines (Yellow, Blue, and Red), providing automated station discovery, bidirectional corridor slicing, distance-based slab fare calculation with peak-hour adjustments, and metro smart card transactions.



Overview
The Delhi Metro Ticketing System replicates a digital ticketing kiosk for metro commuters. Built purely with modular procedural programming (no third-party dependencies or object-oriented boilerplate), the system organizes logic into three distinct functional modules:
1.Network Module (stations.py): Stores line corridors and provides case-insensitive station lookups.

2.Route Planner Module (route.py): Computes bidirectional paths, stops, and estimated travel duration using index slicing.

3.Fare Engine Module (fare.py): Applies DMRC-style distance slab rates, detects peak rush hours, and manages smart card wallet deductions.

4.Execution Interface (main.py): Presents a command-line interface (CLI) to guide users through line selection, trip routing, and ticket generation.
