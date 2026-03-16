# Prediction of on-field rugby scrummaging contact forces from videos using Artificial Neural Networks.

[![DOI](https://zenodo.org/badge/1122439798.svg)](https://doi.org/10.5281/zenodo.18048888)

<p align="center">

## Requirements

- Python version 3.9–3.12.
- Tensorflow version 2.21.0.
- Pandas version 3.0.1 or higher.

---

## Instructions

- **Prepare the input data**. The input data contain the magnitude of the velocity vector of the 2D midpoint between the C7 and the lumbar top-plane locations. The input data do not need to be scaled or length-normalized. An example input data file is provided:
[Example input data](https://github.com/JuanCS96/Rugby_Biomechanics_ANN/blob/main/testData/velTestData.csv)

- **The ANN predict the shoulder contact force in rugby scrummaging**

<br>

See the example [Python code](https://github.com/JuanCS96/Rugby_Biomechanics_ANN/blob/main/rugby_ANN.py) to perform predictions.

If you use this code, please cite the article associated with this study:

- Juan Cordero-Sánchez, Zak Sheehy, Gil Serrancolí, Ezio Preatoni, Grant Trewartha, Dario Cazzola. Prediction of on-field rugby scrummaging contact forces from videos using Artificial Neural Networks
