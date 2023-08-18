# BraTS23

# Our team submission to the 2023 Brain Tumor Segmentation Challenge

This repo contains the codes and pretrained weights for the our submission to the 2023 Brain Tumor Segmentation Challenge.

## Inference with command line
If you want to run the model without docker, first, download the models from [here](https://drive.google.com/file/d/1wsxlOdcL0Gjw8k9ZUt4-x-V1EqnOp0SJ/view?usp=share_link). Extract the files and put the models in the `nnUNet_results` that you set up with nnUNet.
Then run the following commands:
```
nnUNetv2_predict -i <INPUT> -o <OUTPUT> -d 13 -c 3d_fullres -f all -tr nnUNetTrainerDiceCELoss_noSmooth
```
