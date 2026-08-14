"""
Content for the site. Edit this file to update what shows up —
no HTML editing required. build.py imports RESUME from here.
"""

RESUME = {
    "name": "Cody Glad",
    "title": "Firmware Engineer / Embedded Systems",
    "tagline": "I approach code development as a craftsman.",
    "location": "West Jordan, UT",
    "email": "codymglad@gmail.com",
    "github": "https://github.com/zerihemla",
    "linkedin": "https://www.linkedin.com/in/cody-glad-903821149/",

    "about": (
        "I build things that have to work reliably in the real world.<br><br>"
         "I have worked on the full firmware stack, from architecting real-time systems to writing low-level drivers<br><br>" 
         "My experience spans the full embedded system spectrum. From designing PCBs, building prototypes, and creating the tools that make those systems easier to test and understand.<br><br>"
         "I’m drawn to difficult problems where the boundaries between disciplines disappear.<br><br>"
         "I care deeply about the details that turn working code into dependable engineering, namely:<br>"
         "- Clean architecture<br>"
         "- Readable code <br>"
         "- Thoughtful interfaces<br>"
         "- Systems built to last"
    ),

    # Rendered as labeled component groups, not a flat cloud of tags.
    "skill_groups": [
        {
            "label": "LANGUAGES",
            "skills": ["C", "Python", "Rust", "LaTEX", "Markdown", "Mermaid"],
        },
        {
            "label": "FIRMWARE",
            "skills": ["ESP32", "STM32", "FreeRTOS", "LittleFS", "Protobuf", "Bare Metal"],
        },
        {
            "label": "COMMUNICATION",
            "skills": ["I2C", "SPI/QSPI", "BLE", "Serial / UART", "USB",  "Protobuf"],
        },
        {
            "label": "HOST / TOOLING",
            "skills": ["PyQt", "GDB", "Logic Analyzers", "Oscilloscope"],
        },
        {
            "label": "PLATFORM",
            "skills": ["Linux", "Windows", "Git", "GDB"],
        },
        {
            "label": "PROTOTYPING",
            "skills": ["Schematic Design", "Board Design", "Soldering", "Board Rework", "3d printing", "Mechanical Design"],
        }
    ],

    "projects": [
        {
            "name": "GINAA (Ginna Is Not An Acrynym)",
            "status": "Active",
            "stack": "Python · PyQt5",
            "description": (
                "Cross-platform desktop application that generates"
                "Random items, dungons, NPCs and quests for running TTRPGs."
            ),
            "link": "https://github.com/zerihemla/ginaa",
        },
        {
            "name": "Balance Robot",
            "status": "Shelved",
            "stack": "C · FreeRTOS · Rpi Zero",
            "description": (
                "2 wheeled robot. Reads from IMU and moves motors "
                "in order to stay upright and maintain control.<br>"
                "Designed to exersize my control systems knowledge."
            ),
            "link": "https://github.com/zerihemla/balance_robot",
        },
        {
            "name": "Project Three",
            "status": "Complete",
            "stack": "Add your stack",
            "description": "Swap this out for your next project.",
            "link": "",
        },
    ],

    "experience": [
        {
            "role": "Firmware Engineer",
            "org": "Octavian Solutions",
            "period": "April 2025 — Present",
            "summary": "Architected FreeRTOS firmware Project<br>"
            "Architected/Implimented communication protocol with Protobuf<br>"
            "Architected/Implimented computer interface application (PyQt6)<br>"
            "Designed a full BLE interface including SIG/custom characteristics<br>",
        },
        {
            "role": "Lead Firmware Engineer",
            "org": "Advanced Conceptions/Co-Dx",
            "period": "April 2021 - April 2025",
            "summary": "Architected FreeRTOS firmware Proejct<br>"
            "Manged two other firmware engineers<br>"
            "Designed a pyQt5 computer application to interface with firmware<br>"
            "Implimented encryption for communication and firmware binaries<br>"
            "Implimented an abstraction layer for firmware to work across multiple boards<br>",
        },
        {
            "role": "Embedded Systems Engineer",
            "org": "Eclipse Design Innovations",
            "period": "April 2019 - April 2021",
            "summary": "Designed PCBs in KiCad<br>"
            "Coded Firmware for embedded systems<br>"
            "Oversaw 2 other Engineers<br>"
            "Published technical Documentation using LaTEX<br>",
        },
        {
            "role": "Electrical Engineer Intern",
            "org": "Monnit",
            "period": "May 2018 - March 2019",
            "summary": "Designed PCBs with KiCad<br>"
            "Coded Firmware for embedded sensors<br>"
            "Built Prototypes of embedded sensors<br>"
            "Processed RMA to decern reason of failure<br>",
        },
        
    ],

    "education": [
        {
            "School": "Weber State University",
            "Degree": "M.S. of Computer Engineering",
            "Year": "Fall 2018 to April 2021",
            "GPI": "3.88",
        },
        {
            "School": "Weber State University",
            "Degree": "B.S. of Computer Engineering",
            "Year": "Fall 2015 to December 2018",
            "GPI": "3.66",
        },
        {
            "School": "Lewis-Clark State College",
            "Degree": "Pre=Engineering",
            "Year": "Fall 2011 to Spring 2021",
            "GPI": "3.95",
        },
    ],

    "school_projects":[
        {
            "Name": "Custom Quadcopter",
            "Purpose": "Senior Project",
            "Description": "",
        },
        {
            "Name": "Fall Detection System",
            "Purpose": "Master's Project",
            "Description": "",
        },
    ],


    "interests": [
        {
            "Grouping": "Physical",
            "Activities": "Running, Weight Lifting"
        },
        {
            "Grouping": "Making",
            "Activities": "Wood Working, Cooking, Sourdough, 3d printing",
        },
        {
            "Grouping": "Musical",
            "Activities": "Singing, Ukelele, Guitar, Trumpet"
        }
],
}
