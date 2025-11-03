import os
import dicom2nifti
import concurrent.futures

def process_dicom_dir(dicom_dir, output_dir):
    try:
        output_filename = os.path.join(output_dir, os.path.basename(dicom_dir) + '.nii.gz')
        dicom2nifti.dicom_series_to_nifti(dicom_dir, output_filename)
        print(f"成功处理: {dicom_dir}")
    except Exception as e:
        print(f"处理 {dicom_dir} 时出错: {e}")

def alternative_dicom_to_nii(input_dir=r'F:\mydata\fetalBrainBody\images\1008', output_dir=r'F:\mydata\fetalBrainBody\images\1008\NIIGZ'):
    os.makedirs(output_dir, exist_ok=True)
    dicom_dirs = set()
    for root, dirs, files in os.walk(input_dir):
        if any(file.lower().endswith(('.dcm', '.dicom')) for file in files):
            dicom_dirs.add(root)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(process_dicom_dir, dicom_dir, output_dir) for dicom_dir in dicom_dirs]
        concurrent.futures.wait(futures)

if __name__ == '__main__':
    alternative_dicom_to_nii()