# smalldog
相关技术：
	Pygame、精灵组、精灵序列图的加载和控制、地图滚动、碰撞检测
项目描述：
  基于Python开发的小黄狗跑酷游戏。玩家控制单身狗移动跳跃，躲避情侣狗；玩家可以吃地图中随机生成的鸡腿，吃到鸡腿时计分器会根据得分发生改变，同时根据存活时间玩家也可以得到相应的存活分。当情侣狗触碰玩家1次时，天空会下起雪花，当情侣狗触碰玩家3次时，游戏结束，显示结束画面。
  开发中，先对游戏窗口初始化，然后加载图片、音乐、文字、图形等游戏元素；使用键盘监听、鼠标监听来响应用户的外部输入；引入随机函数，增加游戏随机性；使用碰撞检测，处理游戏中各元素发生碰撞时产生响应的效果；使用标志位控制整个游戏的流程；计分器根据用户得分做出响应。
