from dataset_temp import custom_dataset
import albumentations as A
from albumentations.pytorch import ToTensorV2
from torch.utils.data import DataLoader
import torch

# device 윈도우 기반 그래픽카드 엔비디아 사용 시 
device = torch.device('cuda' if torch.cuda.is_available else 'cpu')

# device  m1, m2 칩셋 사용 시 
# device = torch.device('mps:0' if torch.backend else 'cpu')

# augmentation
train_transform = A.Compose([
    A.Resize(height=224, width=224),
    ToTensorV2()
])

val_transform = A.Compose([
    A.Resize(height=224, width=224),
    ToTensorV2()
])

# dataset
train_dataset = custom_dataset('./data/train', transform=train_transform)
val_dataset = custom_dataset('./data/val', transform=val_transform)

# dataloader
train_loader = DataLoader(train_dataset, batch_size=24, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=24, shuffle=False)



# 디버깅
for i, (image, target) in enumerate(train_loader):
    print(i, image, target)

    