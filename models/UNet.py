import torch
import torch.nn as nn
import torch.nn.functional as F

class UNet(torch.nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)