---
name: tactile-toy
description: 做"手感小玩具"网页：一个单独的 HTML 文件，用 three.js，双击就能在浏览器里玩。画面里是一个用真实材质做的物件（软糖、肥皂泡、黏土、玻璃、麻薯……），能抓、捏、拉、扔，有弹簧阻尼的回弹手感；版式固定：白底、左上编号加衬线斜体标题、右侧浮动面板、左下操作提示、圆形光标。用户说"做个小玩具""做个能玩的网页""再做一个 Nº 系列的""像 jelly bricks / mochi pets 那样""做个 three.js 小东西""做个捏/戳/堆/吹的玩具""弄个解压小游戏"时使用，哪怕只说了一个物件名（"做个水球"）也用。Builds single-file three.js tactile toy pages (squishy physical materials, spring-damper feel, fixed editorial layout) in the user's numbered "Goods" series. Not for full games with levels, menus or scores, multi-page sites, or React/build-tool projects.
---

# 手感小玩具（tactile-toy）

一句话：**一个物件 + 真实的材质 + 有弹性的手感 + 固定的版式 + 一个让人想反复玩的动作。**

交付物是一个 `.html` 文件：three.js 和（需要时）cannon-es 通过 importmap 从 unpkg 加载，没有构建步骤，双击打开就能玩。这是一个编号系列（Nº 09–22 已经做了 14 个，在 `examples/` 里），新做的要和它们放在一起不突兀。

## 用户的七条规则

这些是用户自己总结的，每一条都要落实到代码里：

| # | 规则 | 落到代码里是什么 |
|---|---|---|
| 1 | 一句话说清楚是什么、怎么交付：一个单独的 HTML 文件、用 three.js、直接在浏览器打开 | 单文件，importmap 引 `three@0.160.0`，不用 npm、不拆文件、不用本地资源（贴图用 canvas 现画） |
| 2 | 用真实材质描述外观：不说"好看"，说"像真的软糖：有光泽、半透明、越厚颜色越深"，并点名参数（transmission、clearcoat、环境贴图） | 先写一句"像真的什么"，再从 `references/materials.md` 挑配方；环境贴图（RoomEnvironment）永远开着 |
| 3 | 把手感写成动作和反应：抓起来被拉长、松手回弹、落地被压扁再弹起来；用弹簧阻尼 + 顶点着色器实现。**这是最关键的部分** | 位置交给物理，形变交给弹簧；`references/feel.md` 的事件 → 冲量表 |
| 4 | 固定版式：白背景、左上编号 + 衬线斜体标题、右侧浮动面板（色块、一个滑块、实时计数、一个黑色按钮）、左下操作提示、圆形光标 | `assets/template.html` 的 CSS 和 DOM 原样用，只改文字和强调色 |
| 5 | 给好初始场景：一打开就有东西可以玩，不是一片空白 | 开场就摆好物件，最好有东西在轻轻动 |
| 6 | 点名一两个"爽点"，写清分寸（"活泼但不要像爆炸"） | 爽点单独做一个函数，所有速度和冲量都有上限 |
| 7 | 性能：笔记本上跑到 60fps | 见下面的性能清单，交付前实测 `__toy.fps` |

## 流程

### 1. 先写一份简报

用户通常只给一个物件名（"做个水球"）。不要连环追问：自己把七条填满，在回复开头用 5–7 行列出来，然后直接做。只有连物件本身都不清楚的时候才问。简报长这样：

```
Nº 23 / Wet Goods — Water / Balloon.
物件：几只灌了水的气球，躺在白纸上。
材质：像真的橡胶水球：薄、有光泽、半透明，透出里面的水色（transmission 0.6 + clearcoat + sheen）。
手感：戳一下凹进去然后整只晃；抓起来下面坠着被拉长；扔下去落地压扁、水在里面晃两下才停。
面板：Balloon（5 色）/ Fill（滑块：越满越沉、晃得越久）/ Balloons · Splashes / Fill another
开场：5 只大小不一的水球，散在画面左侧。
爽点：扔太狠会"啪"地破掉，溅出一圈水滴，很快消失。分寸：水滴少而快，不铺满屏幕。
```

### 2. 找最接近的例子，读源码

看 `references/catalog.md`，挑一两个手感最像的页面完整读一遍（12–20 KB）。最常用的两个：

