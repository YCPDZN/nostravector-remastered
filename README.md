# NOSTRAVECTOR Remastered

*Exploration Division*

A story-driven 3D sci-fi exploration game that runs in the browser on phones and desktops. It's set in **2125 AD**.

## Play

Open `index.html` in a modern browser. It needs an internet connection the first time, because the 3D engine (Three.js) and the fonts load from public CDNs. Everything else is built into that one file: the models, music and voice lines.

## What's in the game

- **Main menu** with the wandering astronaut, Continue, New Game, Wanderers, Mission Brief and Settings.
- **Opening:** a flight through the Milky Way to Earth, with five narrated quotes.
- **Character creator:** you choose callsign, species, gender, skin, hair, beard, and suit or armour colours.
- **Four playable species:**
  - **Human:** from Earth, which survived the Third World War 30 years ago and has only recently entered spaceflight.
  - **Erisian:** from the dwarf planet Eris. They travel to Earth as merchants or as bodyguards to human nobles.
  - **Chompy:** from Janira Prime and Aridaxx. They're long-lived, and some remember Sevirrus's fracturing of their empire 300 years ago. Today they're loyal to Emperor Hak Chompjak V.
  - **Grek:** from the garden space station Archiostal, guided by their god Archamus.
- **Multiple wanderers:** create several characters, switch between them at any time, and each one tracks its own chapter progress.
- **Manual save / load:** three slots, and nothing is saved unless you choose to.
- **Prologue:** a hypothermic collapse on the Antarctic ice and a rescue by James Brown, with his lines voiced.
- **Chapter I · Antarctica:** explore the research station. Objectives:
  1. Speak to James Brown (voiced).
  2. Inspect the station: the bunk, heater, window, radio and outer hatch.
  3. Sleep in the bunk.
- **The dream:** after you sleep, the leader of your species appears and speaks to you in a voiced, unnamed monologue.
- **The wake-up:** you wake to find the outer hatch open and James Brown gone. The new objective is to find him.
- **Procedural Antarctica:** step outside into endless, procedurally generated terrain in the style of No Man's Sky: snowfields, wind-cut ridges, rocky cliffs, frozen lakes, rock outcrops and ice spires, all under a blizzard. Each wanderer has their own world seed. James's footprints lead away from the station; fresh patches of prints and his lantern glow lead you to him about 400 m out (objectives: Find James Brown → Speak to James Brown). Hold Shift (or push the stick fully) to run.
- **The meeting on the ice:** about halfway along James's trail, a cutscene plays: James talking with a soldier in black armour with cyan trim. The armour is a Human Federation of Sol (HFOS) design, but the Federation doesn't wear those colours. Press Space/E to advance a line, or Skip. It plays once per wanderer.
- **Lip sync:** James and all four species leaders move their jaws and mouths with their recorded voices.

## Controls

| | Phone | Computer |
|---|---|---|
| Move | Left thumbstick (push fully to run, lightly to walk) | WASD / arrow keys (run by default; C toggles walking) |
| Sprint | SPRINT button (toggle) | Hold Shift |
| Jump | JUMP | Space |
| Dodge roll | DODGE | Q |
| Attack / mine / place / use | ATTACK | Click (without dragging) or F |
| Look | Drag the right side | Drag the mouse; wheel to zoom |
| Interact / advance text | TALK / LOOK / TAKE button, or tap the text | E or Enter |
| Hotbar | Tap a slot | 1–6 (once James has joined you: mouse wheel) |
| Order James | JAMES button, or walk up to him and tap ORDER | 1 Mine · 2 Explore · 3 Base · 4 Wander · 5 Follow |
| Zoom (outside, once James has joined) | — | − / = |
| Inventory & crafting | Bag button | I or Tab |
| Earth map | Tap the minimap | M |
| Pause | ☰ button | Esc |

## Survival

- **Health and stamina:** sprinting, jumping, dodging and swinging cost stamina, which refills when you rest.
- **Gathering:** attack rocks (stone, sometimes scrap metal), ice spires (ice, sometimes frost crystal) and supply crates (scrap metal, cloth, sometimes frost crystal). Three crates sit near the station to get you started.
- **Crafting** (Inventory → Craft):
  - Ice pick: doubles mining and melee damage.
  - Med kit: +40 health.
  - Thermal lamp, wind barrier and signal beacon.
  - Camp heater: heals you while you stand nearby.
- **James Brown, companion:** after you find him and he finishes speaking, James joins you. He carries his own rifle (slung on his back, ready for when hostile creatures arrive) and takes orders:
  - **1 · Mine:** heads for the nearest rock, ice spire or crate, mines it with his pick and adds what he finds to your bag.
  - **2 · Explore:** scouts on his own, up to ~260 m away, and sometimes brings back a resource.
  - **3 · Meet me back at base:** walks back to the station and waits by the door (and is inside when you go in).
  - **4 · Wander around:** strolls around where he is.
  - **5 · Follow me:** the default. If you get more than 40 m ahead, he catches up by appearing just behind you.
  On a phone, tap **JAMES** under your objectives, or walk up to him and tap **ORDER**. He shows as a green dot on the minimap.
