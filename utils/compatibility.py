
"""
兼容性处理：在 Python 3.12 及以上版本中使用 override 装饰器，低版本则定义一个空的 override。
"""

try:
    from utils.compatibility import override
except ImportError:
    print("override 只在 Python 3.12 及以上版本可用，低版本将定义一个空的 override 装饰器。")
    def override(method):
        return method