- **能堆、能推倒、真刚体** → `examples/jelly-bricks.html`（cannon-es + 顶点着色器 + 吸附）
- **软的、圆的、会自己动** → `examples/mochi-pets.html`（手写物理 + 整体缩放 + 戳坑）
- 可以按出印子的表面 → `sand-garden.html` / `clay-stamp.html`；透明薄膜 → `soap-bubbles.html`；有声音 → `wind-chimes.html`

### 3. 从模板开始

把 `assets/template.html` 复制到当前工作目录，文件名用英文短横线（`water-balloon.html`）。模板里已经有：固定的 CSS 和 DOM、渲染器（ACES、阴影、像素比上限）、环境贴图、灯光、阴影地面、圆形光标、`swatches()`、`Spring` 类、`softMaterial()`（带压扁/剪切/拉长/戳坑/余震的物理材质）、相机漂移、主循环、`window.__toy` 调试句柄。

替换 `{{...}}`，再把 `TODO` 的地方写满：

- **编号**：在输出文件夹里找最大的编号 +1（复制模板之前跑 `grep -hoE "Nº [0-9]+" *.html | sort -t' ' -k2 -n | tail -1`）。文件夹里没有就用目录里的下一个（Nº 23）。
- **类别**：`{{Kind}} Goods`，一个词说清它的物理性质：Soft、Air、Rolling、Pressed、Squishy、Ringing、Quiet、Glowing、Popped、Grown、Bonded、Acidic。
- **标题**：两个词拆成两行，`Word /<br><span>Word.</span>`，第二个词上强调色、带句号。一个词的名字按音节拆（Pop / Corn.）。
- **一句话**：平实，说它是什么，可以带一点小情绪（"Take your time." "Wait for it."）。
- **强调色**：物件的主色，同时是色块的第一个颜色。
- **页面上的文字全用英文**，和系列保持一致，除非用户要中文。

### 4. 材质

读 `references/materials.md`。先写"像真的什么"，再选配方。透明的东西颜色交给 `attenuationColor`，表面色往白色拉；软的东西靠 `sheen`；亮的东西靠 `clearcoat`。

### 5. 手感（最花时间的一步）

读 `references/feel.md`。要点：

- 位置由物理决定（cannon-es 或手写），形变由每个物件自己的弹簧决定，只影响画面。
- 先列出"事件 → 哪根弹簧 → 踢多大"，再写代码。至少覆盖：按下、拖动、松手、落地、互相碰撞。
- 唯一的滑块就是手感的"性格"：`k = 300-230*knob`、`z = 0.3-0.22*knob`，所有弹簧共用。
- 抓起来要先"拉"再"起"：有一个被拽长的瞬间，过了阈值才真正离开。
- 光标按下时缩小变实心（`#cur.hold`），松开恢复。

### 6. 开场场景和爽点

- 开场：物件已经摆好，数量刚好够玩（5–10 个），大小、颜色有变化。最好有一点自发的动静（风、待机小跳、在流的墨水），画面不是死的。
- 爽点：一两个，单独写成函数（`shake()`、`topple()`、`pop()`）。所有速度、冲量都设上限，弹性系数低，"弹"交给形变弹簧，而不是物理反弹。
- 面板上的黑色按钮给"再来一些"或"还原"，让人能一直玩下去；物件总数设上限，超了就移除最旧的。

### 7. 验证

打开页面亲自看，别只看代码：

