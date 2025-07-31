# Motor Health Pro: Advanced Vibration Analysis and Predictive Maintenance Dashboard

## Abstract

This project presents a comprehensive, real-time vibration analysis and predictive maintenance system designed for industrial motor health monitoring. The system integrates traditional machine learning algorithms with advanced neural network architectures to provide early fault detection, condition monitoring, and predictive maintenance capabilities for critical rotating machinery.

### **Technical Architecture**

The system is built using a modern Python-based web application framework (Streamlit) that provides an interactive dashboard interface for real-time monitoring and analysis. The core architecture employs a multi-layered approach combining:

1. **Data Processing Layer**: Handles vibration data from multiple frequency domains (10Hz, 15Hz, 20Hz, 35Hz, 40Hz, 45Hz, 50Hz) with comprehensive feature engineering including domain-specific vibration metrics such as RMS velocity, peak acceleration, crest factors, and temperature correlations.

2. **Machine Learning Pipeline**: Implements both traditional and advanced anomaly detection algorithms including:
   - **Traditional ML Models**: Isolation Forest, One-Class SVM, Local Outlier Factor, Elliptic Envelope, DBSCAN, and Z-Score analysis
   - **Neural Network Models**: Autoencoder, LSTM Autoencoder, and CNN Autoencoder for temporal pattern recognition
   - **Classification Models**: Random Forest and XGBoost for fault classification
   - **Regression Models**: Temperature prediction and trend analysis

3. **Real-Time Monitoring System**: Features configurable alert thresholds, health status indicators, and automated Telegram notifications for critical events.

### **Key Features and Capabilities**

The dashboard provides five main functional modules:

- **Overview**: Data visualization and statistical summaries with interactive time-series plots
- **Condition Monitoring**: Real-time health status tracking with configurable thresholds and automated alerting
- **Anomaly Detection**: Multi-model comparison framework for detecting operational anomalies
- **Correlation Analysis**: Feature importance analysis and correlation matrices for root cause analysis
- **Settings**: System configuration and parameter optimization

### **Innovative Contributions**

1. **Hybrid ML-NN Approach**: The system uniquely combines traditional statistical methods with deep learning architectures, providing both interpretability and advanced pattern recognition capabilities.

2. **Domain-Specific Feature Engineering**: Implements vibration-specific features including crest factors, RMS ratios, acceleration-velocity relationships, and temperature-vibration interactions.

3. **Real-Time Alert System**: Integrates Telegram messaging for immediate notification of critical conditions, enabling proactive maintenance interventions.

4. **Multi-Frequency Analysis**: Supports analysis across multiple operational frequencies, providing comprehensive coverage of different motor operating conditions.

---

## Installation Guide

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Automation_lab
```

### Step 2: Virtual Environment Setup

#### Option A: Using venv (Recommended)

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

#### Option B: Using conda

```bash
# Create a conda environment
conda create -n vibration_analysis python=3.9

# Activate the conda environment
conda activate vibration_analysis
```

### Step 3: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

**Note**: The installation may take several minutes due to TensorFlow and other large packages.

### Step 4: Verify Installation

```bash
# Check if all packages are installed correctly
python -c "import streamlit, tensorflow, sklearn, plotly; print('All packages installed successfully!')"
```

---

## 📁 Project Structure

```
Automation_lab/
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
├── vibration_dashboard.py             # Main Streamlit dashboard application
├── vibration_analysis.py              # Core analysis functions
├── 50Hz_1hr.csv                       # Sample vibration data
├── 10Hz.csv, 15Hz.csv, 20Hz.csv, etc. # Additional frequency data files
├── venv/                              # Virtual environment directory
└── vibration_dashboard_project/       # Additional project files
```

---

## 🎯 Usage Instructions

### Starting the Dashboard

1. **Activate your virtual environment** (if not already active):
   ```bash
   source venv/bin/activate  # macOS/Linux
   # or
   venv\Scripts\activate     # Windows
   ```

2. **Run the Streamlit dashboard**:
   ```bash
   streamlit run vibration_dashboard.py
   ```

3. **Access the dashboard**: Open your web browser and navigate to `http://localhost:8501`

### Dashboard Navigation

The dashboard consists of five main sections:

#### 1. **Overview**
- Data overview and basic statistics
- Feature distributions and time-series plots
- Quick data exploration tools

#### 2. **Condition Monitoring**
- Real-time health status tracking
- Configurable alert thresholds
- Asset health indicators
- Maintenance scheduling
- Telegram alert integration

#### 3. **Anomalies**
- Multi-model anomaly detection comparison
- Traditional ML vs Neural Network models
- Parameter tuning and optimization
- Anomaly visualization and export

#### 4. **Correlation**
- Feature correlation analysis
- Feature importance ranking
- Statistical summaries
- Data quality assessment

#### 5. **Settings**
- System configuration
- Parameter guides
- Installation requirements
- Performance optimization tips

---

## ⚙️ Configuration

### Telegram Alerts Setup

1. **Create a Telegram Bot**:
   - Message @BotFather on Telegram
   - Create a new bot and get the bot token
   - Get your chat ID by messaging @userinfobot

2. **Configure in Dashboard**:
   - Go to the sidebar in the dashboard
   - Enable "Telegram Alerts"
   - Enter your bot token and chat ID
   - Test the connection

### Data Configuration

- **Update Interval**: Configure data refresh rate (default: 1 minute)
- **Alert Thresholds**: Set custom thresholds for vibration and temperature parameters
- **Model Parameters**: Adjust contamination rates and sequence lengths for anomaly detection

---

## 🔧 Troubleshooting

### Common Issues

1. **TensorFlow Installation Issues**:
   ```bash
   # If TensorFlow fails to install, try:
   pip install tensorflow-cpu
   # or for GPU support:
   pip install tensorflow-gpu
   ```

2. **Port Already in Use**:
   ```bash
   # Use a different port
   streamlit run vibration_dashboard.py --server.port 8502
   ```

3. **Memory Issues**:
   - Reduce the number of models selected in anomaly detection
   - Use smaller sequence lengths for LSTM/CNN models
   - Process data in smaller batches

4. **Package Conflicts**:
   ```bash
   # Recreate virtual environment
   deactivate
   rm -rf venv
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### Performance Optimization

- **For Large Datasets**: Use data sampling or reduce update frequency
- **For Real-time Processing**: Enable GPU acceleration if available
- **For Memory Efficiency**: Close unused browser tabs and restart the application periodically

---

## 📊 Data Format

The system expects CSV files with the following columns:
- `ZaxisRMSVelocity`: Z-axis RMS velocity measurements
- `XaxisRMSVelocity`: X-axis RMS velocity measurements
- `Temperature`: Temperature readings
- `ZaxisPeakacceleration`: Z-axis peak acceleration
- `XaxisPeakacceleration`: X-axis peak acceleration
- `ZPeakvelocity`: Z-axis peak velocity
- `XPeakvelocity`: X-axis peak velocity
- `ZAxisCrestFactor`: Crest factor measurements

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the troubleshooting section above

---

## 🔄 Version History

- **v1.0.0**: Initial release with basic dashboard functionality
- **v1.1.0**: Added neural network models and Telegram integration
- **v1.2.0**: Enhanced real-time monitoring and alert system
- **v1.3.0**: Improved performance and added correlation analysis

---