# 拉勾职位信息爬虫
&emsp; 通过拉勾职位信息API抓取拉勾所有职位信息 (限定50页) 并进行数据分析。

## 抓取流程
1. 抓取拉勾网页站点首页所有职位名称，构造并遍历职位列表页URL
2. 设置 meta 参数的 cookiejar 请求职位列表页，获取服务器返回的Cookies
3. 设置 meta 参数的 cookiejar 请求职位信息接口，回调给解析函数解析

## 解释
&emsp; 拉勾主要是Cookies反爬，所以在 Request 或者 FormRequest 时设置 meta 的 cookiejar 是必不可少的。为方便调试，Spider 中设置仅抓取职位列表的第一个职位的前10页数据，请根据需要自行更改代码，例如：
```Python
......
    for position_url in position_url_list:
        cookiejar = CookieJar()
        yield Request(url=position_url,
                    callback=self.get_position_data,
                    errback=self.error_back,
                    dont_filter=True,
                    priority=10,
                    meta={'kd': position_name_list.pop(0), 'cookiejar': cookiejar})
    # 测试仅请求第一个职位
    break
......
```
&emsp; 注意，虽然拉勾显示某个职位可能有上万条数据，但超过正常访问范围便会返回空数据。举个例子，你去淘宝搜iPad，你最多看两三页就烦了，所以淘宝只给你返回100页，尽管它有成千上万条数据。因此设置爬取极限为50页。
```Python
MAX_PAGES = 50
```
&emsp; 已实现的中间件：RandomUAMiddleware、ProxyMiddleware、RetryMiddleware。已实现的管道：MysqlTwistedPipeline、ExcelPipeline、JsonPipeline。详见代码。

## 反反爬
&emsp; 随机UA，挂代理，随机下载延时，cookiejar。前三种方法我已经在“ [58同城房屋信息爬虫](https://github.com/Northxw/City58) ”中提到，此处不再赘述。而cookiejar的设置原理就是session机制。

## 运行
&emsp; Pycharm 中直接运行 main.py 文件即可。

## 更新列表
&emsp; 2019.4.15 已更新。

## 可视化
&emsp; Tableau 做了简单的可视化。如下：

![map](https://github.com/Northxw/Lagou/blob/master/Lagou/utils/other/map.png)

![map_2](https://github.com/Northxw/Lagou/blob/master/Lagou/utils/other/salary.png)