1. **起一个本地静态服务器再打开**。内置浏览器里 `file://` 页面不执行脚本，只是一张静态快照。在 `.claude/launch.json` 里加一项 `python -m http.server <端口> --bind 127.0.0.1 --directory <页面所在文件夹>`，用 `preview_start` 按名字启动，再打开 `http://localhost:<端口>/xxx.html`。测完删掉这一项。
2. 控制台没有报错（着色器编译错误也会出现在这里）。
3. 等 3 秒，读 `window.__toy.fps`，应该 ≥ 55。不够就按下面的性能清单砍。
4. 截图检查版式：标题在左上，面板在右侧居中，提示在左下；**主体在画面偏左，没有被面板挡住**；颜色对不对（尤其透明薄层会不会发黑）。浏览器窗格很窄时，用 `resize_window` 设成笔记本尺寸（1280×760）再看；模拟尺寸下截图有时会缩在角落里，以 `innerWidth` 和 JS 读到的状态为准。
5. **真的去玩，用 JS 来玩**。把物件投影到屏幕坐标，往 canvas 上派发 `PointerEvent`，再从 `__toy` 读弹簧状态，确认每个动作都有反应、所有数值都在上限内：

   ```js
   const s=v=>{v=v.clone().project(__toy.camera);return [(v.x+1)/2*innerWidth,(1-v.y)/2*innerHeight];};
   const fire=(type,x,y,t=document.querySelector('canvas'))=>t.dispatchEvent(new PointerEvent(type,{clientX:x,clientY:y,bubbles:true}));
   // 戳：pointermove(window) → pointerdown(canvas) → 读形变 → pointerup(window)
   // 拖扔：pointerdown 后每 16ms 一次 pointermove(window)，再 pointerup，之后每 25ms 采样一次剪切/速度，看最大值和 2–3 秒后能不能停下
   // 爽点：直接调 __toy 上暴露的函数（比如 shake()），确认没有东西飞出边界、翻倒或穿地
   // 按钮：连点到超过数量上限，确认计数和上限一致
   ```

   所以 `window.__toy` 里要暴露物件数组、爽点函数和关键计数。

### 8. 交付

告诉用户：文件路径；怎么玩（就是左下角那行提示）；爽点在哪、怎么触发；实测帧率。不用解释代码。

## 版式：什么固定，什么可以变

**固定（原样复制模板的 CSS，不要"优化"）**：白底；左上 40px/34px 的标题块（小型大写编号、64px Georgia 斜体、14px 灰色一句话）；右侧 220px 半透明毛玻璃面板，垂直居中；面板里 h4 是 11px 大写灰字，计数是 22px Georgia 斜体；黑色胶囊按钮；左下 12px 灰色提示；26px 圆形光标，全页 `cursor:none`；相机自动缓慢漂移，没有轨道控制（鼠标是"手"，不是"镜头"）。

**可以变**：色块数量（通常 5）、计数行数（2–3）、多一组 `.seg` 切换、h4 后面跟当前选项名、面板里放一张小图表（ph-lab）、输入框（data-garden）。但面板只放这些：一个滑块、一个按钮。控件越多越不像玩具。

## 性能清单（60fps）

- `setPixelRatio(Math.min(devicePixelRatio,1.5))`，阴影贴图 1024。
- 几何体缓存复用；每个物件一份材质只为了独立 uniform，用 `customProgramCacheKey` 共用 shader。
- 物件总数设上限；小而多的东西（水滴、碎屑、粒子）用 `InstancedMesh`。
- 主循环里不 `new` 向量，复用临时变量；DOM 计数每 10 帧更新一次。
- `dt = Math.min(clock.getDelta(), 1/30)`；弹簧分 4 个子步。
- cannon-es：`SAPBroadphase`、`allowSleep`、静止物件 `sleep()`。
- 高度场只在改动后 `computeVertexNormals()`。
- `transmission` 很贵，数量多时换成 `opacity` 做法。

## 常见问题

- **透明材质一片灰** → 环境贴图被删了，或者 `envMapIntensity` 太低。
- **主体被面板挡住** → `camera.lookAt` 的 x 往正方向偏（系列里是 1.2–2.4），主体就落到画面偏左。
- **形变方向不对** → 剪切和拉长方向要转进物件局部坐标（乘物件旋转的逆）。
- **一碰就飞** → 有速度没加上限，或者 restitution 太高。
- **拖动时选中了文字** → `user-select:none`（模板里有）。
- **透明物件前后闪** → 前后面拆成两个 mesh、固定 `renderOrder`（见 materials.md）。
- **开场是空的** → 规则 5，开场就要能玩。

## 文件

- `assets/template.html`：起点，固定的版式和基础设施。
- `references/materials.md`：真实材质 → 参数配方，地面阴影，透明的坑。
- `references/feel.md`：弹簧、事件冲量表、抓拉拖扔、三种形变方式、手写物理、爽点分寸、声音。
- `references/catalog.md`：14 个已有页面的一览、面板写法变体、开场场景。
- `examples/*.html`：14 个已有页面的完整源码。
