# HealthyWork
生活不止有屏幕上的代码,还有诗和远方. 
这是一款基于Python语言和PyQt图形化框架编写的桌面应用，用来提醒正在电脑前工作的人们注意休息，以保障身体健康。

## Features
- 防颈椎病
- 防腰间盘突出
- 防痔疮
- 防心脏病
- 自定义壁纸
- 自定义时间
- 本地音乐播放
- 全屏显示，窗口置顶
- 界面简约（编不下去了）
- 你值得拥有

![截图](https://github.com/Sindgein/HealthyWork/blob/master/Screenshot.png)
![截图](https://github.com/Sindgein/HealthyWork/blob/master/Screenshot_2.png)
## Dependence
- python3.6
- PyQt5

## How to work
```python
python healthywork.py 
```
## Custom

初次运行会在用户目录下的.config文件夹中创建healthywork/config.json文件，写入的都是config.py中DEFAUT_CONFIG 变量内所定义的json字符串。

如下：

```pytho
DEFALUT_CONFIG = {
    'label_stylesheet': "color: rgb(255, 0, 127);font: 30pt \"WenQuanYi Micro Hei Mono\";",
    'button_stylesheet': "background-color: rgba(182, 176, 171, 90);color: rgb(255, 0, 127);font: 30pt \"WenQuanYi Micro Hei Mono\";",
    'message': "喝杯水休息一下吧",
    'count': "        ",
    'time_work': "1800000",
    'time_rest': "300000",
    'wallpapers_dir': "./wallpapers",
    'music_dir': "./music",
    'with_music': "1"
}
```

- label_stylesheet： 界面上标签的样式
- button_stylesheet：界面上按钮的样式
- message：提醒的文字
- count：给倒计时标签占位用的，方便计算label的位置
- time_work: 工作时间间隔，单位毫秒，默认半小时
- time_rest: 休息时间间隔，单位毫秒，默认五分钟
- wallpapers_dir: 存放壁纸的目录，默认为当前的wallpapers目录
- music_dir: 存放音频的目录，默认为当前的music目录
- with_music: 休息时是否播放音乐，1为播放，0为不播放。默认播放。