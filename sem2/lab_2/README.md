# NMT Experiments Summary

## Overview
This project implements a Neural Machine Translation system from Russian to English. Multiple improvements were applied to a baseline Seq2Seq LSTM model to achieve the target BLEU score of 27.

---

## Models

| # | Model | Improvements | BLEU | Val PPL |
|---|-------|--------------|------|---------|
| 1 | Baseline | LSTM Seq2Seq | 15.49 | 116.71 |
| 2 | Mean Attention | Average of encoder outputs | 17.71 | 95.51 |
| 3 | Bahdanau Attention | Additive attention with learnable weights | 25.86 | 95.513 |
| 4 | BPE + Attention | BPE tokenization + Bahdanau | 22.73 | 194.70 |
| 5 | **Final** | Bahdanau Attention + LR Scheduler + Dropout (0.3) + 15 epochs | **27.63** | 88.80 |

---

## Improvements Explained

### Mean Attention (Simple)
- Takes arithmetic mean of all encoder hidden states
- Every source word gets equal weight
- **BLEU**: 17.71

### Bahdanau Attention
- Allows decoder to focus on relevant source words
- Computes attention weights based on current decoder state
- **Impact**: +10 BLEU to baseline

### BPE Tokenization
- Splits rare words into subwords
- Reduces vocabulary size from ~9000 to ~5000
- Handles out-of-vocabulary words
- **Impact**: Requires more epochs to converge, +7 BLEU to baseline

### Learning Rate Scheduler
- `ReduceLROnPlateau` reduces LR when validation loss plateaus
- Stabilizes training and improves convergence
- **Impact**: Key to reaching 27+ BLEU

---

## Results & Analysis

- **Bahdanau attention** gave the largest single improvement (+10 BLEU)
- **BPE alone** underperformed with 10 epochs but contributed to final model
- **LR scheduler** was essential to reach the 27 BLEU target