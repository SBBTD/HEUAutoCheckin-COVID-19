### HEUAutoCheckin-COVID-19
HEU哈尔滨工程大学平安行动自动打卡，支持多账户、Github Actions和Server酱微信推送。

首先`fork`下来，在`settings`中添加secret，名称为`ACCOUNTS`，内容可通过如下python脚本生成（SCKey设为空串则关闭微信推送，但请勿删除此项，[点此了解SCKey](http://sc.ftqq.com/)）：

```
import json
print(json.dumps([
    {'usr': '20XXXXXXXX', 'pwd': 'YourPassword', 'SCKey': ''},
    {'usr': '20XXXXXXXX', 'pwd': 'YourPassword', 'SCKey': 'SCUxxxxxxxxxxxxxx'},
]))
```

然后去Actions页面执行一次checkin流程，第一次使用会有很多安全提示，成功执行一次后则会每天7:00自动执行。

secret被添加后，不会被包括开发者在内的任何人（甚至您自己）所见，请知悉开发者不会获取您的个人凭据信息。

本项目仅用作学习交流，不可用于实际生产生活，因本项目产生的后果均由使用者自负！
