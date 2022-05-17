_base_ = 'mmdetection/configs/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_coco.py'

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1),
        mask_head=dict(num_classes=1)))

dataset_type = 'COCODataset'
classes = ('balloon',)
dataset = dict(
    _delete_=True,
    type="MineAppleDataset",
    classes=("fruit",),
    data_root="data/")
data = dict(
    train=dict(
        **dataset,
        pipeline={{ _base_.data.train.pipeline }}),
    val=dict(
        **dataset,
        pipeline={{ _base_.data.val.pipeline }}),
    test=dict(
        **dataset,
        test_mode=True,
        pipeline={{ _base_.data.test.pipeline }}))

load_from = 'checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'