# DailyFresh

一,数据库设计:
1)用户表: ID,用户名,密码,邮编,激活标识,权限标识
2)地址表: ID,收件人,收件地址,邮编, 联系方式,是否默认,用户ID
3)商品SKU表: ID, 名称, 简介,价格,单位,库存,图片, 状态,种类ID, SPUID
4)商品种类表: ID, 种类名称, logo,图片,
5)首页轮播商品表:ID,skuID, 图片,index
6)商品SPU表: ID,名称, 详情
7)首页促销活动表: ID,图片,活动URL,index
8)订单信息表: 订单ID,地址ID,用户ID,支付方式,总数目,总金额,运费,支付状态,创建时间
9)订单商品表: ID,订单ID, skuID, 商品数量,商品价格
10)商品图片表: ID,图片,SKUID
11)首页分类商品展示表: ID,skuID,种类ID,展示标识,index

二,Django static的配置和使用, 这部分很容易出错, 导致引用CSS或者JS文件404
首先在settings 里面设置:
STATIC_URL = '/static/'
STATICFILES_DIRS = [
os.path.join(BASE_DIR, 'static')
]
目录中的建立的目录 是static
其次: TEMPLATES 中要引入: 'django.template.context_processors.static',
最后 模板中引用的时候:  {% load static %}    <link rel="stylesheet" type="text/css" href="{% static 'css/reset.css' %}">
三,用户注册流程小结:需要说明的有
1)注册成功后, 发送激活邮件: 用到的是 from django.core.mail import send_mail, 发送激活邮件需要传送用户信息, 对用户信息加密用到了from itsdangerous import TimedJSONWebSignatureSerializer as dangerous_serializer 得到 加密的token bytes
然后对token进行decode 转换成str 拼接到激活地址中

四, 用celery异步发送邮件:
发送邮件原理: 用户发送邮件---先到SMTP服务器---然后再到收件人邮箱,收件时间如果不用异步的话, 出现网络问题之后, 会让用户一直等待



