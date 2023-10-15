# BraTS23

# Our team's submission to the 2023 Brain Tumor Segmentation Challenge

This repo contains the codes and pretrained weights for the our submission to the 2023 Brain Tumor Segmentation Challenge.

## Running our model
If you want to run the model, first, download the models from [here](https://drive.google.com/file/d/1wsxlOdcL0Gjw8k9ZUt4-x-V1EqnOp0SJ/view?usp=share_link). Ensure that the models are kept in the **final** directory after extracting the file.

Then put all four modalities in `<INPUT>` directory with following names and format:

`<INPUT>`/

  ├─ t2w.nii.gz
  
  ├─ t1c.nii.gz
  
  ├─ t1n.nii.gz
  
  └─ t2f.nii.gz



#### With these two option you can test model:

### Notebook
You only need to run **test.ipynb**

### Python file

Using your own directory paths, run the **test** function in main.py:

```test(<INPUT>, <OUTPUT>, <RESULTS>)```

`<INPUT>`: This is the directory where you put your raw input files.

`<OUTPUT>`: This is the directory where you want to save the result.

`<RESULTS>`: This is the directory where you placed the model weight([final](https://drive.google.com/file/d/1wsxlOdcL0Gjw8k9ZUt4-x-V1EqnOp0SJ/view?usp=share_link)).
