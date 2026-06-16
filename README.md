# smalldog

一个用 `pygame` 写的小型跑酷游戏。

你扮演一只单身狗：

- 左右移动躲开情侣狗
- 跳起来穿过障碍
- 吃到鸡腿会加分
- 被情侣狗撞到 3 次就结束

## 这次优化做了什么

- 修正了错误依赖，项目现在真正依赖 `pygame`
- 重写主循环，拆成 `MENU / PLAYING / GAME_OVER` 三个状态
- 增加分数、生命、等级 HUD
- 增加难度递增：分数越高，障碍移动越快、生成越密
- Game Over 页面会展示最终分数和达到的等级
- 修复资源路径，打包和直接运行都能正确找到素材
- 修复障碍物绘制和回收逻辑，避免对象越积越多
- 去掉每帧 `print` 和一批模板残留代码
- 增加 `Enter` 开始/重开，`Esc` 退出
- 音乐初始化改成容错模式，没音频设备也不会直接崩

## 运行

```bash
uv sync
uv run python main.py
```

没有 `uv` 也可以：

```bash
python -m pip install -r requirements.txt
python main.py
```

## 操作

- `Left / Right`: 左右移动
- `Space`: 跳跃
- `Enter`: 开始或重新开始
- `Esc`: 退出

## 自动化烟雾测试

这个项目支持无窗口短跑测试：

```bash
set SDL_VIDEODRIVER=dummy
set SDL_AUDIODRIVER=dummy
set SMALLDOG_HEADLESS_TEST_FRAMES=120
python main.py
```
