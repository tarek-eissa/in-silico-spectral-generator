# _In silico_ Spectral Generator

## Description
This repository contains a toolbox for the _in silico_ model described in the paper entitled "**Limits and prospects of molecular fingerprinting for
phenotyping biological systems revealed through in silico modeling**" (https://doi.org/10.1021/acs.analchem.2c04711).

The scripts, along with the provided datasets, allow for convenient applications of the described model to reproduce and extend the results presented in the paper.

The toolbox is fully built using the Python language (version 3.8.8) with custom scripts, supported by commonly-used Python packages.

The spectral_generator.py file contains the _generate_spectra_ function which was used to simulate the different experimental settings.

In addition to the _generate_spectra_ function, four Jupyter Notebooks (.ipynb) are provided to illustrate the use of the generate_spectra function and simulate different experimental designs. As examples of use, the four Jupyter Notebooks simulate results shown and described in the paper.

## Datasets
The "data" folder contains the spectral datasets as CSV files.
* "dataset_1" contains generated spectra based on the experimentally-recorded serum-based FTIR spectra for lung cancer cases, prostate cancer cases, and control individuals. The dataset was split into 20 parts, each in a CSV file, to work around the 100 MB GitHub file limit.
* "dataset_2" contains spectra recorded from water samples using the same FTIR spectrometer which measured the serum spectra.

For more details on how the data was collected and generated, please refer to the paper and the supporting information provided in it.

## Required Python libraries
* numpy (version 1.21.2 used in paper)
* pandas (version 1.2.4 used in paper)
* sklearn (version 0.24.1 used in paper)
* matplotlib (version 3.5.1 used in paper)

## Citation
> to be added.
