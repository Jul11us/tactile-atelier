# 材质配方：从"像真的什么"到具体参数

先说清楚它在现实里像什么（"像真的软糖：有光泽、半透明、越厚颜色越深"），再从下面挑最接近的一行改。所有配方都假设场景里有 `RoomEnvironment` 环境贴图和 ACES 色调映射（模板里已经配好）：没有环境贴图，透明和清漆材质会是一片死灰。

每一行都是系列页面里实际用过、看起来对的数值。

## 透明 / 半透明

| 像什么 | 配方 | 出处 |
|---|---|---|
| 软糖、果冻（越厚越深） | `color: c.lerp(白,0.15), transmission:0.92, thickness:1.4, attenuationColor:c, attenuationDistance:0.55, roughness:0.12, ior:1.38, clearcoat:1, clearcoatRoughness:0.06, specularIntensity:1, envMapIntensity:1.2` | jelly-bricks |
| 彩色玻璃管（薄、清脆） | `color: tint.lerp(白,0.55), transmission:1, thickness:0.35, ior:1.5, attenuationColor:tint, attenuationDistance:1.6, roughness:0.04, clearcoat:1, clearcoatRoughness:0.03, envMapIntensity:1.6, specularIntensity:1` | wind-chimes |
| 玻璃弹珠外壳 | `color:'#fff', transmission:1, thickness:0.5, ior:1.5, roughness:0, clearcoat:1, envMapIntensity:1.4`；里面另放一个带花纹贴图的小球 | marble-run |
| 烧杯、实验玻璃 | `transmission:1, thickness:0.12, ior:1.47, roughness:0.03, clearcoat:1, envMapIntensity:1.5, side:DoubleSide` | ph-lab |
| 肥皂泡（薄膜彩虹） | `transmission` + `iridescence:1, iridescenceIOR:1.33, iridescenceThicknessRange:[250,1000], clearcoat:1, clearcoatRoughness:0, envMapIntensity:2.6`。环境里要加几块彩色方板，薄膜才有东西可映 | soap-bubbles |
| 水、溶液（很淡） | `roughness:0.03, clearcoat:1, transparent:true, opacity:0.12, depthWrite:false, envMapIntensity:1.2` | crystal-grow |

**越厚颜色越深**靠的是 `attenuationColor` + `attenuationDistance`：光在材质里走得越远，被染得越深。`attenuationDistance` 越小越浓。`color` 往白色拉一点，表面就不会脏。

## 软 / 哑光 / 有绒感

| 像什么 | 配方 | 出处 |
|---|---|---|
| 麻薯、团子（软、微微发光） | `roughness:0.5, sheen:0.5, sheenColor:白, sheenRoughness:0.45, clearcoat:0.35, clearcoatRoughness:0.5, emissive:同色, emissiveIntensity:0.08` | mochi-pets |
| 黏土（哑、软） | `roughness:0.88, metalness:0, sheen:0.6, sheenRoughness:0.8, sheenColor:白` | clay-stamp |
| 爆米花（干、蓬） | `vertexColors:true, roughness:0.75, sheen:0.6, sheenColor:白`；黄油点缀另用 `roughness:0.3, clearcoat:0.8` | popcorn |
| 花瓣 | `roughness:0.45, sheen:0.6, sheenColor:白, emissive:同色, emissiveIntensity:0.05` | data-garden |
| 天鹅绒展台 | `color:'#1d2330', roughness:0.75, sheen:0.6, sheenColor:'#5a6680'` | crystal-grow |
| 沙 | `MeshStandardMaterial roughness:1`，`map` 和 `bumpMap` 用同一张随机灰度噪点 canvas 贴图，`bumpScale:0.6`，`repeat` 铺开 | sand-garden |

`sheen` 是"软"的关键：边缘有一圈柔光，像绒面。加一点同色 `emissive`，暗面就不会发灰，看起来像光从里面透出来。

## 有光泽 / 硬

| 像什么 | 配方 | 出处 |
|---|---|---|
| 塑料分子球（糖果般亮） | `roughness:0.18, clearcoat:1, clearcoatRoughness:0.05, metalness:0` | molecule-kit |
| 发光墨水 | `emissive:同色, emissiveIntensity:0.9, roughness:0.12, clearcoat:1, clearcoatRoughness:0.05, transparent:true`，下面垫一张同色光晕贴图 | gel-pens |
| 平底锅（会烧红） | `color:'#2b2b2f', metalness:0.7, roughness:0.35, clearcoat:0.5, emissive:'#ff5a1a'`，`emissiveIntensity` 跟温度走 | popcorn |
| 石子 | `roughness:0.42`，灰褐色 HSL 随机明度 | sand-garden |
| 金属挂件 | `metalness:1, roughness:0.25` | wind-chimes |

## 地面与阴影

- 默认：`ShadowMaterial({opacity:0.13})` 的大平面 + 一盏投影平行光（mapSize 1024、`radius:6`、`bias:-0.0008`）。白背景上只看得到阴影，物件像放在一张白纸上。
- 物件很多、会飞起来，或者不想开 shadowMap 时：每个物件脚下放一片径向渐变贴图（模板里的 `blobTex`），离地越高越淡越大（mochi-pets、soap-bubbles）。
- 彩色物件下面可以再垫一片同色光晕（`MeshBasicMaterial` + 光晕贴图，`opacity≈0.4`，`depthWrite:false`，`renderOrder:-1`），像透明糖果在白纸上投下的彩色光（jelly-bricks）。

## 踩过的坑

- **透明物件前后闪**：玻璃容器把背面（`BackSide`）和正面（`FrontSide`）拆成两个 mesh，固定 `renderOrder`（背面 1、液体 2、内容物 3、正面 4），不要让 three.js 每帧自己排序（crystal-grow）。
- **共面闪烁**：两个面贴在一起时抬高 0.002–0.004（crystal-grow 的玻璃皿、地面光晕）。
- **薄的透明层（焦糖、糖浆、果酱）发黑**：白底上 `attenuationDistance` 太小（< 0.3）、颜色又深的时候，薄层会接近黑色。焦糖用 `#b5601c`、`attenuationDistance:0.4`、`color` 往白 lerp 0.25，看起来才是琥珀色。厚的地方自然会更深。（Nº 22 布丁测试里踩过）
- **透明壳盖在不透明物件上**：壳透过去能看到下面的东西，前提是下面那个物件是不透明的（transmission 只采样不透明物体）。所以布丁本体用不透明的 sheen 配方，焦糖才用 transmission。
- **透明材质的 `color` 别太饱和**：往白色 lerp 0.15–0.55，颜色交给 `attenuationColor`，不然看起来像塑料。
- `transmission` 很贵：只要场景里有一个 transmission 物件，每帧就要多渲染一遍不透明物体到一张贴图；而且每个 transmission 物件的片元着色本身也重。物件数量要设上限（jelly-bricks 是 46 块），小而多的东西（水滴、碎屑）改用 `opacity` 做法。
