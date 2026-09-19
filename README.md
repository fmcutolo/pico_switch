
## Table of Contents
- [Issues](#issues)
- [Datasheets](#datasheets)
  - [Pico](#pico)
  - [RYLR998 LoRa Module](#rylr998-lora-module)
  - [RTC/EEPROM Module](#rtceeprom-module)
  - [Misc](#misc)


# Issues
9/19/26  

I discovered that the last change in the file pico_switch.pro was not checked in. I can't remember why that change is there and what it does, except that it contains more info and settings. From what I learned online, chatgpt, is that *.pro file does not affect schematic or pcbnew. 
When this change occurred, there was an issue with the allpcb fabricator regarding whole-to-whole spacing which was resolved. I'm not sure if this change related to that, the two files below shows the details of that. I'm including these files here just in case I may need th

[allpcb hole-to-hole spacing issue](images/issues_from_all_pcb.pdf)

[hole-to-hole affected area](images/allpcb_issue.jpg)


# Datasheets

## Pico

| Component | Part Number | Datasheet |
|-----------|-------------|-----------|
| Microcontroller | Pico   | [Pico Datasheet](datasheets/raspberry_pi_picos/pico-datasheet.pdf) |
| Microcontroller | Pico | [python sdk](datasheets/raspberry_pi_picos/RPI-PICO-R3-PUBLIC-SCHEMATIC.pdf) |
| Microcontroller | Pico | [Pico Pinout](datasheets/raspberry_pi_picos/Pico-R3-A4-Pinout.pdf) |
| Microcontroller | Pico2   | [Pico2 Datasheet](datasheets/raspberry_pi_picos/pico-2-datasheet.pdf) |
| Microcontroller | Pico2w   | [Pico2w Datasheet](datasheets/raspberry_pi_picos/pico-2-w-datasheet.pdf) |
| Microcontroller | Pico2w   | [Pico2w Schematic](datasheets/raspberry_pi_picos/pico-2-w-schematic.pdf) |
| Microcontroller | RP2040 | [RP2040 Datasheet](datasheets/raspberry_pi_picos/rp2040-datasheet.pdf) |
| Microcontroller | RP2350 | [RP2350 Datasheet](datasheets/raspberry_pi_picos/rp2350-datasheet.pdf) |
| Microcontroller | PicoX | [python sdk](datasheets/raspberry_pi_picos/raspberry-pi-pico-python-sdk.pdf) |
| Microcontroller | Info   | [Connecting Pico to the internet](datasheets/raspberry_pi_picos/connecting-to-the-internet-with-pico-w.pdf) |
| Microcontroller | Info | [Hardware design with RP2350](datasheets/raspberry_pi_picos/hardware-design-with-rp2350.pdf) |


## RYLR998 LoRa Module
| Component | Part Number | Datasheet |
|-----------|-------------|-----------|
| RF Transceiver | RYLR998    | [RYLR998 datasheet](datasheets/RYLR998/RYLR998.pdf) |
| RF Transceiver | RYLR998 | [RYLR998 AT Commands](datasheets/RYLR998/RYLR998_AT_Commands.pdf) |

## RTC/EEPROM Module
| Component | Part Number | Datasheet |
|-----------|-------------|-----------|
| RTC       | DS3231          | [DS3231 datasheet](datasheets/DS3231_AT24C32_Module/DS3231.pdf) |
| EEPROM    | AT24C32         | [AT24C32](datasheets/DS3231_AT24C32_Module/RYLR998_AT_Commands.pdf) |

## Misc
| Component | Part Number | Datasheet |
|-----------|-------------|-----------|
| TX/RX module       | FT232RL          | [FT232RL datasheet](datasheets/FT232RL_USB_TO_TTL.pdf) |
| Ultrasonic sensor       | HC-SR04 user's manual          | [HC-SR04 Users' Manual](datasheets/HC-SR04_user's_manual.pdf) |
| Voltage regulator       | MCP1700-3302E/TO          | [3.3V Low Dropout (LDO) Voltage](datasheets/MCP1700-Data-Sheet-20001826F.pdf) |
| LED       | Color: RGB  | [Common Anode RGB LED](datasheets/RGB_LED.JPG) |
