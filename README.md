# “江苏图采”微信小程序照片上传工具
主要原理：Charles抓包，Map Remote到本地Flask服务器，使用Multipart Encoder修改multipart中的照片文件。

## 操作步骤
### 1.配置Charles抓包
现在安卓系统越来越封闭，建议使用IOS/PC/MAC端配置好Charles抓包。
- 参考[Charles抓包教程](https://blog.csdn.net/NianShaoQingKuang1/article/details/145994014)

配置好后，请先在小程序中跑一遍上传逻辑，确认可以正常抓到“jstxcj.91job.org.cn”的包

### 2.修改并运行modify_multipart.py
请将程序中的照片路径修改为你要上传的照片路径：
```python
file_obj = open(r'C:\Pictures\avatar.jpg', 'rb')
```
安装对应的包并运行flask
```bash
pip install flask,requests_toolbelt
python modify_multipart.py
```

### 3.Charles中配置好Map Remote
Map To的Host就填127.0.0.1。参考配置如下：

<img width="60%" alt="截屏2024-05-13 23 43 25" src="https://github.com/Little-King2022/jstc_pic_uploader/assets/110970384/6b8841ca-edee-4760-99ef-87059a6e1c4b">

### 4.在小程序中直接拍照吧～
你会惊讶地发现，照片会被成功替换！🥳



