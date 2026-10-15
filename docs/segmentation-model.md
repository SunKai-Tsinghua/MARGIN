# Part 1 — nnU-Net biliary and tumor segmentation models

**Release status: coming soon** · [Project overview](../README.md) · [Part 2: MARGIN training](margin-training.md)

## Purpose

This component comprises trained, customized 3D nnU-Net models for automated segmentation of the biliary tree and primary tumor from preoperative contrast-enhanced CT in perihilar cholangiocarcinoma.

## Model information reported in the manuscript

| Field | Description |
| --- | --- |
| Model family | Customized 3D nnU-Net |
| Modality | Preoperative contrast-enhanced CT |
| Population | Patients with perihilar cholangiocarcinoma |
| Targets | Biliary tree and primary tumor |
| Training data | 197 manually annotated pCCA CT scans |
| Role in MARGIN | Anatomical masks for reviewed 3D reconstruction and downstream feature extraction |
| Study review procedure | Automated masks reviewed and refined by two senior radiologists |

The manuscript does not establish whether the release will package the two targets as one multiclass model or separate model checkpoints. Checkpoint structure and numeric label assignments will be specified with the release.

## Planned release materials

- Trained segmentation model weights.
- Compatible nnU-Net version and configuration.
- Environment and hardware requirements.
- CT input, preprocessing, and inference instructions.
- Output label definitions and postprocessing instructions.
- Model license and applicable terms.

## Intended workflow

1. Prepare CT inputs according to the released model's documented requirements.
2. Load the released checkpoint using the corresponding nnU-Net environment.
3. Run inference to obtain biliary and tumor masks.
4. Review segmentation quality before downstream anatomical analysis.

Executable commands will be added after the actual model package is available. The 1 mm isotropic resampling described in the manuscript applies to subsequent feature extraction and must not be treated as an inferred nnU-Net inference requirement.

## Evaluation

Segmentation-specific performance, including any Dice or IoU measurements and evaluation protocols, will need to be documented separately. The MARGIN external-test AUROC of 0.87 evaluates margin-status prediction and does not measure segmentation quality.

## Framework reference

[nnU-Net — official upstream repository](https://github.com/MIC-DKFZ/nnUNet)

The released package must be used with its documented version and settings; installing the latest upstream version alone is not a guarantee of checkpoint compatibility.
