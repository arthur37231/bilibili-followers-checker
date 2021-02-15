# Followers Checker 粉丝数量监控器（公开版）

建议python版本3.x以上。

如果需要创建虚拟环境，使用命令

`python3 -m venv venv`

并使用命令

```
source venv/bin/activate    (Linux and MacOS)
venv\Script\activate        (Windows)
```

进入虚拟环境。

在运行程序之前，需要使用命令`pip3 install -r requirements.txt`安装程序所依赖的包，
缺少运行所必须的包将导致程序编译或运行时错误。

你也需要在setting.py文件中补充对应的数据库配置，特别是你希望通过/generate请求获取粉丝
数量的同时，将数据结果记录入数据库。如果你不填写数据库的配置，程序将只能获取粉丝的实时数据，
不能记录数据，也不能获取昨日、以及最近N条记录的数据。

## API 功能解释

### /api/generate

__请求方法__：POST

__请求说明__：获取当前目标用户的粉丝数量，并选择是否记录该条数据

__请求参数__：
```
{
  "vmid": String,
  "is_record": Boolean
}
```

__响应参数__: 
```
{
  "bili_follower_number": Number,
  "bili_record_time": String
}
```

### /api/latest

__请求方法__：GET

__请求说明__：获取当前目标用户的最新纪录的粉丝数量

__请求参数__：
```
{
  "vmid": String
}
```

__响应参数__: 
```
{
  "bili_count_id": Number,
  "bili_follower_number": Number,
  "bili_record_time": String,
  "bili_vmid": String
}
```

### /api/yesterday

__请求方法__：GET

__请求说明__：获取当前目标用户昨天最后记录的粉丝数量

__请求参数__：
```
{
  "vmid": String
}
```

__响应参数__: 
```
{
  "bili_count_id": Number,
  "bili_follower_number": Number,
  "bili_record_time": String,
  "bili_vmid": String
}
```

### /api/all

__请求方法__：GET

__请求说明__：获取当前目标用户的所有粉丝数量纪录

__请求参数__：
```
{
  "vmid": String
}
```

__响应参数__: 
```
{
  "followers": Array(Number),
  "time_slots": Array(String)
}
```

### /api/recent

__请求方法__：GET

__请求说明__：获取当前目标用户的最近N条粉丝数量纪录

__请求参数__：
```
{
  "vmid": String,
  "number": Number
}
```

__响应参数__: 
```
[
  {
    "bili_count_id": Number,
    "bili_follower_number": Number,
    "bili_record_time": String,
    "bili_vmid": String
  },
  ...
]
```