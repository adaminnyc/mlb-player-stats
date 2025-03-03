# MLB Player Daily Statistics

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A web application that allows users to retrieve MLB player statistics for a specific date using pybaseball and Gradio.

![Screenshot](screenshot.png)

## Features

- Search for any MLB player by name
- Retrieve player statistics for a specific date
- View detailed statistics including pitch information, hit data, and more
- Support for both batters and pitchers
- Easy-to-use web interface

## Installation

### Option 1: Using the installation script (Recommended)

On macOS or Linux:
```bash
chmod +x install.sh
./install.sh
```

### Option 2: Manual installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/mlb-player-stats.git
   cd mlb-player-stats
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

   If you encounter issues, try installing with setup.py:
   ```bash
   pip install -e .
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to the URL displayed in the terminal (typically http://127.0.0.1:7860)

3. Enter a player's full name (first and last) and a date in YYYY-MM-DD format

4. Click "Get Statistics" to view the player's statistics for that day

## Example

- Player Name: Mike Trout
- Date: 2023-07-15

## Troubleshooting

If you encounter installation issues:

1. Try using a different Python version (3.8, 3.9, 3.10, or 3.11)
2. Install packages one by one to identify which one is causing problems
3. Use conda instead of pip:
   ```bash
   conda create -n mlb-stats python=3.10
   conda activate mlb-stats
   conda install -c conda-forge gradio pybaseball pandas numpy matplotlib
   ```

## Notes

- The application requires an internet connection to fetch data from MLB's Statcast database
- If no statistics are found for a player on a specific date, it could mean:
  - The player did not play that day
  - The player played but no Statcast data was recorded
  - The date format is incorrect (use YYYY-MM-DD)
  - The player name is misspelled or not found in the database

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 