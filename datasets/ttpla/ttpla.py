from torch.utils.data import Dataset
from ttpla_dataset_master.scripts import labelme2coco_2, remove_void, split_jsons
from datasets.dataset_utils import Phase
import os


class TTPLA(Dataset):
    '''
    Class that implements the TTPLA: An Aerial-Image Dataset for Detection and Segmentation of Transmission Towers and Power Lines
    dataset based on the paper. The ttpla_dataset-master folder is downloaded from the https://github.com/R3ab/ttpla_dataset/tree/master
    github repository and used for labelling COCO data and spolitting the dataset.

    @inproceedings{abdelfattah2020ttpla,
        title={TTPLA: An Aerial-Image Dataset for Detection and Segmentation of Transmission Towers and Power Lines},
        author={Abdelfattah, Rabab and Wang, Xiaofeng and Wang, Song},
        booktitle={Proceedings of the Asian Conference on Computer Vision},
        year={2020}
    }       
    '''
    def __init__(self, path:str, phase:Phase, transform=None):
        self.image_folder = f'{os.path}/{path}'
        self.transform = transform
        self.file_index_folder = f'{os.path}/"splitting_dataset_txt"'
        self.validation_indeces_file = f'{self.file_index_folder}/"val.txt"'
        self.test_indeces_file = f'{self.file_index_folder}/"test.txt"'
        self.train_indeces_file = f'{self.file_index_folder}/"train.txt"'
        self.phase = phase

        if phase == Phase.TRAINING:
            self.indices = self.file_to_indices_list(self.train_indeces_file)
        
        if phase == Phase.VALIDATION:
            self.indices = self.file_to_indices_list(self.validation_indeces_file)

        if phase == Phase.TESTING:
            self.indices = self.file_to_indices_list(self.test_indeces_file)

    def __getitem__(self, idx):
        pass

    def __len__(self):
        pass

    def create_new_split(self):
        split_jsons()

    def file_to_indices_list(self, path):
        indices = []
        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                indices.append(line)
        
        return indices