# Part 2 — MARGIN training code

**Release status: coming soon** · [Project overview](../README.md) · [Part 1: segmentation models](segmentation-model.md)

## Purpose

This component is the training code for **MARGIN (multimodal adaptive resection guided integration network)**, a downstream framework for patient-level margin-status prediction in perihilar cholangiocarcinoma. It is distinct from the nnU-Net segmentation models released in Part 1.

## Inputs and architecture

| Branch | Input / representation | Method described in the manuscript |
| --- | --- | --- |
| Spatial | Eight anatomical and resection-plane-related features | Features derived from patient-specific 3D biliary models; training-set-fitted min–max scaling |
| Local | Six CT patches: two each from the tumor, tumor–biliary interface, and reconstructed margin regions | 32 × 32 × 32 voxel patches encoded by a shared-weight 3D Mamba backbone |
| Global | A larger CT patch | 112 × 112 × 112 voxel input encoded by Liver-DINO; feature selection restricted to the training set |
| Fusion | Spatial, local, and global representations | Residual multimodal fusion for margin-status prediction |

## Evaluation design

- The development cohort contains 234 patients, partitioned into training and internal validation sets at a 7:3 ratio.
- The independent external test cohort contains 176 patients from a third center.
- All reported prediction metrics are calculated at the patient level.
- Where multiple local patch sets are sampled for one patient, set-level prediction scores are averaged within that patient for evaluation.
- Histopathological assessment of ductal margins is the reference standard, with R1 as the positive class.

## Planned release materials

MARGIN training code and configuration instructions will be provided. The release documentation will identify the actual entry points, dependencies, required feature inputs, training settings, and evaluation procedure.

No runnable training command is provided yet because the released code package and command-line interface have not been verified. Availability of Liver-DINO weights, MARGIN checkpoints, and data will be documented separately; none is implied by this planned training-code release.

## Anatomical input dependency

Part 1 supplies the segmentation component. In the reported study, model-generated masks were reviewed and refined by radiologists, then used to construct 3D biliary models. Resection planes were retrospectively reconstructed from surgical records and postoperative CT. Users should account for this study-specific workflow when interpreting the results.

