#!/usr/bin/env python3
"""Standard nnU-Net v2 inference for the MARGIN segmentation release.

Example (run from the repository root):
    python segmentation/inference.py --model-dir /path/to/model \
        --input-dir /path/to/imagesTs --output-dir /path/to/predictions
"""
import argparse
import os
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model-dir', required=True, type=Path,
                        help='Directory containing dataset.json, plans.json and fold_all/')
    parser.add_argument('--input-dir', required=True, type=Path,
                        help='Single-channel CT files named CASE_0000.nii.gz')
    parser.add_argument('--output-dir', required=True, type=Path,
                        help='Directory for output CASE.nii.gz masks')
    parser.add_argument('--device', choices=('cuda', 'cpu'), default='cuda')
    parser.add_argument('--disable-tta', action='store_true', help='Disable mirroring test-time augmentation')
    parser.add_argument('--save-probabilities', action='store_true')
    parser.add_argument('--continue-prediction', action='store_true', help='Skip existing predictions')
    parser.add_argument('--num-processes', type=int, default=1,
                        help='Workers for preprocessing and segmentation export')
    args = parser.parse_args()
    args.model_dir = args.model_dir.expanduser().resolve()
    args.input_dir = args.input_dir.expanduser().resolve()
    args.output_dir = args.output_dir.expanduser().resolve()
    for filename in ('plans.json', 'dataset.json', 'fold_all/checkpoint_best.pth'):
        if not (args.model_dir / filename).is_file():
            parser.error(f'Missing model file: {args.model_dir / filename}')
    if not args.input_dir.is_dir() or not list(args.input_dir.glob('*_0000.nii.gz')):
        parser.error('Input directory must contain CT files named CASE_0000.nii.gz.')
    if args.output_dir == args.input_dir or args.output_dir == args.model_dir:
        parser.error('Use a separate output directory.')
    if args.num_processes < 1:
        parser.error('--num-processes must be positive.')

    # Compilation is optional in nnU-Net; disable it for a portable inference entry point.
    os.environ['nnUNet_compile'] = 'false'
    import torch
    from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor

    if args.device == 'cuda' and not torch.cuda.is_available():
        parser.error('CUDA is unavailable. Use --device cpu, or a CUDA-enabled PyTorch environment.')
    predictor = nnUNetPredictor(
        tile_step_size=0.5,
        use_gaussian=True,
        use_mirroring=not args.disable_tta,
        perform_everything_on_device=args.device == 'cuda',
        device=torch.device(args.device),
        verbose=False,
        verbose_preprocessing=False,
        allow_tqdm=True,
    )
    # nnU-Net automatic fold discovery excludes fold_all, so specify it explicitly.
    predictor.initialize_from_trained_model_folder(
        str(args.model_dir),
        use_folds=('all',),
        checkpoint_name='checkpoint_best.pth',
    )
    predictor.predict_from_files(
        str(args.input_dir),
        str(args.output_dir),
        save_probabilities=args.save_probabilities,
        overwrite=not args.continue_prediction,
        num_processes_preprocessing=args.num_processes,
        num_processes_segmentation_export=args.num_processes,
        folder_with_segs_from_prev_stage=None,
        num_parts=1,
        part_id=0,
    )


if __name__ == '__main__':
    main()
