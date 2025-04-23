import flask
from flask import request, Response
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

app = flask.Flask(__name__)

@app.route('/v2/camera/upload', methods=['POST'])
def modify():
    try:
        # 获取请求参数
        file_type = request.form.get('type')
        code = request.form.get('code')
        token = request.headers.get('Authorization')
        content_type = request.headers.get('Content-Type')
        boundary = content_type.split(';')[1].split('=')[1]

        # 构建请求头（移除冲突的Host头）
        modify_headers = {
            'Authorization': token,
            'User-Agent': request.headers.get('User-Agent'),
            'Content-Type': f'multipart/form-data; boundary={boundary}',
            'Referer': request.headers.get('Referer')
        }

        # 打开本地照片（添加文件存在性检查）
        try:
            file_obj = open(r'C:\Pictures\avatar.jpg', 'rb')
        except FileNotFoundError:
            return Response("替换文件不存在", status=500)

        # 构建Multipart数据
        modify_form = {
            'type': (None, file_type),
            'code': (None, code),
            'file': ('modified.jpg', file_obj, 'image/jpeg')
        }
        encoder_multipart = MultipartEncoder(fields=modify_form, boundary=boundary)

        # 发送请求
        res = requests.post(
            'https://jstxcj.91job.org.cn/v2/camera/upload',
            data=encoder_multipart,
            headers=modify_headers,
            proxies={"http": None, "https": None},  # 强制禁用代理
            verify=False,  # 忽略证书验证
            timeout=10  # 添加超时
        )
        res.raise_for_status()  # 检查HTTP状态码
        return res.content

    except requests.exceptions.RequestException as e:
        print(f"请求错误: {str(e)}")
        return Response(f"上游请求失败: {str(e)}", status=500)
    except Exception as e:
        print(f"未知错误: {str(e)}")
        return Response("服务器内部错误", status=500)
    finally:
        file_obj.close()  # 确保文件句柄关闭

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6689, debug=True)