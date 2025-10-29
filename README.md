# Fetal segmentation weights for nnUnetV2
This repository contains open-source segmentation weights for nnUnetV2, used for segmenting the body and brain from 3D-FIESTA sequences of fetal MRI.
These segmentation weights are being applied to an SCI paper, which is currently under submission.
nnUnet link: https://github.com/MIC-DKFZ/nnUNet.

My nnUnet virtual environment dependency list is as follows:
packages in environment at nnunet:

Name                           Version          Build            Channel
acvl-utils                       0.2.5            pypi_0           pypi
argparse                         1.4.0            pypi_0           pypi
batchgenerators                  0.25.1           pypi_0           pypi
batchgeneratorsv2                0.3.0            pypi_0           pypi
blosc2                           3.6.1            pypi_0           pypi
bzip2                            1.0.8            h2bbff1b_6
ca-certificates                  2025.2.25        haa95532_0
certifi                          2025.7.14        pypi_0           pypi
charset-normalizer               3.4.2            pypi_0           pypi
colorama                         0.4.6            pypi_0           pypi
connected-components-3d          3.24.0           pypi_0           pypi
contourpy                        1.3.3            pypi_0           pypi
cycler                           0.12.1           pypi_0           pypi
dynamic-network-architectures    0.4.2            pypi_0           pypi
einops                           0.8.1            pypi_0           pypi
expat                            2.7.1            h8ddb27b_0
fft-conv-pytorch                 1.2.0            pypi_0           pypi
filelock                         3.13.1           pypi_0           pypi
fonttools                        4.59.0           pypi_0           pypi
fsspec                           2024.6.1         pypi_0           pypi
future                           1.0.0            pypi_0           pypi
graphviz                         0.21             pypi_0           pypi
huggingface-hub                  0.34.1           pypi_0           pypi
idna                             3.10             pypi_0           pypi
imagecodecs                      2025.3.30        pypi_0           pypi
imageio                          2.37.0           pypi_0           pypi
jinja2                           3.1.4            pypi_0           pypi
joblib                           1.5.1            pypi_0           pypi
kiwisolver                       1.4.8            pypi_0           pypi
lazy-loader                      0.4              pypi_0           pypi
libffi                           3.4.4            hd77b12b_1
linecache2                       1.0.0            pypi_0           pypi
markupsafe                       2.1.5            pypi_0           pypi
matplotlib                       3.10.3           pypi_0           pypi
mpmath                           1.3.0            pypi_0           pypi
msgpack                          1.1.1            pypi_0           pypi
ndindex                          1.10.0           pypi_0           pypi
networkx                         3.3              pypi_0           pypi
nnunetv2                         2.6.2            pypi_0           pypi
numexpr                          2.11.0           pypi_0           pypi
numpy                            2.1.2            pypi_0           pypi
openssl                          3.0.17           h35632f6_0
packaging                        25.0             pypi_0           pypi
pandas                           2.3.1            pypi_0           pypi
pillow                           11.0.0           pypi_0           pypi
pip                              25.1             pyhc872135_2
platformdirs                     4.3.8            pypi_0           pypi
py-cpuinfo                       9.0.0            pypi_0           pypi
pyparsing                        3.2.3            pypi_0           pypi
python                           3.12.11          h716150d_0
python-dateutil                  2.9.0.post0      pypi_0           pypi
pytz                             2025.2           pypi_0           pypi
pyyaml                           6.0.2            pypi_0           pypi
requests                         2.32.4           pypi_0           pypi
safetensors                      0.5.3            pypi_0           pypi
scikit-image                     0.25.2           pypi_0           pypi
scikit-learn                     1.7.1            pypi_0           pypi
scipy                            1.16.0           pypi_0           pypi
seaborn                          0.13.2           pypi_0           pypi
setuptools                       78.1.1           py312haa95532_0
six                              1.17.0           pypi_0           pypi
sqlite                           3.50.2           hda9a48d_1
sympy                            1.13.3           pypi_0           pypi
threadpoolctl                    3.6.0            pypi_0           pypi
tifffile                         2025.6.11        pypi_0           pypi
timm                             1.0.19           pypi_0           pypi
tk                               8.6.14           h5e9d12e_1
torch                            2.7.1+cu128      pypi_0           pypi
torchaudio                       2.7.1+cu128      pypi_0           pypi
torchvision                      0.22.1+cu128     pypi_0           pypi
tqdm                             4.67.1           pypi_0           pypi
traceback2                       1.4.0            pypi_0           pypi
typing-extensions                4.12.2           pypi_0           pypi
tzdata                           2025.2           pypi_0           pypi
ucrt                             10.0.22621.0     haa95532_0
unittest2                        1.1.0            pypi_0           pypi
urllib3                          2.5.0            pypi_0           pypi
vc                               14.3             h2df5915_10
vc14_runtime                     14.44.35208      h4927774_10
vs2015_runtime                   14.44.35208      ha6b5a95_10
wheel                            0.45.1           py312haa95532_0
xz                               5.6.4            h4754444_1
yacs                             0.1.8            pypi_0           pypi
zlib                             1.2.13           h8cc25b3_1

fetal_body segmentation weight: Dataset2025_fetalbody
fetal_brain segmentation weight: Dataset921_fetalbrain

Using the default nnUnet settings, only the epoch was changed to 250, and 3D-fuller and 5-fold cross-validation were used during training.
