<div align="center">

# MARGIN

### Biliary & Tumor Segmentation · Multimodal Margin Prediction

**Preoperative CT-Based Prediction of Margin Status along Resection Planes in Perihilar Cholangiocarcinoma**

[Project website](https://sunkai-tsinghua.github.io/MARGIN/) · [Segmentation models](#part-1-nnu-net-biliary-and-tumor-segmentation-models) · [MARGIN training code](#part-2-margin-training-code) · [中文说明](README.zh-CN.md)

**Segmentation weights and inference scripts available · MARGIN training code coming soon**

</div>

## Overview

MARGIN is a research project on CT-based prediction of microscopic margin status in **perihilar cholangiocarcinoma (pCCA)**. The workflow combines CT imaging and anatomical reconstruction to study patient-level margin-status prediction.

**Our open-source release is organized into two distinct parts:**

1. **nnU-Net-based biliary and tumor segmentation models** — trained models for segmenting the biliary tree and primary tumor from preoperative contrast-enhanced CT.
2. **MARGIN training code** — code for training the downstream multimodal framework for patient-level margin-status prediction.

These components address different tasks. The segmentation models generate anatomical masks; MARGIN uses imaging and anatomical information to predict margin status. **MARGIN is not the segmentation network.**

| Component | Task | Release materials | Status |
| --- | --- | --- | --- |
| **Part 1: nnU-Net segmentation models** | Biliary tree and primary tumor segmentation from CT | Best checkpoint, Python / notebook inference, and training curves | **Available** |
| **Part 2: MARGIN training code** | Multimodal learning for patient-level R0 / R1 prediction | Training code and configuration instructions | **Coming soon** |

Download the [segmentation model package](https://github.com/SunKai-Tsinghua/MARGIN/releases/download/segmentation-v1.0.0/MARGIN-segmentation-v1.0.0.zip), then follow the [model details and inference instructions](docs/segmentation-model.md). Executable MARGIN training code remains forthcoming.

## Part 1: nnU-Net biliary and tumor segmentation models

This release focuses on the **customized 3D nnU-Net models used to segment the biliary tree and primary tumor** from preoperative contrast-enhanced CT in patients with pCCA.

- **Model family:** customized 3D nnU-Net.
- **Input:** preoperative contrast-enhanced CT.
- **Segmentation targets:** biliary tree and primary tumor.
- **Training cohort reported in the manuscript:** 197 manually annotated pCCA CT scans.
- **Model:** nnU-Net v2 `ResidualEncoderUNet`, `3d_fullres`, `fold_all/checkpoint_best.pth`.
- **Available:** trained checkpoint, [Python script](segmentation/inference.py), [Notebook](segmentation/inference.ipynb), configuration and training curves.

In the reported study, two senior radiologists reviewed and refined all automated segmentation results before the finalized masks were used for 3D biliary reconstruction. CT images and masks were subsequently resampled to 1 × 1 × 1 mm for downstream feature extraction; this is **not a specification of the segmentation model's training or inference spacing**.

Model configuration, region-based label mapping, environment requirements, and standard nnU-Net inference commands are documented in the model card. The supplied plans independently specify 1 mm isotropic spacing. Inference has not been executed for this release, and no independent segmentation Dice or IoU score is claimed.

See the [segmentation model card](docs/segmentation-model.md). For the upstream framework, see [MIC-DKFZ/nnUNet](https://github.com/MIC-DKFZ/nnUNet).

## Part 2: MARGIN training code

Training code for **MARGIN**, the downstream patient-level margin-status prediction framework, is planned for a future release. The framework uses CT and anatomical information to study R0 / R1 margin status.

**Planned package:** training code, configuration instructions, dependencies, and usage documentation. MARGIN training code, prediction checkpoints, and clinical data are not included in the current release.

See the [MARGIN release overview](docs/margin-training.md).

## Study workflow

![High-level MARGIN workflow](assets/study-workflow.svg)

**Contrast-enhanced CT → segmentation → 3D reconstruction → feature extraction → patient-level margin prediction.**

In this retrospective study, resection planes were reconstructed using surgical records and postoperative CT. The framework has not yet been validated for comparing multiple alternative surgical plans for an individual patient.

## Research findings

The radar chart summarizes **MARGIN** performance in internal and external evaluation cohorts across accuracy, sensitivity, specificity, positive predictive value, negative predictive value, and F1 score.

![MARGIN performance radar chart: internal and external sets](assets/model-performance.png)

These measures describe **patient-level margin-status prediction**, not nnU-Net segmentation performance.

### Paired reader study

In a paired reader study involving five hepatobiliary surgeons, mean accuracy increased from **0.71 to 0.84** and mean sensitivity from **0.20 to 0.62** with MARGIN assistance. Mean specificity remained **0.94**. These values compare unassisted with MARGIN-assisted reader assessment.

## Research scope and availability

This is a research project. The reported study was retrospective, restricted to resected patients, and conducted within one country. Prospective validation remains necessary before clinical deployment. Predictions are intended to support further research into surgical decision support and do not replace specialist assessment.

Patient-level clinical data are not included in this repository. Release licenses and terms for each component will be specified with the corresponding release; the availability of this project page does not itself grant a license to unreleased code or weights.

## Website

This repository also contains a dependency-free, responsive project website in `index.html`, `styles.css`, and `script.js`.

For local preview, run from this directory:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8000` in your browser. See [GitHub Pages deployment instructions](DEPLOY.md) to publish the website.
