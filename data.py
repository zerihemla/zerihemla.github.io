"""
Content for the site. Edit this file to update what shows up —
no HTML editing required. build.py imports RESUME from here.

Fields that support rich text (about, project descriptions, experience
summaries) accept basic HTML like <br> — the template renders them
with the `safe` filter so tags work instead of showing as literal text.
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
        "I have worked on the full firmware stack, from architecting real-time systems to writing low-level drivers.<br><br>"
        "My experience spans the full embedded system spectrum — designing PCBs, building prototypes, and creating the tools that make those systems easier to test and understand.<br><br>"
        "I'm drawn to difficult problems where the boundaries between disciplines disappear.<br><br>"
        "I care deeply about the details that turn working code into dependable engineering, namely:<br>"
        "- Clean architecture<br>"
        "- Readable code<br>"
        "- Thoughtful interfaces<br>"
        "- Systems built to last"
    ),

    "skill_groups": [
        {
            "label": "LANGUAGES",
            "skills": ["C", "Python", "Rust", "LaTeX", "Markdown", "Mermaid"],
        },
        {
            "label": "FIRMWARE",
            "skills": ["ESP32", "STM32", "FreeRTOS", "LittleFS", "Bare Metal"],
        },
        {
            "label": "COMMUNICATION",
            "skills": ["I2C", "SPI/QSPI", "BLE", "Serial / UART", "USB", "Protobuf"],
        },
        {
            "label": "HOST / TOOLING",
            "skills": ["PyQt", "GDB", "Logic Analyzers", "Oscilloscope"],
        },
        {
            "label": "PLATFORM",
            "skills": ["Linux", "Windows", "Git"],
        },
        {
            "label": "PROTOTYPING",
            "skills": ["Schematic Design", "Board Design", "Soldering", "Board Rework", "3D Printing", "Mechanical Design"],
        },
    ],

    "projects": [
        {
            "name": "GINAA (Ginna Is Not An Acronym)",
            "status": "Active",
            "stack": "Python · PyQt5",
            "description": (
                "Cross-platform desktop application that generates "
                "random items, dungeons, NPCs, and quests for running TTRPGs."
            ),
            "link": "https://github.com/zerihemla/ginaa",
        },
        {
            "name": "Balance Robot",
            "status": "Shelved",
            "stack": "C · FreeRTOS · Rpi Zero",
            "description": (
                "2-wheeled robot. Reads from IMU and moves motors "
                "in order to stay upright and maintain control.<br>"
                "Designed to exercise my control systems knowledge."
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
            "summary": "Architected FreeRTOS firmware project<br>"
            "Architected/implemented communication protocol with Protobuf<br>"
            "Architected/implemented computer interface application (PyQt6)<br>"
            "Designed a full BLE interface including SIG/custom characteristics<br>",
        },
        {
            "role": "Lead Firmware Engineer",
            "org": "Advanced Conceptions/Co-Dx",
            "period": "April 2021 - April 2025",
            "summary": "Architected FreeRTOS firmware project<br>"
            "Managed two other firmware engineers<br>"
            "Designed a PyQt5 computer application to interface with firmware<br>"
            "Implemented encryption for communication and firmware binaries<br>"
            "Implemented an abstraction layer for firmware to work across multiple boards<br>",
        },
        {
            "role": "Embedded Systems Engineer",
            "org": "Eclipse Design Innovations",
            "period": "April 2019 - April 2021",
            "summary": "Designed PCBs in KiCad<br>"
            "Coded firmware for embedded systems<br>"
            "Oversaw 2 other engineers<br>"
            "Published technical documentation using LaTeX<br>",
        },
        {
            "role": "Electrical Engineer Intern",
            "org": "Monnit",
            "period": "May 2018 - March 2019",
            "summary": "Designed PCBs with KiCad<br>"
            "Coded firmware for embedded sensors<br>"
            "Built prototypes of embedded sensors<br>"
            "Processed RMAs to discern reason of failure<br>",
        },
    ],

    "education": [
        {
            "school": "Weber State University",
            "degree": "M.S. of Computer Engineering",
            "period": "Fall 2018 to April 2021",
            "detail": "3.88 GPA",
        },
        {
            "school": "Weber State University",
            "degree": "B.S. of Computer Engineering",
            "period": "Fall 2015 to December 2018",
            "detail": "3.66 GPA",
        },
        {
            "school": "Lewis-Clark State College",
            "degree": "Pre-Engineering",
            "period": "Fall 2011 to Spring 2012",
            "detail": "3.95 GPA",
        },
    ],

    "school_projects": [
        {
            "name": "Custom Quadcopter",
            "purpose": "Senior Project",
            "description": "Coded a flight controller from scratch.<br>"
            "The purpose of the flight controller was to keep control of the quadcoper when a weight was placed on one arm of the drone.<br>",
        },
        {
            "name": "Fall Detection System",
            "purpose": "Master's Project",
            "description": "Used pressure transducers to calculate the users height.<br>"
            "Created a mesh radio network to filter out pressure changes due to ambient weather.<br>"
            "Used an IMU to detect a fall and calculate the distance fell to determine if help is needed.<br>",
        },
    ],

    "interests": [
        {
            "grouping": "Physical",
            "activities": "Running, Weight Lifting",
        },
        {
            "grouping": "Making",
            "activities": "Woodworking, Cooking, Sourdough, 3D Printing",
        },
        {
            "grouping": "Musical",
            "activities": "Singing, Ukulele, Guitar, Trumpet",
        },
    ],
}
