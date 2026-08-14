"""
Content for the site. Edit this file to update what shows up —
no HTML editing required. build.py imports RESUME from here.
"""

RESUME = {
    "name": "Your Name",
    "title": "Embedded Systems / Firmware Engineer",
    "tagline": "I build the software that runs closest to the metal — "
                "and the tools that talk to it.",
    "location": "Layton, UT",
    "email": "you@example.com",
    "github": "https://github.com/yourusername",
    "linkedin": "https://linkedin.com/in/yourusername",

    "about": (
        "I write firmware for microcontrollers and the desktop software "
        "that pairs with it. Most days that means C on an STM32 target "
        "and Python on the host side, talking to each other over a wire."
    ),

    # Rendered as labeled component groups, not a flat cloud of tags.
    "skill_groups": [
        {
            "label": "FIRMWARE",
            "skills": ["C", "STM32", "FreeRTOS", "CMSIS-RTOSv2", "LittleFS", "Bare Metal"],
        },
        {
            "label": "HOST / TOOLING",
            "skills": ["Python", "PyQt6", "Protobuf (nanopb)", "Serial / UART", "conda"],
        },
        {
            "label": "PLATFORM",
            "skills": ["Linux (Mint)", "Git", "GDB", "Logic Analyzers"],
        },
    ],

    "projects": [
        {
            "name": "Companion Desktop App",
            "status": "Active",
            "stack": "Python · PyQt6 · Protobuf",
            "description": (
                "Cross-platform desktop application that talks to embedded "
                "hardware over serial using a shared protobuf message schema, "
                "for configuration, monitoring, and diagnostics."
            ),
            "link": "",
        },
        {
            "name": "LittleFS Migration",
            "status": "Complete",
            "stack": "C · FreeRTOS · STM32",
            "description": (
                "Migrated firmware storage layer from FatFS to LittleFS, "
                "with wear-leveling and performance tuning for "
                "flash-constrained targets."
            ),
            "link": "",
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
            "org": "Your Company",
            "period": "20XX — Present",
            "summary": "One or two lines on scope and impact, not a task list.",
        },
        {
            "role": "Previous Role",
            "org": "Previous Company",
            "period": "20XX — 20XX",
            "summary": "Same — keep it to the highlight, not the full history.",
        },
    ],
}
