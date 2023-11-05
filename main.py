import torch
import argparse
import logging
from logger import Logger
from torch.utils.data import Dataset, DataLoader
from models.generative_adversarial_network import Discriminator
from datasets.ttpla.ttpla import TTPLA
from datasets.dataset_utils import Phase
import matplotlib.pyplot as plt

def train():
    pass

def validate():
    pass

def test():
    pass


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--lr", dest='lr', type=float, default=1e-2)
    parser.add_argument("--weight-decay", dest="weight-decay", type=float, default=1e-4)
    parser.add_argument("--batch-size", type=int, default=10, dest="batch-size")
    parser.add_argument("--epochs", type=int, default=10, dest="epochs")
    parser.add_argument("--model", type=str, default="GAN", dest="model")
    parser.add_argument("--dataset", type=str, default="/", dest="dataset")

    args = parser.parse_args()
    logger = Logger(args.model)

    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")

    logger.log(f"The device is {device.type}.", 1)
    logger.log(f"Loading the dataset", 1)

    transforms = []

    train_dataset = TTPLA("/", Phase.TRAINING, None)
    image = next(iter(train_dataset))

    plt.imshow(image.T)
    plt.show()
    





if __name__ == "__main__":
    main()