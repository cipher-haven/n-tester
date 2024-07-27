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

```bash
pip install speedtest-cli tqdm colorama
