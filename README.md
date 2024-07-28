# N-Tester

This Python script performs a network speed test, measuring download and upload speeds, as well as ping latency.

## Features

- **Speed Testing**: Measures download and upload speeds in Mbps.
- **Ping Measurement**: Reports the network latency in milliseconds.
- **Continuous Testing**: Repeats the test every 15 seconds, with an option to stop the test with a keyboard interrupt.

## Requirements

- Python 3.x
- `speedtest-cli` library
- `tqdm` library
- `colorama` library

## Installation

You can install the required libraries using pip:

`pip install speedtest-cli tqdm colorama`


To use the N-Tester script, you need to install the required libraries. Follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/n-tester.git
   cd n-tester

# Usage

To run the N-Tester script, follow these steps:

1. Navigate to the directory containing the script:

   ```bash
   cd n-tester

2. Run the script:

`python n-tester.py`


# Example Output

When you run N-Tester, you should see an output similar to the following:

```plaintext
_____   __              ________           _____
___  | / /              ___  __/_____________  /_____________
__   |/ /  ________     __  /  _  _ \_  ___/  __/  _ \_  ___/
_  /|  /   _/_____/     _  /   /  __/(__  )/ /_ /  __/  /
/_/ |_/                 /_/    \___//____/ \__/ \___//_/

                 >>Made by Cipher Haven<<

Testing download speed...
Download Speed: 45.67 Mbps
Upload Speed: 12.34 Mbps
Ping: 23 ms
----------------------------------------
