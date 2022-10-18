# 创建虚拟环境 Virtual Environment

Install venv module on Ubuntu 20.04

```bash
sudo apt install -y python3-venv
```

Create a new virtual environment called venv
```bash
python3 -m venv venv
```

Start using the virtual environment
```bash
source venv/bin/activate
```

Stop using the virtual environment 
```bash
deactivate
```

使用pip自动生成requirements.txt文件
```bash
pip freeze > requirements.txt
```
