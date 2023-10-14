from fusion import *


def percentage(part, whole):
    Percentage = 100 * part / whole
    return str(round(Percentage) + 1) + "%"


def zero_learning_fusion(input_images):
    FU = Fusion(input_images)
    fusion_img = FU.fuse()
    return fusion_img


def normalizer(image):
    img_min = np.min(image)
    img_max = np.max(image)
    image = (image - img_min) / (img_max - img_min)
    image = image * 255
    return image


def fusion(raw_data_path):
    base_dir = raw_data_path

    fusion_modes = ['t1n-t1c', 't1c-t2f', 't1c-t2w']
    images = []
    for i, mode in enumerate(fusion_modes):
        Final_fusion3D = ''
        images = [nib.load(join(base_dir, '{}.nii.gz'.format(mode.split('-')[0]))).get_fdata(),
                  nib.load(join(base_dir, '{}.nii.gz'.format(mode.split('-')[1]))).get_fdata()]
        for slice_num in range(155):
            if (slice_num % 10) == 0:
                print(percentage(155 * i + slice_num + 1, 155 * 3))
            slices = [normalizer(image[:, :, slice_num]) for image in images]
            fusion = zero_learning_fusion(slices)
            if slice_num == 0:
                Final_fusion3D = fusion
            else:
                Final_fusion3D = np.dstack((Final_fusion3D, fusion))

        output = nib.Nifti1Image(Final_fusion3D, np.eye(4))
        output.header.get_xyzt_units()
        output.to_filename(join(base_dir, '{}.nii.gz'.format(mode)))
        print(mode + ': Done')


def test(raw_data_path, output_path, results_path):

    os.environ["nnUNet_raw"] = join('.')
    os.environ["nnUNet_preprocessed"] = join('.')
    os.environ["nnUNet_results"] = results_path

    fusion(raw_data_path)
    imagestr = join('.', 'input')

    try:
        os.mkdir(imagestr)
    except:
        pass

    shutil.copy(join(raw_data_path, "t1n-t1c.nii.gz"), join(imagestr, 'Brain_0000.nii.gz'))
    shutil.copy(join(raw_data_path, "t2f.nii.gz"), join(imagestr, 'Brain_0001.nii.gz'))
    shutil.copy(join(raw_data_path, "t1c-t2w.nii.gz"), join(imagestr, 'Brain_0002.nii.gz'))
    shutil.copy(join(raw_data_path, "t1c-t2f.nii.gz"), join(imagestr, 'Brain_0003.nii.gz'))

    inp = join('.', 'input')
    out = join(output_path)

    os.system(
        'nnUNetv2_predict -i {} -o {} -d 13 -c 3d_fullres -f all -tr nnUNetTrainerDiceCELoss_noSmooth'.format(inp, out))
