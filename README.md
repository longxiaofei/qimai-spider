### Use(不能用了，有时间更新)

1. [七麦数据](https://www.qimai.cn)免费注册一个账号
2. 登录
3. 复制cookie, 粘贴到程序第7行的cookie对象上
4. 运行

```
"""
    :brand; str, free,免费榜  paid,付费榜  grossing,畅销榜
    :country; str, cn,中国; us,美国; tr,土耳其;  ...
    :device; str, ipad or iphone
    :date; str, example, 2018-11-13
"""
demo = get_datas(brand='free', country='cn', date='2018-11-13', device='iphone')
for data in demo:
    print(data)
```
