# 发布到 GitHub Pages

目标账号：**SunKai-Tsinghua**。建议仓库名：**MARGIN**。

此目录已整理为可以独立发布的静态站点。只需上传 `github-homepage` **目录内的文件**；不要上传整个本地 MARGIN 项目、临床表格、论文修订文件或本地训练权重。

## 发布步骤

1. 登录 `SunKai-Tsinghua`，创建公开仓库 `MARGIN`。如仓库已经存在，先检查其内容，合并所需网站文件，避免覆盖已有代码。
2. 将本目录内容上传到仓库 `main` 分支根目录，确保 `index.html` 位于根目录，保留 `assets/`、`docs/`、README 等文件的相对位置。将空文件 `.nojekyll` 一并提交。
3. 在仓库 **Settings → Pages → Build and deployment** 中，将 Source 设置为 **Deploy from a branch**，选择 **main** 和 **/(root)**，点击 **Save**。

成功部署后，预期网站地址为：`https://SunKai-Tsinghua.github.io/MARGIN/`。该地址仅为配置后的预期地址，不能据此认定网站已经上线。请以 GitHub Pages 返回的实际访问地址和部署状态为准。

官方说明：[创建 GitHub Pages 站点](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) · [配置发布来源](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

## 本地预览

在本目录运行：

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

浏览器访问 `http://127.0.0.1:8000`。

网站无需 Node.js、构建命令或第三方 CDN。图像均为当前论文中的研究图，首屏胆道图为明确标注的概念示意图。

## 更新发布状态

两个开源部分应分别更新：

- **分割模型发布时：**补充真实权重链接、nnU-Net 版本、标签定义、预处理和推理说明及许可证。
- **MARGIN 训练代码发布时：**补充真实代码路径、依赖、训练配置、运行和评估方法及许可证。

同时更新 `README.md`、`README.zh-CN.md`、对应 `docs/` 文档和 `index.html` 的状态文本。分割精度与切缘预测性能应持续分开表述。
