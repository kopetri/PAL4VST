_base_ = [
    '../_base_/models/upernet_convnext.py', '../_base_/datasets/artifacts_cmgan_supercaf_1024.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
crop_size = (1024, 1024)
checkpoint_file = 'https://download.openmmlab.com/mmclassification/v0/convnext/downstream/convnext-small_3rdparty_32xb128-noema_in1k_20220301-303e75e3.pth'  # noqa
model = dict(
    backbone=dict(
        type='mmcls.ConvNeXt',
        arch='tiny',
        out_indices=[0, 1, 2, 3],
        drop_path_rate=0.4,
        layer_scale_init_value=1.0,
        gap_before_final_norm=False,
        init_cfg=dict(
            type='Pretrained', checkpoint=checkpoint_file,
            prefix='backbone.')),
    decode_head=dict(
        in_channels=[96, 192, 384, 768],
        num_classes=2,
    ),
    auxiliary_head=dict(in_channels=384, num_classes=2),
    test_cfg=dict(mode='slide', crop_size=crop_size, stride=(341, 341)),
)

optimizer = dict(
    constructor='LearningRateDecayOptimizerConstructor',
    _delete_=True,
    type='AdamW',
    lr=0.0001,
    betas=(0.9, 0.999),
    weight_decay=0.05,
    paramwise_cfg={
        'decay_rate': 0.9,
        'decay_type': 'stage_wise',
        'num_layers': 6
    })

lr_config = dict(
    _delete_=True,
    policy='poly',
    warmup='linear',
    warmup_iters=1500,
    warmup_ratio=1e-6,
    power=1.0,
    min_lr=0.0,
    by_epoch=False)



# fp16 settings
optimizer_config = dict(type='Fp16OptimizerHook', loss_scale='dynamic')
# fp16 placeholder
fp16 = dict()

# By default, models are trained on 8 GPUs with 2 images per GPU
data = dict(samples_per_gpu=8)
checkpoint_config = dict(by_epoch=False)
evaluation = dict(interval=200, metric=['mIoU', 'mFscore'], pred_eval=True, save_best='mIoU')


# Data
data_root = '/home/lingzzha/artifacts/data/cmgan_supercaf/processed'
data = dict(
    samples_per_gpu=8,
    workers_per_gpu=4,
    train=dict(
        img_dir='mmseg_images_1024/train',
        ann_dir='mmseg_labels_1024/train'),
    val=dict(
        img_dir='mmseg_images_1024/val',
        ann_dir='mmseg_labels_1024/val'),
    test=dict(
        img_dir='mmseg_images_1024/test_cmgan',
        ann_dir='mmseg_labels_1024/test_cmgan'))


