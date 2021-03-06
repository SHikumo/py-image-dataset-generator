import random
import os
import time

from augmentation.operations import OperationPipeline
from utils.utils import FileUtil, ProgressBarUtil, NoImageFoundException


class DatasetGenerator(OperationPipeline):
    folder_path = None
    num_files = None
    save_to_disk = True
    folder_destination = "result"

    def __init__(self,
                 folder_path: str,
                 num_files: int = 50,
                 save_to_disk=True,
                 folder_destination="result") -> None:
        super().__init__()
        self.folder_path = folder_path
        self.num_files = num_files
        self.save_to_disk = save_to_disk
        self.folder_destination = folder_destination

    def preview(self):
        """
            It print a preview of :
                - dataset current size
                - operations list
                - dataset augmented size
        """
        pass

    def execute(self, gen_type):
        """
            Execute the pipeline operation as configured
        """
        start_time = time.time()
        images_in_folder = FileUtil.get_images_file_path_array(self.folder_path)
        
        label_in_folder = []
        for f in os.listdir(self.folder_path):
            if f.endswith('.txt'):
                label_in_folder.append(f)
                print("label " + f)

        if not images_in_folder:
            raise (NoImageFoundException("No images found in %s folder" % self.folder_path))

        images_to_transform = []

        
        # pick 'num_files' random files that will be use for data augmentation
        while len(images_to_transform) < self.num_files:
            # random.choice(images_in_folder)
            images_to_transform.append(random.choice(images_in_folder))

        i = 0
        for file_path in images_to_transform:
            try:
                files_name = os.path.basename(file_path)
                print("\n")
                # print(" " + files_name)
                files_name = os.path.splitext(files_name)[0]
                
                
                augmented_image = FileUtil.open(file_path)
                for operation in self.operations:
                    random_num = random.uniform(0, 1)
                    do_operation = random_num <= operation.probability
                    if do_operation:
                        augmented_image = operation.execute(augmented_image)
                        
                if self.save_to_disk:
                    print(files_name)
                    for label in label_in_folder:
                        label_name_wtxt = os.path.basename(label)
                        label_name = os.path.splitext(label_name_wtxt)[0]
                        if files_name == label_name:
                            if gen_type == 'blur':
                                FileUtil.save_file(augmented_image, label_name_wtxt, self.folder_path, self.folder_destination, str(files_name) + '_blur')
                            elif gen_type == 'noise':
                                FileUtil.save_file(augmented_image, label_name_wtxt, self.folder_path, self.folder_destination, str(files_name) + '_noise')    
                    # pass
                    
            finally:
                i = i + 1
                ProgressBarUtil.update(i, self.num_files)

        end_time = time.time()
        print('\n\n %s images generated in the folder %s in %s sec' % (self.num_files, self.folder_destination, round(end_time - start_time, 2)))
