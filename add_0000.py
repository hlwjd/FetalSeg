import os
import shutil

src_folder = r'F:\mydata\fetalBrainBody\images\3Dniigz\zigouhua\images'
dst_folder = r'F:\mydata\fetalBrainBody\images\3Dniigz\zigouhua\images\imagesTs'
os.makedirs(dst_folder, exist_ok=True)

for filename in os.listdir(src_folder):
    if filename.endswith('.nii.gz'):
        name, ext = os.path.splitext(filename)           # 分离 .gz
        name2, ext2 = os.path.splitext(name)             # 分离 .nii
        new_name = f"{name2}_0000{ext2}{ext}"            # 病例名_0000.nii.gz
        src_path = os.path.join(src_folder, filename)
        dst_path = os.path.join(dst_folder, new_name)
        shutil.copy2(src_path, dst_path)                 # 复制并重命名到新文件夹