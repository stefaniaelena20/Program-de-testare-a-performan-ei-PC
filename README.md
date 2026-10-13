````markdown
# 🖥️ PC Performance Benchmark

A Python desktop application for testing and comparing the performance of a computer’s CPU and memory through a collection of synthetic benchmarks.

The application features a simple graphical interface where you can run individual tests, review their results, and calculate an overall performance score.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)
![Project](https://img.shields.io/badge/Type-Performance%20Benchmark-purple)

## ✨ Features

- 🧠 Displays processor and memory information
- ⚡ Runs CPU, memory access, and memory transfer benchmarks
- 🔢 Tests integer and floating-point calculations
- 🌀 Measures performance with a Mandelbrot calculation
- 📊 Calculates a score based on selected benchmark results
- 🪟 Runs tests in the background to keep the interface responsive
- 🔄 Lets you reset results and run the tests again

## 🧪 Available Tests

| Test | What it measures |
|---|---|
| CPU Information | Processor model, architecture, core count, and frequency |
| Memory Information | Total, available, and used RAM |
| Memory Access | Sequential and random memory access times |
| Memory Transfer | Data copying speed for different block sizes |
| Integer Operations | Integer addition and multiplication performance |
| Floating-Point Operations | Floating-point addition and multiplication performance |
| Mandelbrot Calculation | Time required to calculate a Mandelbrot set sample |

## 🛠️ Built With

- **Python**
- **Tkinter** — graphical user interface
- **psutil** — system and memory information
- **py-cpuinfo** — processor details

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
2. Choose a test from the available buttons.
3. Review the result displayed in the application.
4. Run the required benchmarks and select **Calculate Final Score** to see the combined result.
5. Select **Reset All Tests** to clear the results and start again.

## 📊 About the Score

The final score compares selected benchmark results with reference values built into the application. Results can vary depending on your hardware, Python environment, system load, and other programs running in the background.

## 📁 Project Files

```text
Program-de-testare-a-performan-ei-PC/
├── bunbunssc (1).py
└── ssc_documentatie (2) (1).pdf
```

## 🎓 What I Practiced

- Building a desktop application with Tkinter
- Collecting hardware and memory information
- Measuring execution time for synthetic benchmarks
- Running tasks on background threads
- Presenting benchmark results in a graphical interface

## 👩‍💻 Author

**Czebely Stefania-Elena**
