# 🐍🪜 The Great Snakes and Ladders Experiment: From Game Analysis to AI Tournament Simulation

*A comprehensive data science and AI research project that evolved from analyzing 100,000 basic games to simulating massive AI tournaments with 3.2+ million games, revealing hidden patterns in gameplay and testing rational agent strategies*

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
[![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=flat&logo=plotly&logoColor=white)](https://plotly.com/)
[![Git LFS](https://img.shields.io/badge/git%20lfs-enabled-green.svg)](https://git-lfs.github.io/)

## 📖 Overview

This repository contains a multi-phase computational experiment that evolved from analyzing **100,000 Snakes and Ladders games** across **100 board configurations** to simulating **100,000+ AI tournaments** with **3.2+ million games**. The project explores both the mathematical foundations of the classic board game and advanced AI decision-making in probabilistic environments, featuring rational agent strategies and comprehensive statistical analysis.

### 🔍 What We Discovered

**Phase 1: Game Mathematics Analysis**
- **Biased Randomness**: Our random number generator was systematically biased, favoring lower dice rolls
- **Board Design Dominance**: Board topology matters more than luck—game length varied by **6x** between boards
- **Hidden Geography**: Identified "launch pad" and "danger zones" on the game board
- **Mathematical Patterns**: Both snakes AND ladders increase game complexity and duration

**Phase 2: AI Tournament & Rational Agents**
- **Strategic Agent Performance**: Rational agents using different strategies showed measurable performance differences
- **Tournament Dynamics**: Large-scale tournament simulation revealed emergent patterns in competitive play
- **Behavioral Analysis**: Multi-dimensional analysis of agent decision-making and win rates
- **Statistical Significance**: All findings backed by rigorous statistical analysis across millions of games

## 📁 Repository Structure

```
├── README.md                          # This file
├── analysis.md                        # Complete Medium blog post analysis
├── .gitignore                         # Git ignore patterns
├── .gitattributes                     # Git LFS configuration
├── Data/                              # Datasets (tracked with Git LFS)
│   ├── boards.csv                     # Board configurations (100 boards, ~20KB)
│   ├── game_journeys_turn_level.csv   # Turn-by-turn game logs (2.9M+ records, ~78MB)
│   └── tournament_results.csv         # AI tournament results (3.2M+ games, large file)
├── Analysis/                          # Generated analysis results
│   ├── advancement_probability.csv    # Tournament advancement statistics
│   ├── agent_stage_win_rates.csv      # Win rates by tournament stage
│   ├── behavioral_clustering_pca.csv  # Agent behavior clustering analysis
│   ├── championship_counts.csv        # Championship statistics
│   ├── group_stage_advancement.csv    # Group stage performance
│   ├── head_to_head_win_rates.csv     # Head-to-head matchup analysis
│   ├── match_duration_by_stage.csv    # Game duration by tournament stage
│   ├── strategy_profile_comparison.csv # Strategy effectiveness comparison
│   ├── turn_efficiency_vs_winrate.csv # Efficiency vs success correlation
│   ├── win_efficiency_by_turns.csv    # Win efficiency analysis
│   └── win_rate_volatility.csv        # Performance volatility metrics
├── Notebooks/                         # Jupyter analysis notebooks
│   ├── Game_Analysis.ipynb            # Original EDA and statistical analysis
│   ├── Snakes_And_Ladders_Billion_Simulator.ipynb  # Basic game simulation
│   ├── 100K Tournaments of 3.2 Million Games Simulation.ipynb  # Tournament simulation
│   └── simulation-data-analysis.ipynb # Tournament results analysis
├── modified Agents/                   # AI agent implementations
│   ├── Rational Agents.ipynb          # Rational agent strategies
│   └── Rational_Agents.ipynb - Colab.pdf  # Documentation
└── Src/                               # Python source code
    ├── game_analysis.py               # Original statistical analysis script
    └── snakes_and_ladders_billion_simulator.py     # Basic game simulation engine
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
   pip install pandas numpy matplotlib seaborn plotly scipy statsmodels tqdm jupyter
   ```

### Running the Analysis

**Phase 1: Original Game Analysis**
1. **Start Jupyter**
   ```bash
   jupyter notebook
   ```

2. **Open the original analysis**
   - Navigate to `Notebooks/Game_Analysis.ipynb`
   - Run all cells to reproduce the foundational statistical analysis

**Phase 2: AI Tournament Analysis**
3. **Explore tournament results**
   - Open `Notebooks/simulation-data-analysis.ipynb`
   - Analyze the large-scale tournament data and agent performance

4. **Study rational agents**
   - Open `modified Agents/Rational Agents.ipynb`
   - Examine different AI agent strategies and implementations

**Generate New Data** (optional)
5. **Run basic simulation**
   - Open `Notebooks/Snakes_And_Ladders_Billion_Simulator.ipynb`
   - Generate fresh basic game data

6. **Run tournament simulation**
   - Open `Notebooks/100K Tournaments of 3.2 Million Games Simulation.ipynb`
   - Generate new tournament data (Warning: computationally intensive)

## 📊 Key Findings Summary

### Phase 1: Mathematical Game Analysis

#### 1. **The Dice Were Rigged**
- Roll of 1: **18.6%** (expected: 16.67%)
- Roll of 6: **15.7%** (expected: 16.67%)
- Chi-square statistic: **10,691.93** (p < 0.000001)

#### 2. **Board Design Trumps Luck**
- Fastest board: **13.35 turns** average
- Slowest board: **85.07 turns** average
- ANOVA F-statistic: **220.21** (p < 0.000001)

#### 3. **Hidden Game Geography**
- **Launch Pad Zones** (Positions 1-6): +5.8 squares beyond expected
- **Danger Zones** (Positions 90+): -8.5 squares below expected

#### 4. **Mathematical Model Results**
- Each additional snake: **+1.62 turns**
- Each additional ladder: **+1.62 turns** (counterintuitive!)
- Longer snakes: **+0.65 turns** per unit length
- Longer ladders: **-0.62 turns** per unit length

### Phase 2: AI Tournament & Agent Analysis

#### 5. **Rational Agent Performance**
- Multiple agent strategies tested across 100,000+ tournaments
- Measurable performance differences between rational decision-making approaches
- Behavioral clustering revealed distinct strategic patterns

#### 6. **Tournament Dynamics**
- Large-scale competitive analysis with **3.2+ million games**
- Head-to-head matchup patterns and advancement probabilities
- Stage-specific performance metrics and win rate volatility

#### 7. **Strategic Insights**
- Turn efficiency vs. win rate correlations
- Agent behavior clustering using PCA analysis
- Championship probability distributions

## 🔬 Technical Details

### Phase 1: Game Mathematics
**Data Generation Parameters**
- **Boards**: 100 unique configurations
- **Games per board**: 1,000
- **Total games**: 100,000
- **Total turns recorded**: 2,979,201
- **Max snakes per board**: 10
- **Max ladders per board**: 10

### Phase 2: AI Tournament Simulation
**Tournament Parameters**
- **Tournaments simulated**: 100,000+
- **Total games**: 3.2+ million
- **AI agents**: Multiple rational strategy implementations
- **Dataset size**: Large tournament results file
- **Analysis dimensions**: 11 comprehensive analysis datasets

### Analysis Techniques Used
- **Descriptive Statistics**: Mean, median, distributions
- **Statistical Testing**: Chi-square, ANOVA, t-tests
- **Regression Analysis**: Multiple linear regression (OLS)
- **Data Visualization**: Static (matplotlib/seaborn) and interactive (plotly)
- **3D Visualization**: Interactive board topology analysis
- **Machine Learning**: PCA for behavioral clustering
- **Tournament Analysis**: Head-to-head performance, advancement probabilities
- **Agent Evaluation**: Strategy comparison and efficiency metrics

## 📈 Visualizations

The analysis includes comprehensive visualizations across multiple phases:

**Phase 1: Game Mathematics**
- **Distribution plots** of dice rolls and game durations
- **Heatmaps** of position transitions
- **Scatter plots** showing board features vs. game length
- **3D interactive plots** of snake and ladder positions
- **Statistical regression** plots and residual analysis

**Phase 2: Tournament & Agent Analysis**
- **Tournament progression** charts and stage analysis
- **Agent performance** comparisons and win rate distributions
- **Behavioral clustering** visualizations using PCA
- **Head-to-head matchup** heatmaps and performance matrices
- **Strategy efficiency** plots and correlation analysis
- **Advancement probability** distributions and championship paths

## 🛠️ File Descriptions

### Data Files (Git LFS)
- **`boards.csv`** (~20KB): 100 board configurations with JSON-encoded snake and ladder positions
- **`game_journeys_turn_level.csv`** (~78MB): Turn-by-turn logs of every move in every game from Phase 1
- **`tournament_results.csv`** (Large file): Complete tournament results with 3.2+ million game records

### Analysis Files
- **`advancement_probability.csv`**: Tournament advancement statistics by agent and stage
- **`agent_stage_win_rates.csv`**: Win rate analysis broken down by tournament stage
- **`behavioral_clustering_pca.csv`**: PCA analysis of agent behavioral patterns
- **`championship_counts.csv`**: Championship statistics and winner distributions
- **`head_to_head_win_rates.csv`**: Detailed head-to-head matchup performance
- **`win_efficiency_by_turns.csv`**: Analysis of turn efficiency vs. success rates

### Code Files
- **`snakes_and_ladders_billion_simulator.py`**: Basic game simulation engine
- **`game_analysis.py`**: Original statistical analysis and visualization code

### Notebooks
- **`Game_Analysis.ipynb`**: Original comprehensive EDA and statistical analysis
- **`Snakes_And_Ladders_Billion_Simulator.ipynb`**: Basic game simulation notebook
- **`100K Tournaments of 3.2 Million Games Simulation.ipynb`**: Large-scale tournament simulation
- **`simulation-data-analysis.ipynb`**: Tournament results analysis and visualization
- **`Rational Agents.ipynb`**: AI agent strategy implementations and testing

### Documentation
- **`analysis.md`**: Complete Medium-style blog post with Phase 1 findings and insights
- **`README.md`**: This file - comprehensive project overview and setup instructions

## 🔄 Reproducing Results

### Phase 1: Original Analysis
To reproduce the exact results from the original game analysis:

1. Use the provided datasets in the `Data/` folder
2. Run `Notebooks/Game_Analysis.ipynb` with the same random seeds
3. All statistical tests and visualizations will regenerate identically

### Phase 2: Tournament Analysis
To reproduce the tournament analysis:

1. Use the large `tournament_results.csv` file (2.3GB)
2. Run `Notebooks/simulation-data-analysis.ipynb`
3. Generated analysis files in the `Analysis/` folder will match

### Generating New Data

**For basic game simulation:**
1. Modify the constants in `Src/snakes_and_ladders_billion_simulator.py`:
   ```python
   N_BOARDS = 100          # Number of board configurations
   GAMES_PER_BOARD = 1000  # Games to simulate per board
   MAX_SNAKES = 10         # Maximum snakes per board
   MAX_LADDERS = 10        # Maximum ladders per board
   ```

**For tournament simulation (computationally intensive):**
1. Open `Notebooks/100K Tournaments of 3.2 Million Games Simulation.ipynb`
2. Adjust tournament parameters as needed
3. Run to generate new tournament datasets (Warning: requires significant compute time and storage)

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
