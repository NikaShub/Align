# 🧬 DNA-Sequence-Aligner: Optimized Genomic Alignment Engine

A high-performance bioinformatics utility written in Python that computes the optimal alignment between two DNA sequences (represented as alphanumeric strings of A, C, G, and T). By implementing recursive tracking paired with algorithmic **Memoization (Dynamic Programming)**, this engine evaluates massive sequence strings, scales down exponential runtime into polynomial complexity, and returns mathematically perfect similarity scores.

The primary objective of this project was to tackle computational biology challenges, eliminate redundant recursive branches via state-caching, and build a light, robust toolkit for genomic data analysis.

---

## 📊 Scoring Architecture & Heuristics

The engine evaluates alignments dynamically by inserting gaps/spaces to maximize a custom alignment matrix score:
* **Match (+1):** Granted when characters in both sequences match exactly and neither is a gap.
* **Mismatch (-1):** Applied when characters differ and neither is a gap.
* **Gap Penalty (-2):** Incurred whenever a space is introduced in either sequence to adjust the sequence length.

The engine recursively explores all potential placement choices (matching, skipping sequence X, or skipping sequence Y) to find the absolute maximum cumulative score.

---

## ⚡ Engineering & Algorithmic Highlights

### 1. Dynamic Programming via Memoization
* **Exponential to Polynomial Shift:** A standard recursive approach to sequence alignment suffers from severe overlapping sub-problems, leading to a sluggish, exponential $$O(3^N)$$ time complexity. 
* **State Caching Layer:** I engineered an in-memory cache layer utilizing a centralized Python dictionary (`dict`). Before executing any deep recursive call, the engine consults this shared cache. If the sub-problem has been solved previously, the result is returned instantly in near $$O(1)$$ time, resulting in massive execution speedups.

### 2. Space-Efficient Recursion
* Leveraging clean Pythonic argument passing, the single cache object is safely bubbled down through the recursive stack, avoiding object-cloning bottlenecks and ensuring a low memory profile during deep traversals.

---

## 🛠️ Technology Stack & Toolkit
* **Language:** Python 3
* **Concepts:** Dynamic Programming (DP), Memoization, Bioinformatics Algorithms, String Alignment
* **Data Structures:** Hash Maps / Dictionaries, Custom State Tuples

---

## 🚀 Setup and Execution

### Prerequisites
* Python 3.x installed on your machine.

### Installation
1. Clone the repository to your local directory:
   ```bash
   git clone [https://github.com/yourusername/DNA-Sequence-Aligner.git](https://github.com/yourusername/DNA-Sequence-Aligner.git)
   cd DNA-Sequence-Aligner
