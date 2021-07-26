import torchvision
import torch
import torchvision.transforms as transforms
import os
import matplotlib.pyplot as plt
import numpy as np


train_dataset_path = ...
test_dataset_path = ...

train_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    # transforms.Normalize(torch.Tensor(mean), torch.Tensor(std))

])
