# BraTS23

# Our team's submission to the 2023 Brain Tumor Segmentation Challenge

This repo contains the codes and pretrained weights for the our submission to the 2023 Brain Tumor Segmentation Challenge.

## Using Model
Whit these two option you can test model

If you want to run the model, first, download the models from [here](https://drive.google.com/file/d/1wsxlOdcL0Gjw8k9ZUt4-x-V1EqnOp0SJ/view?usp=share_link). Extract the files and put the models in the `<RESULTS>`.

Then put all four modalities in `<INPUT>` directory with following names and format:

<INPUT>/

  ├─ t2w.nii.gz
  
  ├─ t1c.nii.gz
  
  ├─ t1n.nii.gz
  
  └─ t2f.nii.gz

Run the test function from main.py with your directory as inputs:
```test(`<INPUT>`, `<OUTPUT>`, `<RESULTS>`)```

`<INPUT>`: Directory where you put your raw input files in.

`<OUTPUT>`: Directory where you want to output file be saved.

`<RESULTS>`: Directory where you put the model weight([final](https://drive.google.com/file/d/1wsxlOdcL0Gjw8k9ZUt4-x-V1EqnOp0SJ/view?usp=share_link)) in.