- **Voiced scenes:** the meeting cutscene (James and the soldier) and James's lines at the end of the trail are fully voiced with lip sync.
- **Main menu:** set in Antarctica at polar night, with aurora and snowfall; once James has joined you, he walks alongside your wanderer. The moon-style menu is kept for when the story reaches the Moon.
- **Options:** in the pause menu (and Settings on the main menu) you can turn the music on or off separately from all sound. Both choices are remembered.
- **Custom creations** (main menu): creator tools in the spirit of Spore's editors and Galactic Adventures. Creations are stored on this device separately from save slots, and are only saved when you press Save.
  - **Species creator:** build a creature with a live 3D preview (drag to rotate, scroll to zoom, Walk to see it move). You can set legs (0, 2, 4 or 6), leg length, arms, body length and width, tail, back spikes, neck, head, snout, 1–8 eyes, horns, ears, skin pattern (plain, stripes, spots, bands, scales), three colours, bioluminescence and size. Add lore: temperament, diet, homeworld and a description.
  - **Planet maker:** pick a preset (terran, ice, desert, ocean, volcanic, jungle, toxic or gas giant) and tune the seed, sea level, continents versus islands, mountains, size, colours, atmosphere, clouds, rings, moons, climate, gravity and life.
  - **Adventure maker:** name and summarise an adventure, choose its planet (Earth or one of yours), set the difficulty and XP reward, cast up to 8 characters (Human or your own species, as ally, neutral or enemy, each with a line of dialogue), and write up to 8 acts with goals (reach, talk, collect, defeat, explore, survive), a target and story text. The preview shows your cast on the stage under your planet. Playing adventures comes in a later update.
- **Levels 1–100:** every wanderer earns XP and levels up from 1 to a maximum of 100. The level and XP bar sit above your objectives, and the level shows in the Wanderers list and on the main menu.
  - **XP from:** mining (rock 12, ice 10, crate 15; half when James mines), crafting (tools 30, everything else 20), placing builds (8), walking outside (1 per 25 m), and story moments (inspecting 15 each, talking to James 50, resting 100, stepping outside 50, the meeting 100, finding James 150, James joining 250).
  - **Each level:** +2 max health (298 at level 100), and a full heal on level up. Levels 20, 50 and 80 each add +1 mining damage.
  - XP needed per level grows from 100 (level 1→2) to about 14,900 (99→100); reaching 100 takes about 640,000 XP in total. Wanderers made before levels existed get XP for the story they've already played.
 in the pause menu (and Settings on the main menu) you can turn the music on or off separately from all sound. Both choices are remembered.
- **Minimap and Earth map:** outside, a heading-up minimap (top right) shows the terrain, the station, your beacons and a gold diamond on the current objective, with its distance. Tap it or press M for the full north-up Earth map with your coordinates.
- **Antarctica exploration music:** four tracks play while you're out on the ice, shuffled with quiet gaps of 9–25 seconds between them. The music fades when you go inside, softens during pauses and cutscenes, and steps aside for combat themes.
- **Combat themes:** five tracks (Predator I–IV and Wonders of Laniakea, combat version). In play, one is picked at random whenever something hostile engages you; it takes over from the ambient music and fades out a few seconds after the fight ends. You can preview them in Settings → Combat themes, where each tap plays the next track.
- **Held items:** whatever is selected in the hotbar (ice pick, med kit, thermal lamp, or a placeable) is shown in your right hand, positioned to fit your species.
- **Building:** select a placeable in the hotbar and a green preview appears in front of you; attack to place it. Walk up to it and press E (TAKE) to pick it back up.
- What you mine and build is remembered per wanderer and saved with your save game.

## Repository layout

```
index.html                  the complete game, with all assets embedded
assets/models/              source 3D models (.glb), including hfos_soldier.glb (original HFOS colours)
assets/audio/               main menu theme, combat themes (combat/), Antarctica exploration music (antarctica/), opening narration, James Brown's lines (prologue + Chapter I)
assets/logo_reference.png   logo / font style reference
```

The files in `assets/` are the source copies. The game doesn't load them, because `index.html` already contains them.

## Saves

The game never autosaves. It writes progress only when you choose **Save game**, either from the main menu (Save / Load) or from the pause menu in a chapter.

- There are three save slots. Each holds all your wanderers, the active one, their chapter progress, and where you were standing if you saved in the station.
- Changes since your last save are kept only in memory and are marked **UNSAVED**. Loading or overwriting a slot asks you to confirm.
- **Delete save** (in Save / Load or the pause menu) clears a slot after a second tap to confirm.
- Each wanderer remembers exactly where they were (out on the ice or in the station). Saving, loading, Continue and going to the main menu all put you back on that spot.
- When the game starts, it reads your most recent save so Continue picks up where you left off. That only reads; it never writes.
- Saves live in the browser's local storage, so each browser and device keeps its own slots.
