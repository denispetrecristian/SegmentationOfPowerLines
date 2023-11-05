import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class Discriminator(torch.nn.Module):
    '''
    '''
    def __init__(self,) -> None:
        super(Discriminator, self).__init__()
        self.conv1 = nn.Conv2d(3*64,128)
        self.conv2 = nn.Conv2d(128,256)
        self.conv3 = nn.Conv2d(256,512)
        self.conv4 = nn.Conv2d(512,1)

        self.batch_norm1 = nn.BatchNorm2d(128)
        self.batch_norm2 = nn.BatchNorm2d(256)
        self.batch_norm3 = nn.BatchNorm2d(512)

    def forward(self, x):
        x1 = F.relu(self.conv1(x))
        x2 = F.relu(self.batch_norm1(self.conv2(x1)))
        x3 = F.relu(self.batch_norm2(self.conv3(x2)))
        x4 = F.relu(self.batch_norm3(self.conv4(x3)))


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