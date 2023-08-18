# BraTS23

# Our team submission to the 2023 Brain Tumor Segmentation Challenge

This repo contains the codes and pretrained weights for the our submission to the 2023 Brain Tumor Segmentation Challenge.

## Using Model
Whit these two option you can test model

### Notebook
You can run test.ipynb for test our model.

### Run code
If you want to run the model, first, download the models from [here](https://drive.google.com/file/d/1wsxlOdcL0Gjw8k9ZUt4-x-V1EqnOp0SJ/view?usp=share_link). Extract the files and put the models in the `nnUNet_results` that you set up with nnUNet.

Then put all four modalities in ./test directory with following format and run fusion.py:

test/

  ├─ t2w.nii.gz
  
  ├─ t1c.nii.gz
  
  ├─ t1n.nii.gz
  
  └─ t2f.nii.gz

Then run the following commands in order:
```
imagestr = <INPUT>
base_dir = './test'
shutil.copy(join(base_dir + "t1n-t1c.nii.gz"), join(imagestr + 'Brain_0000.nii.gz'))
shutil.copy(join(base_dir, "t2f.nii.gz"), join(imagestr + 'Brain_0001.nii.gz'))
shutil.copy(join(base_dir + "t1c-t2w.nii.gz"), join(imagestr + 'Brain_0002.nii.gz'))
shutil.copy(join(base_dir + "t1c-t2f.nii.gz"), join(imagestr + 'Brain_0003.nii.gz'))
nnUNetv2_predict -i <INPUT> -o <OUTPUT> -d 13 -c 3d_fullres -f all -tr nnUNetTrainerDiceCELoss_noSmooth
```
