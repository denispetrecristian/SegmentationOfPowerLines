import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class Discriminator(torch.nn.Module):
    '''
    '''
    def __init__(self,) -> None:
        super(Discriminator, self).__init__()
        self.conv1 = nn.Conv2d

    def forward(self, x):
        pass


class Generator(torch.nn.Module):
    '''
    
    '''
    def __init__(self) -> None:
        super(Generator, self).__init__()

    def forward(self, x):
        pass

class GAN(torch.nn.Module):
    '''
    
    '''
    def __init__(self) -> None:
        super(GAN).__init__()

    def forward(self, x):
        pass