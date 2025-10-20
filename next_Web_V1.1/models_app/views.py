from django.shortcuts import render


def dashboard(request):
    context = {
        'username': '研究员'
    }
    return render(request, 'models_app/dashboard.html', context)


def self_supervised(request):
    # 自监督学习模型列表 - 便于扩展
    self_supervised_models = {
        '基础模型': [
            {'name': 'DINOV1', 'description': 'Facebook提出的自监督视觉Transformer模型'},
            {'name': 'DINO2', 'description': 'DINO的改进版本，支持更大规模训练'},
            {'name': 'DINOV3', 'description': '最新版本的DINO模型，性能进一步提升'},
            {'name': 'ConvNextV2', 'description': 'ConvNext的自监督版本'},
        ],
        '对比学习模型': [
            {'name': 'SimCLR', 'description': '简单的对比学习框架'},
            {'name': 'MoCo', 'description': '动量对比学习模型'},
            {'name': 'BYOL', 'description': '引导你自己的潜在表示'},
        ],
        '掩码重建模型': [
            {'name': 'MAE', 'description': '掩码自编码器'},
            {'name': 'BEiT', 'description': 'BERT预训练的视觉Transformer'},
        ]
    }

    context = {
        'model_categories': self_supervised_models,
        'page_title': '自监督模型选择'
    }
    return render(request, 'models_app/self_supervised.html', context)


def supervised(request):
    # 监督学习模型列表 - 便于扩展
    supervised_models = {
        '目标检测模型': [
            {'name': 'YOLOV1', 'description': '第一个YOLO版本，实时目标检测'},
            {'name': 'YOLOV2', 'description': '改进的YOLO版本，支持更多尺度'},
            {'name': 'YOLOV3', 'description': '三尺度预测的YOLO版本'},
            {'name': 'YOLOV4', 'description': '引入多种技巧的优化版本'},
            {'name': 'YOLOV5', 'description': 'PyTorch实现的YOLO版本'},
            {'name': 'YOLOV6', 'description': '面向工业应用的版本'},
            {'name': 'YOLOV7', 'description': '最新版本的YOLO模型'},
            {'name': 'YOLOV8', 'description': '支持检测、分割、分类的多任务版本'},
        ],
        '语义分割模型': [
            {'name': 'DeepLabV3', 'description': '使用空洞卷积的语义分割模型'},
            {'name': 'DeepLabV3+', 'description': 'DeepLabV3的改进版本'},
            {'name': 'FPN', 'description': '特征金字塔网络'},
            {'name': 'U-Net', 'description': '经典的编码器-解码器分割架构'},
            {'name': 'Mask R-CNN', 'description': '实例分割模型'},
            {'name': 'SegNet', 'description': '基于编码器-解码器的分割网络'},
        ],
        '分类模型': [
            {'name': 'ResNet', 'description': '残差网络'},
            {'name': 'EfficientNet', 'description': '高效的缩放网络'},
            {'name': 'Vision Transformer', 'description': '视觉Transformer'},
            {'name': 'Swin Transformer', 'description': '滑动窗口Transformer'},
        ]
    }

    context = {
        'model_categories': supervised_models,
        'page_title': '监督模型选择'
    }
    return render(request, 'models_app/supervised_model.html', context)


def select_model(request, model_type, model_name):
    # 这里处理模型选择逻辑
    context = {
        'model_type': model_type,
        'model_name': model_name,
        'message': f'已选择 {model_type} - {model_name} 模型'
    }
    return render(request, 'models_app/model_selected.html', context)