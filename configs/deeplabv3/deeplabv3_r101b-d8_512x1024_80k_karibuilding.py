_base_ = './deeplabv3_r50-d8_512x1024_80k_karibuilding.py'
model = dict(
    pretrained='torchvision://resnet101',
    backbone=dict(type='ResNet', depth=101))
