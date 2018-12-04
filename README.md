# 有道云笔记转为知笔记

有道云笔记导出全部数据，为PDF格式，为知笔记支持导入HTML格式，使用`pdf2htmlex`格式转换

## 使用

**建议在Linux/WSL中使用**

### 安装`pdf2htmlex`

`sudo apt install pdf2htmlex`

> 其他系统参考 https://github.com/coolwanglu/pdf2htmlEX

### 编辑main.py中文件名

例子如下

```python
# 有道笔记目录
rootpath="/mnt/d/YoudaoNote/"
# 导出的PDF文件夹
rootdir="2018-11-25-23-53"
# 转换后目标文件夹
destdir="Linux_EX_HTML"
# 日志文件
logfile="log.txt"
```

最后会是这样

```
/mnt/d/YoudaoNote/
-- 2018-11-25-23-53
    -- xx
        -- aaa.pdf
    -- xxx.pdf
-- Linux_EX_HTML
    -- xx
        -- aaa.html
    -- xxx.html
-- log.txt
```

### 运行

`python main.py`