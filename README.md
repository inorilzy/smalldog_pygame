# smalldog

> 一个用 `pygame` 写的小型跑酷游戏：躲开情侣狗，收集鸡腿，尽量活得更久。

## Features

- 菜单、游玩、结算三个状态清晰分离。
- 分数、生命、等级 HUD 实时展示。
- 分数越高，障碍移动越快、生成越密。
- Game Over 页面展示最终分数和等级。
- 支持 `Enter` 开始 / 重开，`Esc` 退出。
- 音频初始化带容错，没有音频设备时也能运行。

## Quick Start

推荐使用 `uv`：

```bash
uv sync
uv run python main.py
```

不用 `uv` 也可以：

```bash
python -m pip install -r requirements.txt
python main.py
```

## Controls

| Key | Action |
| --- | --- |
| `Left` / `Right` | 左右移动 |
| `Space` | 跳跃 |
| `Enter` | 开始或重新开始 |
| `Esc` | 退出 |

## Assets

游戏资源位于：

```text
image/
sound/
font/
```

直接运行和打包运行都会通过统一资源路径加载素材。

## Smoke Test

项目支持无窗口短跑测试，适合在没有图形界面的环境里验证主循环不会立刻崩溃：

```bash
set SDL_VIDEODRIVER=dummy
set SDL_AUDIODRIVER=dummy
set SMALLDOG_HEADLESS_TEST_FRAMES=120
python main.py
```

PowerShell 可写成：

```powershell
$env:SDL_VIDEODRIVER='dummy'
$env:SDL_AUDIODRIVER='dummy'
$env:SMALLDOG_HEADLESS_TEST_FRAMES='120'
python main.py
```

## Development Notes

- 主入口：`main.py`
- 游戏逻辑和资源加载在主循环中保持简单直接。
- 依赖以 `requirements.txt` 和 `pyproject.toml` 为准。

## Limitations

- 当前没有正式 release 包。
- 资源、关卡和碰撞规则都偏小型 demo，不是完整商业游戏框架。

## License

No license file is currently included. Add an explicit license before redistributing or accepting contributions.
