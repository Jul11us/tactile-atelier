# Tactile Atelier — Gallery design

## Direction

An editorial object catalogue for seventeen tactile browser toys. The presentation borrows the quiet pace of a small design publication: a large serif title, generous margins, real scene photography, numbered objects, and concise descriptions. The existing toy files remain the visual source for the previews and original object numbers.

## Color

| Token | Value | Role |
| --- | --- | --- |
| Paper | `#f4f1e9` | Warm ivory page surface |
| Ink | `#282922` | Main type and dark Skill panel |
| Muted | `#696b60` | Secondary descriptions |
| Line | `#d5d3c8` | Quiet rules and image frames |
| Accent | `#9c492f` | Terracotta title, serials, and focus ring |
| White | `#fbfaf6` | Image fallback surface |

## Typography

- Georgia / Times New Roman provides the expressive serif wordmark, oversized hero, and object titles.
- Arial / Helvetica Neue / Microsoft YaHei supports navigation, small labels, descriptions, and Chinese text.
- Large titles use tight tracking; uppercase catalogue labels use restrained letter spacing.
- The two-line Tactile / Atelier. title uses a narrower responsive scale and a restrained indent to fit the longer name, including the tablet two-column layout.
- English leads the catalogue. Short Chinese labels help identify each toy.

## Layout

- The page uses a maximum width of 1360 px, with 48 px outer margins on desktop and 20 px on small screens.
- An asymmetric two-column hero pairs the title with a larger featured Caramel Pudding preview.
- Seventeen native link cards form a three-column catalogue, falling to two columns on narrow screens.
- A dark two-column Skill panel anchors the end of the page and becomes a single column on mobile.
- Each toy retains its original source serial. The three calm toys appear first, followed by the remaining source sequence.

## Components and interaction

- The gallery is plain HTML and CSS with no JavaScript or third-party assets beyond repository preview images.
- Each card is one semantic anchor with a real screenshot, title, Chinese name, serial, and a source-grounded interaction summary.
- Subtle image scaling and a revealed action label reinforce hover and keyboard focus.
- A skip link, visible focus rings, semantic landmarks, descriptive image text, and reduced-motion handling support navigation.
- Navigation links jump to the collection and Skill; the Skill panel links to its source, downloadable package, and repository.
- Gallery responsiveness does not imply that the original toys support every device. The footer recommends desktop and identifies the external toy dependencies.

## Preview assets

All images use `assets/previews/<game-basename>.jpg`. They are captured from the corresponding toy, rather than generated illustrations. Preview images use a consistent frame with `object-fit: cover` and reserved dimensions to prevent layout jumps while loading.
