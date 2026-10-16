# 系列目录（examples/ 里的 14 个页面）

做新玩具前，挑一个最接近的读一遍源码再动手。它们都是单文件，12–20 KB。

## 一览

| Nº | 文件 | 标题 | 类别 | 强调色 | 物件 / 材质 | 操作提示 | 技术要点 |
|---|---|---|---|---|---|---|---|
| 09 | jelly-bricks.html | Jelly / Bricks. | Soft | `#e8323c` | 半透明软糖积木，transmission + attenuation | Grab to lift · Drop to snap · Space to wobble | cannon-es、顶点着色器形变、吸附粘连、整塔晃、推倒 |
| 10 | soap-bubbles.html | Soap / Bubbles. | Air | `#4aa8ff` | 薄膜肥皂泡，iridescence | Hold to blow · Release to float · Click a bubble to pop | 彩色环境房间、相互粘连合并、破裂水滴、InstancedMesh |
| 11 | marble-run.html | Marble / Run. | Rolling | `#3d7bff` | 玻璃弹珠 + 彩色轨道件 | Drag a piece to move · Right-click or R to rotate · Scroll to raise | cannon-es、可重搭的轨道、合成音效 |
| 12 | clay-stamp.html | Clay / Stamp. | Pressed | `#d9825b` | 哑光黏土板，sheen | Click to stamp · Drag to draw · Shift-drag to smear | 高度场、印章遮罩、慢慢松回原样 |
| 13 | mochi-pets.html | Mochi / Pets. | Squishy | `#f08aa6` | 有表情的麻薯团子，sheen + 微自发光 | Poke to jiggle · Hold to squeeze · Drag to stretch | 手写物理、整体缩放保体积、戳坑着色器、眨眼表情、自己会跳 |
| 14 | wind-chimes.html | Glass / Chimes. | Ringing | `#3fb5c4` | 七根调音玻璃管 | Swipe through to strike · Click once for sound · Gust to let the wind play | 摆锤、划过检测、WebAudio 泛音 + 混响 |
| 15 | sand-garden.html | Sand / Garden. | Quiet | `#b8925a` | 枯山水沙盘 + 石子 | Drag to rake · Double-click to set a stone · Drag a stone to move it | 220×150 高度场、耙纹、石子周围的同心圆 |
| 16 | gel-pens.html | Gel / Pens. | Glowing | `#ff3d9a` | 黑板上的荧光凝胶墨水 | Drag to draw · Ink runs with Flow · Wipe to start over | 管状笔画、发光、往下流的墨滴、开场涂鸦 |
| 17 | popcorn.html | Pop / Corn. | Popped | `#e9a21c` | 平底锅 + 玉米粒/爆米花 | Hold anywhere to heat · Let go and it cools back to kernels · Heat again to re-pop | cannon-es、温度、锅底烧红、爆开音效 |
| 18 | data-garden.html | Data / Garden. | Grown | `#3f9d5a` | 数字长成的花 | Type numbers + Enter · Hover to read · Click a plant to shake it | 输入框、样例数据 `.seg`、生长动画 |
| 19 | molecule-kit.html | Molecule / Kit. | Bonded | `#ff2a1a` | 糖果感的原子球 | Click to place · Drag onto an atom to bond (again for double/triple) · Click to poke · Shift-click to remove | 按化合价成键、分子式实时显示 |
| 20 | ph-lab.html | pH / Lab. | Acidic | `#e8336b` | 烧杯 + 指示剂溶液 | Click to drip · Hold to keep dripping · A / B to switch acid and base | 真实化学计算、液面旋涡着色器、面板里的小曲线图 |
| 21 | crystal-grow.html | Crystal / Grow. | Grown | `#1f78e6` | 过饱和溶液里长晶体 | Click the solution to seed · Faster cooling, faster growth · Pick a substance to change the habit | 玻璃皿前后面分开渲染、晶形、天鹅绒底座（three@0.170.0） |
| 22 | caramel-pudding.html | Caramel / Pudding. | Wobbly | `#e0a032` | 焦糖布丁：不透明 sheen 布丁 + transmission 焦糖壳（带滴落） | Poke to jiggle · Drag and let go to slide · Space to shake the table | 手写物理、多 mesh 共用一套形变 uniform、惯性剪切（急停甩一下）、整桌一起晃 |

下一个编号是 **Nº 23**。如果输出文件夹里已经有更新的页面，以文件夹里最大的编号 +1 为准。

## 面板写法的变体

所有页面都是同一个面板骨架，只是内容不同：

- **色块标签**：Flavor / Flavour、Film tint、Marble、Clay、Ink、Butter、Palette、Element、Indicator、Substance、Sand、Glass tint。叫它在现实里的名字，不叫 "Color"。
- **滑块**（只有一个）：Wobble、Breeze、Gravity、Softness、Squish、Wind、Rake width、Flow、Heat、Growth speed、Vibration、Cooling、Drop concentration。
- **计数**：2–3 行，第一行通常是"我做了多少次"（Pokes、Stamps、Strokes、Popped、Chimes struck），第二行是"现在有多少"（Bricks、Pets、Bubbles、Stones），第三行可选，放一个状态量（Pan 温度、Formula、pH）。
- **黑色按钮**：一个动词短语，"再来一些"或"还原"：Pour more bricks、Blow a cloud、Drop marbles、Adopt more、Gust、Rake it smooth、Smooth it out、Wipe clean、Add kernels、Fresh water、Dissolve all。
- **可选**：一组 `.seg` 胶囊切换（clay-stamp 的印章形状、ph-lab 的酸/碱、data-garden 的样例）；h4 标签后面跟当前选项名（`<span style="letter-spacing:0;text-transform:none;color:#111">`，见 ph-lab、crystal-grow）。

## 开场就有东西玩

没有一个页面是空的：

- jelly-bricks：中间一块 4×2 当地基，周围散着 9 块不同尺寸、不同颜色的积木。
- mochi-pets：5 只不同口味的团子围成一圈，会自己跳。
- soap-bubbles：开场 6 个泡泡在飘。
- sand-garden：3 块大小不一的石子，沙面已经耙好平行纹，石子周围是一圈圈同心纹。
- gel-pens：板上已经有一幅涂鸦。
- marble-run：一条搭好的轨道。
- data-garden：输入框里预填 8 个数，花园已经长出来。
- wind-chimes：有风，管子在轻轻碰。
