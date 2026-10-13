# 🖥️ PC Performance Benchmark

A Python desktop application for testing a computer’s CPU and memory performance through a collection of synthetic benchmarks.

Run individual tests, view the results, and calculate a combined performance score using a simple graphical interface.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)
![Benchmark](https://img.shields.io/badge/Project-Performance%20Testing-purple)

## ✨ Features

- 🧠 Displays processor and memory information
- ⚡ Tests CPU performance and memory access speed
- 📦 Measures memory transfer performance
- 🔢 Benchmarks integer and floating-point operations
- 🌀 Measures performance with a Mandelbrot calculation
- 📊 Calculates a combined score from selected test results
- 🪟 Runs tests in the background to keep the interface responsive
- 🔄 Allows you to reset results and run the tests again

## 🧪 Available Tests

| Test | Description |
|---|---|
| CPU Information | Displays processor model, architecture, cores, and frequency |
| Memory Information | Shows total, available, and used RAM |
| Memory Access | Compares sequential and random memory access |
| Memory Transfer | Measures data copying speed for different block sizes |
| Integer Operations | Tests integer addition and multiplication |
| Floating-Point Operations | Tests floating-point addition and multiplication |
| Mandelbrot Calculation | Measures the time needed to calculate a Mandelbrot set sample |

## 🛠️ Technologies

- **Python**
- **Tkinter** — graphical user interface
- **psutil** — system and memory information
- **py-cpuinfo** — processor information

## 🚀 Getting Started

### Requirements

- Python 3
- `psutil`
- `py-cpuinfo`

### Installation

Clone the repository:

```bash
git clone https://github.com/stefaniaelena20/Program-de-testare-a-performan-ei-PC.git
cd Program-de-testare-a-performan-ei-PC
```

Install the required packages:

```bash
pip install psutil py-cpuinfo
```

### Run the application

```bash
python "bunbunssc (1).py"
```

## 📖 How to Use

1. Start the application.
2. Select a benchmark from the available test buttons.
3. Review the result displayed in the application.
4. Run the required tests and select **Calculate Final Score**.
5. Select **Reset All Tests** to clear the results and start again.

## 📊 About the Results

The final score compares selected benchmark results with reference values included in the application. Results may vary depending on your computer’s hardware, system load, and other programs running in the background.

## 📁 Project Structure

```text
Program-de-testare-a-performan-ei-PC/
├── bunbunssc (1).py
└── ssc_documentatie (2) (1).pdf
```

## 🎓 What I Learned

- Creating a desktop application with Tkinter
- Collecting hardware and memory information
- Measuring execution time for different operations
- Running tasks on background threads
- Displaying benchmark results in a graphical interface

## 👩‍💻 Author

**Czebely Stefania-Elena**
