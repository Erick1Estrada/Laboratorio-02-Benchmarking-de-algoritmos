# Lab 02 — Algorithm Efficiency and Complexity

**Team members:**
- **Erick Steven Estrada Morales**
- **Nahomy Isabel Cisneros Guamaní**

**Course:** Algorithms  
**University:** Universidad Central del Ecuador  
**Topic:** Benchmarking two algorithms for detecting duplicate numbers  
**Programming language:** Python 3

## Objective

Implement and compare two algorithms that solve the same problem: **find repeated values in a list**. The lab measures execution time and examines how computational work grows as the input size increases.

These approaches differ from the two methods shown in the class presentation (nested loops and a set of previously seen values):

- **Algorithm A — `count()`:** checks how many times each value occurs in the entire list. Expected time complexity: **O(n²)**.
- **Algorithm B — `sorted()` and adjacent elements:** sorts a copy of the list and compares neighboring values. Time complexity: **O(n log n)**.

Both algorithms return the same duplicate values, although the order of the results may differ.

## Repository structure

```text
laboratorio-02-eficiencia-complejidad/
├── README.md
├── laboratorio2_duplicados.py
└── Laboratorio_2_Dos_Tablas.xlsx
```

- **`laboratorio2_duplicados.py`** contains both algorithms, iteration tables, execution-time measurements, and benchmarking tests.
- **`Laboratorio_2_Dos_Tablas.xlsx`** contains a **Benchmark** worksheet with **two separate tables**, one for each algorithm. Each table includes input size, test scenario, estimated work, three execution times, average time, and number of duplicates.

## Requirements

- **Python 3** installed on your computer.
- **Microsoft Excel** or another `.xlsx`-compatible spreadsheet application.
- No external Python packages are required; the script uses only the Python standard library.

Check your Python installation:

```bash
python --version
```

On Windows, if `python` is not recognized, try `py --version`.

## How to run the lab

1. Download or clone this repository.
2. Open a terminal **inside the folder** containing `laboratorio2_duplicados.py`.
3. Run:

   ```bash
   python laboratorio2_duplicados.py
   ```

   On Windows, you may also use:

   ```bash
   py laboratorio2_duplicados.py
   ```

4. Review the **two separate iteration tables** and each algorithm's output in the terminal.
5. The script performs **three timing runs for each test scenario and input size**, using `time.perf_counter()`. Printing and iteration-table generation are excluded from the timed section to keep the comparison fair.

### Input data

The iteration examples use the following list:

```python
[8, 3, 12, 8, 5, 9, 3, 20]
```

Expected duplicate values: **3 and 8**.

For benchmarking, the script tests **five input sizes: 100, 500, 1,000, 2,000, and 5,000**. It tests both **unique-value inputs** and **inputs containing a duplicate**, with **three timing runs per case**. Both algorithms receive identical input data for each comparison.

## Generated CSV files

Running the script creates three CSV files in the working directory:

| File | Description |
|---|---|
| `iteraciones_count.csv` | Detailed iterations for Algorithm A (`count()`). |
| `iteraciones_sorted.csv` | Detailed iterations for Algorithm B (`sorted()`). |
| `benchmark_laboratorio2.csv` | Three execution times, average time, and test results for each input size and scenario. |

These files can be opened in Excel. **You do not need to upload the generated CSV files to GitHub** because the Python script can recreate them.

## How to review and update the Excel workbook

1. Open **`Laboratorio_2_Dos_Tablas.xlsx`**.
2. Select the **Benchmark** worksheet.
3. Review **Table A (`count()`)** at the top and **Table B (`sorted()`)** below it.
4. To enter measurements from your own computer, open **`benchmark_laboratorio2.csv`**. Match each row by algorithm, input size, and test scenario, then copy **Run 1, Run 2, and Run 3** into the corresponding **Time 1, Time 2, and Time 3** columns in the workbook.
5. The workbook's **Average (ms)** column automatically calculates the mean of the three measurements.

**Note:** The Python script **does not automatically update** the `.xlsx` file. Any execution times already provided in the workbook were measured in a different environment. To report results from your own computer, run the script locally and replace those values. The **Operations** column contains theoretical work estimates, **not** an exact count of Python's internal instructions.

## Results and complexity analysis

- **Algorithm A (`count()`)** repeatedly scans the list, leading to approximately quadratic time complexity: **O(n²)**.
- **Algorithm B (`sorted()`)** sorts the list and then performs one pass over neighboring elements. Its time complexity is **O(n log n)**.
- For larger inputs, Algorithm B generally scales better, although measured execution time also depends on hardware, input data, and test conditions.

## Conclusion

Both implementations correctly detect duplicate values using techniques different from those presented in class. Their efficiency should be compared using **measured execution times**, **estimated work**, and **observed scaling as input size increases**.
