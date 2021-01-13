# 本脚本仅用于学习交流，因此脚本导致的任何后果请自行承担。

import asyncio
import json
from pyppeteer import launcher


# #生成Secret方式：(SCKey留空则不通知微信)
# import json
# json.dumps([
#     {'usr': '20XXXXXXXX', 'pwd': 'YourPassword', 'SCKey': ''},
#     {'usr': '20XXXXXXXX', 'pwd': 'YourPassword', 'SCKey': 'SCUxxxxxxxxxxxxxx'},
# ])


async def checkin():
    accounts = json.loads(input().strip())
    for a in accounts:
        try:
            browser = await launcher.launch()
            print('#####################')
            page = await browser.newPage()

            # 登录
            await page.goto('http://one.hrbeu.edu.cn/infoplus/form/JKXXSB/start')
            await page.type('#username', a['usr'])
            await page.type('#password', a['pwd'])
            await page.click('.loginBtn')
            print('[Login]usr:' + a['usr'][:2] + '******' + a['usr'][-2:])

            # 勾选结尾复选框
            await asyncio.sleep(17)
            await page.click('#V1_CTRL82')
            print('[CheckBox]Checked.')

            # 提交表单
            await asyncio.sleep(7)
            await page.click('.command_button_content > nobr')
            print('[Submit]Clicked.')

            # 确认提交
            await asyncio.sleep(7)
            await page.click('.dialog_button.default')
            print('[Confirm]Yes.')

            # 完成提交
            await asyncio.sleep(7)
            await page.click('.dialog_button.default')
            print('[Finish]Done.')

            # 检查结果
            await asyncio.sleep(7)
            if '无需任何操作' in await page.evaluate('document.body.textContent'):
                print('[Result]OK!')
                url = page.url
            else:
                print('[Result]Failed!')
                url = None
            await page.close()

            # 微信推送
            if a['SCKey'] != '':
                wx = await browser.newPage()
                if url:
                    await wx.goto(
                        'https://sc.ftqq.com/' + a['SCKey'] + '.send?text=平安行动打卡成功！流水号'
                        + url.split('/')[-2] + '&desp=用户名:' + a['usr'] + '；链接' + url)
                else:
                    await wx.goto('https://sc.ftqq.com/' + a['SCKey'] + '.send?text=平安行动打卡可能失败了！'
                                  + '&desp=用户名:' + a['usr'])
                await wx.close()
            await asyncio.sleep(3)
            await browser.close()
        except Exception as e:
            print(e)


asyncio.get_event_loop().run_until_complete(checkin())
