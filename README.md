# Field-Road Trajectory Dataset

## Description

This repository provides the manually labeled GNSS trajectory datasets of agricultural machinery used for the field-road classification task described in the associated publication. It contains a paddy dataset and a wheat dataset, together with the pre-trained division models and a lightweight script used to reproduce the field/road split.

## Dataset Information

All trajectory data were collected from the Precision Agriculture Application Project Data Service Platform (Wu et al., 2023), where trajectories were recorded by GNSS devices installed on agricultural machines operating in China. Each trajectory record consists of five fundamental attributes:

| Attribute | Description |
|---|---|
| timestamp | Time at which the GNSS point was recorded |
| longitude | Longitude coordinate of the machine |
| latitude | Latitude coordinate of the machine |
| speed | Instantaneous speed of the machine |
| direction | Heading direction of the machine |

Two manually labeled datasets are included, both of which have been widely used in previous field-road segmentation studies:

- **Paddy dataset** (`paddy_0/` – `paddy_4/`) — 100 trajectories collected from 91 paddy harvesters between October and November 2021, totaling 126,602 trajectory points. Sampling frequency is approximately one point every 30 seconds, with a field-to-road point ratio of 1.4:1.
- **Wheat dataset** (`wheat1_0.zip` – `wheat1_4.zip`) — 150 trajectories collected from 65 wheat harvesters between June and July 2021, totaling 574,198 trajectory points. Sampling interval is approximately 5 seconds per point, with a field-to-road point ratio of 3.97:1.

Both datasets are split into 5 parts for storage convenience.

## Code Information

- `data_spilt/split_read.py` — Utility script used to load and divide the raw trajectory data using the pre-trained division model (`.pkl`) corresponding to each dataset.
- `data_spilt/paddy_data_split.pkl` — Pre-trained division model for the paddy dataset.
- `data_spilt/wheat_1_data_split.pkl` — Pre-trained division model for the wheat dataset.
- `data_spilt/__init__.py` — Package initialization file.

The core field-road classification and modeling code (including the feature-extraction and classification methods described in the manuscript, e.g. DBSCAN+Rules, DT, DBSCAN+OD+DBI, GCN) is **not hosted in this repository**. It is provided as a Supplemental File with the published manuscript.

## Usage Instructions

1. Unzip the wheat archives (`wheat1_0.zip` – `wheat1_4.zip`). The paddy data is already provided as unzipped folders (`paddy_0/` – `paddy_4/`).
2. In `data_spilt/split_read.py`, set `files_path` to the local path where the unzipped raw trajectory files are stored, and set `path` to the matching `.pkl` file (`paddy_data_split.pkl` or `wheat_1_data_split.pkl`).
3. Run `data_spilt/split_read.py` to reproduce the field/road split for that dataset.
4. For downstream feature extraction and classification, refer to the code provided in the manuscript's Supplemental Files.

## Requirements

- Python 3.x
- No third-party packages are required — `split_read.py` only uses the Python standard library (`pickle`, `os`, `shutil`).

## Methodology

The datasets support the field-road classification task described in the manuscript (see Section 2.1 "Datasets" for full details on data collection, cleaning, and preprocessing).

## Citation

This dataset is derived from raw trajectory data collected by the Precision Agriculture Application Project Data Service Platform. If you use this dataset in your research, please cite **both** of the following:

1. The associated publication that describes this labeled dataset and the field/road classification task: [please add full citation details of your paper]
2. The original data source: Wu, et al. (2023). Precision Agriculture Application Project Data Service Platform. [please add full citation details]

## License

The raw trajectory data underlying this dataset originates from the Precision Agriculture Application Project Data Service Platform and is redistributed here under the terms of that platform's data usage agreement. No additional open-source license is asserted over the raw data itself. [If you have confirmed you hold the rights to apply an open license to this specific labeled subset, replace this section with the chosen license, e.g. CC-BY-4.0 or CC0-1.0.]
