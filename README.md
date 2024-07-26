# Harmonic Drive Telescope Mounts
# A DIY Approach to Precision Astronomical Viewing and Astrophotography
 
 This project, developed by Thomas Van Pelt and Greg Booher, consists of two
 harmonic drive telescope mounts designed for precise astronomical observations. 
 The project showcases both a robust, aluminum-based mount and a more 
 lightweight, entirely 3D-printed variant.


# Overview

  Target Audience: This document is intended for hobbyists, makers, and astronomers 
  interested in building their own high-performance telescope mounts.

# Project Goals:

  Develop affordable, customizable telescope mounts using harmonic drive technology.
  Offer a lightweight and portable 3D-printed option.
  Provide detailed documentation and open-source designs for community use.
  Achieve precise pointing and tracking for astrophotography applications.

# Unique Selling Points:

  Cost-effective: Harmonic drive technology offers high precision at a reasonable 
      cost compared to traditional gear drives.
  Customizable: Modular design allows for adaptations based on telescope weight 
      and user needs.
  Open-source: Hardware and software designs are freely available for modification 
      and improvement.


# Mounts Description

# Mount 1: Aluminum Anodized Mount

  Material: Aluminum (anodized by Greg Booher)
  Motors: 2 NEMA 17 motors with a 27:1 gearbox
  Harmonic Drive: CSF-17-100-2UH-LW with a 100:1 reduction
  Controllers: TMC2209 stepper controllers
  Microcontroller: Teensy 4.0 running OnStep
  Connectivity: Bluetooth and WiFi
  Design Contributions:
    Greg Booher: Machining and Anodizing the aluminum parts
    Thomas Van Pelt: Designing and creating the covers and printed circuit boards

# Mount 2: 3D Printed Mount

  Material: CF-PETG (Carbon Fiber Polyethylene Terephthalate Glycol)
  Motors: 2 NEMA 17 motors with a 30:1 harmonic drive
  Controllers: Same PCB control board as the larger mount
  Connectivity: Bluetooth and WiFi
  Design Contributions: Entirely designed and 3D printed

# Development Timeline

  The project has been under development for over six months and was demonstrated 
  to the Escambia Amateur Astronomy Association in July 2024.

# Future Work
  Thomas Van Pelt plans to further develop the larger mount, integrating it with a 
  custom PCB and software specifically designed for the Raspberry Pi, enhancing the 
  mount's control capabilities and user interface.

# Getting Started

# Prerequisites:

  Teensy 4.0
  TMC2209 stepper controllers
  NEMA 17 motors
  CSF-17-100-2UH-LW harmonic drive for the aluminum mount (or equivalent 100:1 harmonic drive)
  30:1 harmonic drive for the 3D printed mount
  OnStep firmware
  Bluetooth and WiFi modules
  
# Assembly Instructions:

  1. Assemble the aluminum frame.
  2. Install the NEMA 17 motors and the 27:1 gearbox.
  3. Integrate the CSF-17-100-2UH-LW harmonic drive.
  4. Connect the TMC2209 stepper controllers to the Teensy 4.0.
  5. Connect the Bluetooth and WiFi modules to the Teensy 4.0.
  6. Upload OnStep firmware to the Teensy 4.0.
  7. Install the covers and PCBs designed by Thomas.

# Usage:

  1. Power on the system.
  2. Connect the mount to your computer or control device via Bluetooth or WiFi.
  3. Use OnStep software to control the telescope mount. (OnStep download and 
      configuration instructions can be found online)
  4. Adjust settings as necessary for precise astronomical tracking and observation.

# Contribution

  Contributions to further enhance the mounts are welcome. Please fork the 
  repository and submit pull requests.

# License

  This project is licensed under the MIT License.

  For more detailed information, please refer to the documentation in the repository or contact the developers:

  Thomas Van Pelt
  Greg Booher
  
  Happy Stargazing!
