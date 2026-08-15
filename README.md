# PlantVillage Dataset Directory Structure

This directory is intended to house the **PlantVillage dataset** for model training with `train.py`.

## Dataset Overview
The PlantVillage dataset contains 54,303 healthy and diseased plant leaf images categorized across 38 class folders.

### Downloading the Dataset:
1. Download from Kaggle or official repository:
   - [PlantVillage Dataset on Kaggle](https://www.kaggle.com/datasets/emmarex/plantdisease)
2. Extract the downloaded zip file into this `dataset/` directory.
3. Your directory structure should look like this:
   ```
   dataset/
   ├── Apple___Apple_scab/
   ├── Apple___Black_rot/
   ├── Apple___Cedar_apple_rust/
   ├── Apple___healthy/
   ├── Corn_(maize)___Common_rust_/
   ├── Potato___Early_blight/
   ├── Potato___Late_blight/
   ├── Tomato___Early_blight/
   ├── Tomato___healthy/
   └── ... (38 class folders total)
   ```
4. Run `python train.py` to initiate model training.
