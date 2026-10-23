# MARGIN

**胆管及肿瘤分割模型 · 多模态切缘状态预测**

[English](README.md) · [项目主页](https://sunkai-tsinghua.github.io/MARGIN/) · [部署说明](DEPLOY.md)

## 项目介绍

MARGIN 面向肝门部胆管癌（pCCA）的术前 CT 切缘状态预测，结合 CT 影像与三维胆道解剖信息，研究患者级切缘状态预测。

**本项目计划分为两个部分开源，两者具有不同的用途：**

| 开源部分 | 作用 | 计划提供的内容 | 当前状态 |
| --- | --- | --- | --- |
| **第一部分：基于 nnU-Net 的胆管及肿瘤分割模型** | 从术前增强 CT 中自动分割胆管树和原发肿瘤 | 最佳模型权重、Python / Notebook 推理入口、配置及训练曲线 | **已提供** |
| **第二部分：MARGIN 训练代码** | 基于影像与解剖信息进行患者级切缘状态预测 | MARGIN 训练代码及配置说明 | **即将发布** |

分割模型已提供[权重下载](https://github.com/SunKai-Tsinghua/MARGIN/releases/download/segmentation-v1.0.0/MARGIN-segmentation-v1.0.0.zip)、[Python 推理脚本](segmentation/inference.py)和 [Notebook](segmentation/inference.ipynb)。MARGIN 训练代码仍待发布。

## 第一部分：基于 nnU-Net 的胆管及肿瘤分割模型

该部分提供用于**胆管树和原发肿瘤自动分割**的定制化三维 nnU-Net 模型。输入为术前增强 CT，输出为胆管和肿瘤的分割掩膜，可为后续三维胆道重建提供解剖基础。

论文中的分割模型基于 **197 例人工标注的 pCCA CT** 训练。研究流程中，自动分割结果由两位高级放射科医师复核和修正后，才用于三维重建与下游特征提取。

模型为 nnU-Net v2 `ResidualEncoderUNet`，配置为 `3d_fullres`，使用 `fold_all/checkpoint_best.pth`。实际 `plans.json` 指定 1 mm 各向同性间距；此信息直接来自模型配置。

Model details 已补充环境安装、标准 nnU-Net 命令、Python / Notebook 用法及输出标签。该模型采用区域式分割：`danguan=[1,2]`、`tumor=2`；导出的标签为 0 背景、1 非肿瘤胆管标签、2 肿瘤。

本次未执行实际推理测试，训练曲线不代表独立测试集分割性能。公开资源不包含 `validation` 文件夹、测试 CT 或预测体积。

[分割模型说明](docs/segmentation-model.md)

## 第二部分：MARGIN 训练代码

该部分计划发布 **MARGIN 患者级切缘状态预测框架的训练代码**。框架基于 CT 与解剖信息开展 R0 / R1 切缘状态预测研究。

发布时将提供训练代码、配置说明、依赖环境与使用文档。当前版本不包含 MARGIN 训练代码、切缘预测模型权重或临床数据。

[MARGIN 发布概览](docs/margin-training.md)

## 两部分如何衔接

**增强 CT → 胆管及肿瘤分割 → 三维重建 → 特征提取 → 患者级切缘预测。**

![MARGIN 简化研究流程](assets/study-workflow.svg)

本研究为回顾性研究，切除平面根据手术记录及术后 CT 重建，尚未验证对同一患者多个备选手术方案进行比较的能力。

## 研究结果

雷达图展示 MARGIN 在内部和外部评估队列中的准确率、敏感度、特异度、阳性预测值、阴性预测值及 F1 分数。

![MARGIN 内部与外部评估雷达图](assets/model-performance.png)

**这些指标属于患者级切缘状态预测性能，不是 nnU-Net 的分割精度。**

## 研究用途与发布说明

本项目属于研究用途，仍需前瞻性验证。代码和模型的许可条款将在各自正式发布时说明。
