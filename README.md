# HEUAutoCheckin-COVID-19
HEU哈尔滨工程大学平安行动自动打卡，支持多账户、Github Actions和Server酱微信推送。

首先`fork`下来，添加secret，名称为`ACCOUNTS`，内容通过如下脚本生成（SCKey留空则不开启推送）：

```
import json
json.dumps([
    {'usr': '20XXXXXXXX', 'pwd': 'YourPassword', 'SCKey': ''},
    {'usr': '20XXXXXXXX', 'pwd': 'YourPassword', 'SCKey': 'SCUxxxxxxxxxxxxxx'},
])
```

然后去Actions页面执行一次，之后则会每天7:00自动执行。



本项目仅用作学习交流，因本项目产生的后果均由使用者自负！