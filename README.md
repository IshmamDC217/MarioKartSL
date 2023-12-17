![A5E138C8-2D5F-42D8-8EFD-66C9C71D99DF](https://github.com/IshmamDC217/MarioKartSL/assets/89687266/ec970b27-893d-44bb-ba67-d44883978419)
# Mario Kart Start Lights Simulation 🏎️🚦

## Introduction 🌟
This project is inspired by the iconic start sequence in the Mario Kart series, a beloved racing game franchise that has captured the hearts of players since its inception in 1992. Our goal is to recreate the thrilling countdown experience using LEDs controlled by a microcontroller, specifically simulating the sequence as seen in games ranging from the original Super Mario Kart (1992) to Mario Kart 8 Deluxe (2017). The heart of our project lies in the simple yet effective use of GPIO pins on a microcontroller to control LED lights. The setup includes three LEDs (Red, Green, and Amber) and two buttons. When both buttons are pressed simultaneously, we simulate the Mario Kart race start sequence. The Red LED blinks three times like a countdown, and then the Green LED lights up to signal the race start.

### Components 🛠️
- Microcontroller (e.g., Raspberry Pi Pico, Arduino)
- LEDs (Red, Green, Amber)
- Push Buttons (x2)
- Resistors (for LEDs)
- Breadboard and connecting wires

## Script Explanation 📝
The Python script is written for microcontrollers like the Raspberry Pi Pico and utilizes the `machine` library for GPIO pin control.

### Key Functions 🗝️
- `blink(led, count, on_duration, off_duration)`: Blinks the specified LED a certain number of times with defined durations.
- `while True` Loop: Constantly checks the state of the buttons and controls the LEDs accordingly.

### Behavior 🚦
- **Both Buttons Pressed**: Executes the Mario Kart start sequence.
- **Button 1 Pressed**: Activates the Red LED.
- **Button 2 Pressed**: Can be programmed for another action.
- **No Button Pressed**: Turns on the Green LED by default.

## Reflections and Acknowledgements 🌈
Recreating this iconic piece of video game history has been a nostalgic journey, reminding us of the simplicity and joy found in games like Mario Kart. A big thank you to Nintendo for creating such memorable experiences and to the maker community for continually inspiring projects like this.
