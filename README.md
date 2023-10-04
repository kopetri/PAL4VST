# PAL4VST

[Project Page](https://owenzlz.github.io/PAL4VST/) |  [Paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Zhang_Perceptual_Artifacts_Localization_for_Image_Synthesis_Tasks_ICCV_2023_paper.pdf) | [Bibtex](https://scholar.googleusercontent.com/scholar.bib?q=info:SCG89JWD2TYJ:scholar.google.com/&output=citation&scisdr=ClFw-pD-EOWtv4IsW4M:AFWwaeYAAAAAZR0qQ4NG4ZJLvyJzv8fZpndl5xA&scisig=AFWwaeYAAAAAZR0qQ33AJMGShkF_7tLplELgMr8&scisf=4&ct=citation&cd=-1&hl=en)

<!-- <img src="https://github.com/owenzlz/EgoHOS/blob/main/demo/teaser.gif" style="width:800px;"> -->

**Perceptual Artifacts Localization for Image Synthesis Tasks**\
*International Conference on Computer Vision (ICCV), 2023*\
Lingzhi Zhang, Zhengjie Xu, Connelly Barnes, Yuqian Zhou, Qing Liu, He Zhang, Sohrab Amirghodsi, Zhe Lin, Eli Shechtman, Jianbo Shi
<!-- [Lingzhi Zhang*](https://owenzlz.github.io/), [Zhengjie Xu*](https://scholar.google.com/citations?user=kWdwbUYAAAAJ&hl=en), [Simon Stent](https://scholar.google.com/citations?user=f3aij5UAAAAJ&hl=en), [Jianbo Shi](https://www.cis.upenn.edu/~jshi/) (* indicates equal contribution) -->

This paper presents a comprehensive study of Perceptual Artifacts Localization on multiple synthesis tasks. 

## Prerequisites
- Linux
- Python 3
- NVIDIA GPU + CUDA CuDNN

**Table of Contents:**<br>
1. [Quick Usage](#quick_usage) - quick usage with torchscript<br>
2. [Setup](#setup) - download pretrained models and resources
3. [Datasets](#datasets) - download our train/val/test artifacts datasets
4. [Checkpoints](#checkpoints) - download the checkpoints for all our models
5. [Inference](#inference) - inference with models/data
6. [Training](#training) - training scripts

## Quick Usage
- Quick Inference with a Torchscript
```bash
python .. 
```

## Setup
- Clone this repo:
```bash
git clone https://github.com/owenzlz/PAL4VST
```

- Install dependencies:
```bash
conda create --name pal4vst python=3.8 -y
conda activate pal4vst
pip install torch torchvision
pip install -U openmim
mim install mmengine
mim install "mmcv>=2.0.0"
pip install timm==0.6.5
pip install scikit-image
pip install -U openmim && mim install "mmpretrain>=1.0.0rc8"
pip install mmdeploy==1.3.0
cd mmsegmentation
pip install -v -e .
```
For more information, please feel free to refer to MMSegmentation: https://mmsegmentation.readthedocs.io/en/latest/

<a name="datasets"/>

## Datasets
- Download our dataset using the following command line.
```bash
bash download_datasets.sh
```

(Comming soon)

After downloading, the dataset is structured as follows: 
```bash
- [pal4vst dataset root]
    |- train
        |- image
        |- label
        |- contact
    |- val 
        |- image
        |- label
        |- contact
    |- test_indomain
        |- image
        |- label
        |- contact
    |- test_outdomain
        |- image
        |- label
        |- contact
```



<a name="checkpoints"/>

## Checkpoints

(Comming soon)

<a name="inference_on_images"/>

## Inference on Images

- Let's first download a few test images for running the demo:
```bash
bash download_testimages.sh
```

Depending on the application scenarios, you may want to use one of these commands to generate the segmentation predictions. Please modify the image directory paths in the bash file if needed. The backen segmentation model is Swin-L backbone with UPerNet head. 

The default of the bash commands run on the images in "./testimages/images", and the results are saved in "./testimages" folder. If you wish to test on your own images, you may either put your images into "./testimages/images" folder or change directories in the bash files.

- Predict two hands, contact boundary, and interacting objects (1st order) sequentially. 
```bash
cd mmsegmentation # if you are not in this directory
bash pred_all_obj1.sh
```

<img src="https://github.com/owenzlz/EgoHOS/blob/main/demo/twohands_obj1_optimized.gif" style="width:850px;">

- Predict two hands, contact boundary, and interacting objects (1st and 2nd orders) sequentially. 
```bash
cd mmsegmentation # if you are not in this directory
bash pred_all_obj2.sh
```

<img src="https://github.com/owenzlz/EgoHOS/blob/main/demo/twohands_obj2_optimized.gif" style="width:850px;">

If you only want to predict only hand/contact segmentation, or want to use each module separately, see the commands below. 

- Predict only the left and right hands.
```bash
cd mmsegmentation # if you are not in this directory
bash pred_twohands.sh
```

<img src="https://github.com/owenzlz/EgoHOS/blob/main/demo/twohands_optimized.gif" style="width:850px;">

- Predict the dense contact boundary. 
```bash
cd mmsegmentation # if you are not in this directory
bash pred_cb.sh
```

<img src="https://github.com/owenzlz/EgoHOS/blob/main/demo/cb.gif" style="width:850px;">

- Predict the (1st order) interacting objects. 
```bash
cd mmsegmentation # if you are not in this directory
bash pred_obj1.sh
```

- Predict the (both 1st and 2nd orders) interacting objects. 
```bash
cd mmsegmentation
bash pred_obj2.sh
```

<a name="inference_on_videos"/>

## Inference on Videos

- Let's first download a few test videos for running the demo:
```bash
bash download_testvideos.sh
```

- Predict hands and (1st order) interacting objects. 
```bash
cd mmsegmentation # if you are not in this directory
bash pred_obj1_video.sh
```

- Predict hands and (1st and 2nd orders) interacting objects. 
```bash
cd mmsegmentation # if you are not in this directory
bash pred_obj2_video.sh
```

<a name="other_github"/>

## Other Resouces

We used other resources for the application section, i.e. mesh reconstruction. Please refer to below:
1. Image Inpainting - LaMa: [https://github.com/saic-mdal/lama](https://github.com/saic-mdal/lama)
2. Video Inpainting - Flow-edge Guided Video Completion: [https://github.com/vt-vl-lab/FGVC](https://github.com/vt-vl-lab/FGVC)
3. Mesh Reconstruction of Hand-Object Interaction: [https://github.com/hassony2/homan](https://github.com/hassony2/homan)
4. Video Recognition - SlowFast Newtork: [https://github.com/epic-kitchens/epic-kitchens-slowfast](https://github.com/epic-kitchens/epic-kitchens-slowfast)

If you wish to generate higher quality mask, you may consider using mask refinement model, i.e. Cascade PSP: [https://github.com/hkchengrex/CascadePSP](https://github.com/hkchengrex/CascadePSP)

### Citation
If you use this code for your research, please cite our paper:
```
@inproceedings{zhang2022fine,
  title={Fine-Grained Egocentric Hand-Object Segmentation: Dataset, Model, and Applications},
  author={Zhang, Lingzhi and Zhou, Shenghao and Stent, Simon and Shi, Jianbo},
  booktitle={European Conference on Computer Vision},
  pages={127--145},
  year={2022},
  organization={Springer}
}
```



