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
| Hotbar | Tap a slot | 1–6 |
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
- **Minimap and Earth map:** outside, a heading-up minimap (top right) shows the terrain, the station, your beacons and a gold diamond on the current objective, with its distance. Tap it or press M for the full north-up Earth map with your coordinates.
- **Combat themes:** five tracks (Predator I–IV and Wonders of Laniakea, combat version). In play, one is picked at random whenever something hostile engages you; it takes over from the ambient music and fades out a few seconds after the fight ends. You can preview them in Settings → Combat themes, where each tap plays the next track.
- **Held items:** whatever is selected in the hotbar (ice pick, med kit, thermal lamp, or a placeable) is shown in your right hand, positioned to fit your species.
- **Building:** select a placeable in the hotbar and a green preview appears in front of you; attack to place it. Walk up to it and press E (TAKE) to pick it back up.
- What you mine and build is remembered per wanderer and saved with your save game.

## Repository layout

```
index.html                  the complete game, with all assets embedded
assets/models/              source 3D models (.glb), including hfos_soldier.glb (original HFOS colours)
assets/audio/               main menu theme, combat themes (combat/), opening narration, James Brown's lines (prologue + Chapter I)
assets/logo_reference.png   logo / font style reference
```

The files in `assets/` are the source copies. The game doesn't load them, because `index.html` already contains them.

## Saves

The game never autosaves. It writes progress only when you choose **Save game**, either from the main menu (Save / Load) or from the pause menu in a chapter.

- There are three save slots. Each holds all your wanderers, the active one, their chapter progress, and where you were standing if you saved in the station.
- Changes since your last save are kept only in memory and are marked **UNSAVED**. Loading or overwriting a slot asks you to confirm.
- **Delete save** (in Save / Load or the pause menu) clears a slot after a second tap to confirm.
- When the game starts, it reads your most recent save so Continue picks up where you left off. That only reads; it never writes.
- Saves live in the browser's local storage, so each browser and device keeps its own slots.
