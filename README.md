# 🐍🪜 The Great Snakes and Ladders Experiment

*A comprehensive data science analysis of 100,000 Snakes and Ladders games revealing hidden patterns in seemingly random gameplay*

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Git LFS](https://img.shields.io/badge/git%20lfs-enabled-green.svg)](https://git-lfs.github.io/)

## 📖 Overview

This repository contains a comprehensive computational experiment that simulated **100,000 Snakes and Ladders games** across **100 unique board configurations**, generating nearly **3 million individual dice rolls** to uncover the hidden mathematics behind this classic childhood game.

### 🔍 What We Discovered

- **Biased Randomness**: Our random number generator was systematically biased, favoring lower dice rolls
- **Board Design Dominance**: Board topology matters more than luck—game length varied by **6x** between boards
- **Hidden Geography**: Identified "launch pad" and "danger zones" on the game board
- **Mathematical Patterns**: Both snakes AND ladders increase game complexity and duration
- **Statistical Significance**: All findings backed by rigorous statistical analysis

## 📁 Repository Structure

```
├── README.md                          # This file
├── analysis.md                        # Complete Medium blog post analysis
├── Data/                              # Datasets (tracked with Git LFS)
│   ├── boards.csv                     # Board configurations (100 boards)
│   └── game_journeys_turn_level.csv   # Turn-by-turn game logs (2.9M+ records)
├── Notebooks/                         # Jupyter analysis notebooks
│   ├── Game_Analysis.ipynb            # Comprehensive EDA and statistical analysis
│   └── Snakes_And_Ladders_Billion_Simulator.ipynb  # Game simulation notebook
└── Src/                               # Python source code
    ├── game_analysis.py               # Data analysis script
    └── snakes_and_ladders_billion_simulator.py     # Game simulation engine
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Git with Git LFS enabled
- Jupyter Notebook or JupyterLab

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Snakes And Ladders"
   ```

2. **Install Git LFS** (if not already installed)
   ```bash
   git lfs install
   ```

3. **Pull LFS files**
   ```bash
   git lfs pull
   ```

4. **Install Python dependencies**
   ```bash
   pip install pandas numpy matplotlib seaborn plotly scipy statsmodels tqdm
   ```

### Running the Analysis

1. **Start Jupyter**
   ```bash
   jupyter notebook
   ```

2. **Open the analysis notebook**
   - Navigate to `Notebooks/Game_Analysis.ipynb`
   - Run all cells to reproduce the complete analysis

3. **Generate new data** (optional)
   - Open `Notebooks/Snakes_And_Ladders_Billion_Simulator.ipynb`
   - Adjust parameters in the configuration section
   - Run to generate fresh simulation data

## 📊 Key Findings Summary

### 1. **The Dice Were Rigged**
- Roll of 1: **18.6%** (expected: 16.67%)
- Roll of 6: **15.7%** (expected: 16.67%)
- Chi-square statistic: **10,691.93** (p < 0.000001)

### 2. **Board Design Trumps Luck**
- Fastest board: **13.35 turns** average
- Slowest board: **85.07 turns** average
- ANOVA F-statistic: **220.21** (p < 0.000001)

### 3. **Hidden Game Geography**
- **Launch Pad Zones** (Positions 1-6): +5.8 squares beyond expected
- **Danger Zones** (Positions 90+): -8.5 squares below expected

### 4. **Mathematical Model Results**
- Each additional snake: **+1.62 turns**
- Each additional ladder: **+1.62 turns** (counterintuitive!)
- Longer snakes: **+0.65 turns** per unit length
- Longer ladders: **-0.62 turns** per unit length

## 🔬 Technical Details

### Data Generation Parameters
- **Boards**: 100 unique configurations
- **Games per board**: 1,000
- **Total games**: 100,000
- **Total turns recorded**: 2,979,201
- **Max snakes per board**: 10
- **Max ladders per board**: 10

### Analysis Techniques Used
- **Descriptive Statistics**: Mean, median, distributions
- **Statistical Testing**: Chi-square, ANOVA, t-tests
- **Regression Analysis**: Multiple linear regression (OLS)
- **Data Visualization**: Static (matplotlib/seaborn) and interactive (plotly)
- **3D Visualization**: Interactive board topology analysis

## 📈 Visualizations

The analysis includes:
- **Distribution plots** of dice rolls and game durations
- **Heatmaps** of position transitions
- **Scatter plots** showing board features vs. game length
- **3D interactive plots** of snake and ladder positions
- **Statistical regression** plots and residual analysis

## 🛠️ File Descriptions

### Data Files (Git LFS)
- **`boards.csv`**: Contains 100 board configurations with JSON-encoded snake and ladder positions
- **`game_journeys_turn_level.csv`**: Turn-by-turn logs of every move in every game

### Code Files
- **`snakes_and_ladders_billion_simulator.py`**: Core simulation engine that generates boards and runs games
- **`game_analysis.py`**: Complete statistical analysis and visualization code

### Documentation
- **`analysis.md`**: Complete Medium-style blog post with all findings and insights
- **`README.md`**: This file - project overview and setup instructions

## 🔄 Reproducing Results

To reproduce the exact results from the analysis:

1. Use the provided datasets in the `Data/` folder
2. Run the analysis notebook with the same random seeds
3. All statistical tests and visualizations will regenerate identically

To generate new data with different parameters:

1. Modify the constants in the simulator script:
   ```python
   N_BOARDS = 100          # Number of board configurations
   GAMES_PER_BOARD = 1000  # Games to simulate per board
   MAX_SNAKES = 10         # Maximum snakes per board
   MAX_LADDERS = 10        # Maximum ladders per board
   ```

2. Run the simulation to generate fresh datasets

## 🎯 Future Research Directions

- **Fair Dice Analysis**: How would perfectly unbiased dice change the dynamics?
- **Board Optimization**: What's the optimal board design for specific game lengths?
- **Predictive Modeling**: Can we predict individual game outcomes?
- **Cross-Game Analysis**: How do these insights apply to other board games?

## 📚 Dependencies

### Core Libraries
```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
plotly>=5.0.0
scipy>=1.7.0
statsmodels>=0.12.0
tqdm>=4.60.0
```

### Development Tools
```
jupyter>=1.0.0
git-lfs>=2.13.0
```

## 🤝 Contributing

This is a research project, but contributions are welcome! Areas of interest:

- **Additional statistical analyses**
- **Improved visualizations**
- **Alternative simulation parameters**
- **Cross-validation of findings**
- **Documentation improvements**

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

For questions about the methodology, findings, or code implementation, please open an issue in this repository.

## 🎲 Fun Facts

- If you played one game per minute, it would take **69.4 days** to play 100,000 games
- The dataset contains enough dice rolls to play **496,533 complete games**
- The longest recorded game took **346 turns** to complete
- Position 87 is the most dangerous—it has multiple snakes leading to dramatic setbacks

---

*"Sometimes the most profound discoveries come from the most unexpected places—even a childhood board game can become a window into the deeper patterns that govern our world."*
