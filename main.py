import torch
import argparse
import logging
from logger import Logger
from torch.utils.data import Dataset, DataLoader


def train():
    pass

def validate():
    pass

def test():
    pass


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--lr", type=float, default=1e-2)
    parser.add_argument("--weight-decay", type=float, default=1e-4)
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--model", type=str, default="GAN")
    parser.add_argument("--dataset", type=str, default="/")

    arguments = parser.parse_args()
    logger = Logger(arguments.model)

    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")

    logger.log(f"THe device is {device.type}.", 1)
    logger.log(f"Loading the dataset", 1)

    transforms = []

    train_data = Dataset(path, )



if __name__ == "__main__":
    main()