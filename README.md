# Real Time Data Harvester

## Description

This repository is dedicated to a powerful market scanning tool designed to identify arbitrage opportunities across multiple exchanges. By analyzing real-time price data, the scanner effectively pinpoints discrepancies and potential profit points in the market.

## Table of Contents

- [Objective](#objective)
- [Background](#background)
- [Installation](#installation)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Setup](#setup)
  - [API](#api)
  - [Running the Scanner](#running-the-scanner)
- [Architecture](#architecture)
- [Security](#security)
- [Contributing](#contributing)
- [Contact](#contact)

## Objective

The primary goal of the Real-Time Data Harvester is to efficiently collect and deliver critical, real-time market data across multiple cryptocurrency exchanges. This tool focuses on capturing the current prices of selected currencies, enabling swift and accurate access to essential market information. The purpose of this continuous data collection is to empower automated arbitrage systems by providing them with the timely insights necessary to identify arbitrage opportunities effectively. The harvested data is made accessible via a dedicated API, tailored to support the needs of automated trading strategies and ensure that these systems can react to market changes with the precision required for successful arbitrage operations.

## Background

The Real-Time Data Harvester is specifically designed to meet these critical needs by focusing on the high-speed collection of relevant financial data across multiple cryptocurrency exchanges. By integrating real-time data processing and network communication, this tool ensures that traders have the most current information at their fingertips.

## Installation

Follow these steps to set up the Real Time Data Harvester:

1. Clone the repository:

```bash
git clone git@github.com:Project0rigin/real_time_data_harvester.git
```

2. Navigate to the project directory:

```bash
cd real_time_data_harvester
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Configuration

Edit the [Config](./src/config.py) file to set up your personal configurations as per your trading preferences.

### Setup

For detailed information about the Setup of the Real Time Data Harvester, please refer to the [Setup Documentation](./docs/setup.md)

### API

For detailed information about the API usage of the Real Time Data Harvester, please refer to the [API Documentation](./docs/api.md)

### Running the Scanner

To start the scanner, run the following command from the root of the project:

```bash
python main.py
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Architecture

For detailed information about the architectural design and the components of the Real Time Data Harvester, please refer to the [Architecture Documentation](./docs/architecture.md)

## Security

For detailed information about the Security of the Real Time Data Harvester, please refer to the [Security Documentation](./docs/security.md)

## Contributing

Contributions are welcome. For major changes, please open an issue first to discuss your suggestions or improvements.

## Contact

GitHub: [LourensGH](https://github.com/LourensGH)
Email: [lourenskok@gmail.com](mailto:lourenskok@gmail.com)
