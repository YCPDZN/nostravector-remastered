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
- **Make camp:** once James joins you, the next objective is to set up a camp with him: build a **crafting table** (+60 XP), then a **teleporter** beside it (+120 XP), which links your camp to the station's pad. Then:
  - **Speak to James Brown:** a gold marker leads you to him. He warns (voiced) that a big storm is rolling in off the plateau, too soon to reach the station, so you'll have to build a shelter.
  - **Build a shelter:** a floor with a roof over it, closed in by walls or doorways. One side may stay open as the way in, and bigger bases of several floors and roofs work too. The objective tracks your floor, walls (3) and roof as you build.
  - **Get inside the shelter:** the storm builds for about 20 seconds after James's warning: wind and snow speed up, the snowflakes grow and a whiteout swallows the sky. When it hits at full strength, the sky darkens to slate, your exosuit flashes red and announces **WEATHER WARNING: SUPER BLIZZARD INCOMING** (SUIT), and the narrator explains how to survive it (five voiced lines with subtitles).
  - **Suit heat:** a heat gauge appears under your stamina. Out in the blizzard it drains (about 90 seconds from full to empty). It recovers inside a shelter, beside a camp heater, inside the station, and once the storm is over. Below 30% the exosuit gives its voiced exposure warning (SUIT2). At zero heat the suit performs an emergency recovery, putting you back at the station with 60% heat.
  - **Wait out the storm with James:** the super blizzard lasts five minutes of active play once it hits (the objective shows a countdown, which pauses while the game is paused), then it clears.
  - **Sleep:** a few seconds after the storm clears, James says (voiced) "I'll make a bed. Feel free to sleep." and lays a bedroll in your shelter (or beside you if the shelter is gone). Press E at the bed to sleep. In the dream, a figure you can't yet name (shown as ????) warns you not to trust James Brown. He describes the soldier James was speaking to, a faction of radical humans gathering under a new banner, and their master, who still stands beside the Federation's ruler. He names none of them. For human wanderers all seven lines are voiced (CH1GREK1–7). Erisian, Chompy and Grek wanderers hear the first three voiced, and lines 4–7 are a single non-human version shared by all three (voiced, CH1GREK4–7NONHUMAN). You wake in the morning beside the bed.
  - **Find James's rover by the teleporter:** a few seconds after you wake, James says (voiced) he wants to get out of Antarctica, and you can take his rover to the nearest ferry about a kilometre away. He parked it next to your teleporter (or the station's pad), and a gold marker shows it.
  - **Drive to the ferry:** press E at the rover to drive it. Use W/S or the stick for throttle, A/D to steer, and E (EXIT) to get out. It does up to about 85 km/h, tilts with the snow, kicks up powder, and stops dead if you hit rocks, trees or walls. James rides with you when he's following. Inside the rover your suit heat recovers. The objective counts down the distance to the **Ross Sea ferry terminal**: a flat landing on the coast with a wooden pier, a red-and-white ferry, a terminal building and open water with drifting ice. The pier and the ferry's gangway can be walked on.
  - **The betrayal:** as you reach the terminal, James steps onto the pier between you and the gangway and turns on you, in a fully voiced 15-line speech (JBBETRAYAL1–15). Near the end his hand comes out of his coat.
  - **Push James Brown into the water:** walk up to him and press E (PUSH). He goes over the side into the sea and is gone.
  - **Boss: Croxian (level 30):** a man with a scythe steps off the ferry and introduces himself as Croxian. James was meant to hand you over to his people. The ferry casts off and swings round to a second berth along the shore. **Run to the ferry**: down the pier, along the coast and up the far jetty once the ferry has tied up there. Croxian chases you: his scythe sweeps (red ring warning) hit for 48, and his leaps onto where you were standing (red circle) hit for 60. Dodge (Q) avoids a hit, and blocking takes most of it. He taunts you as he goes. **Never run at him**: get close while moving towards him and he kills you outright. If you die, the fight resets to just before James turns on you. Reach the jetty and you escape Antarctica, and Chapter I ends (to be continued).
- **Day and night:** outside, a full day lasts 20 minutes. The sun rises and sets with warm dusk light, nights turn dark blue with a sky full of stars, and the light and haze change with it. Each planet keeps its own time of day in your save.
- **HD Antarctica:** the ice uses an HD snow texture (tiled every 4 m, seamless across the endless terrain) under an HD polar sky panorama. Rock outcrops use an HD rock model (with colour, normal and roughness maps), and groves of bare, wind-stripped trees built from an HD bark model stand on the flatter ground. The distance haze and sunlight are matched to the sky's horizon and sun.
- **The meeting on the ice:** about halfway along James's trail, a cutscene plays: James talking with a soldier in black armour with cyan trim. The armour is a Human Federation of Sol (HFOS) design, but the Federation doesn't wear those colours. Press Space/E to advance a line, or Skip. It plays once per wanderer.
- **Lip sync:** James and all four species leaders move their jaws and mouths with their recorded voices.

## Controls

| | Phone | Computer |
|---|---|---|
| Move | Left thumbstick (push fully to run, lightly to walk) | WASD / arrow keys (run by default; C toggles walking) |
| Sprint | SPRINT button (toggle) | Hold Shift |
| Jump | JUMP | Space |
| Jetpack | Hold JUMP while in the air | Hold Space while in the air |
| Block | Hold BLOCK | Hold R or the right mouse button |
| Dodge roll | DODGE | Q |
| Attack / mine / place / use | ATTACK | Click (without dragging) or F |
| Look | Drag the right side | Drag the mouse; wheel to zoom |
| Interact / advance text | TALK / LOOK / TAKE button, or tap the text | E or Enter |
| Hotbar | Tap a slot | 1–6 (once James has joined you: mouse wheel) |
| Order companions | Companion button (JAMES) under your objectives, or walk up and tap ORDER | 1 Mine · 2 Explore · 3 Base · 4 Wander · 5 Follow · V picks which companion (or Everyone) |
| Build | BUILD button | B opens the build menu · F / click places · X stops building |
| Zoom (outside, once James has joined) | — | − / = |
| Inventory & crafting | Bag button | I or Tab |
| Earth map | Tap the minimap | M |
| Pause | ☰ button | Esc |

## Survival

- **Health and stamina:** sprinting, jumping, dodging and swinging cost stamina, which refills when you rest.
- **Movement and combat animations:**
  - **Sprint:** long strides, pumping arms and a hard forward lean, kicking up snow as you go.
  - **Block:** arms crossed in front of you behind a hexagonal suit shield. Attacks from the front do a quarter of their damage and cost 14 stamina each, with a knock-back. You move slowly and can't sprint while blocking, and blocking stops when your stamina runs out.
  - **Jetpack:** a twin-nozzle pack on your back. Hold jump in the air (or after stepping off a ledge) to thrust upwards with flame and smoke, leaning into the direction you're moving, and steer better than in a normal jump. Fuel (an orange bar under stamina) lasts about 3 seconds and refills on the ground.
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
  Each order gets a voiced reply from James (Chapters I and II; he has different lines when he rejoins you later). On a phone, tap **JAMES** under your objectives, or walk up to him and tap **ORDER**. He shows as a green dot on the minimap.
- **Voiced scenes:** the meeting cutscene (James and the soldier) and James's lines at the end of the trail are fully voiced with lip sync.
- **Main menu by chapter:**
  - **Chapter I to early Chapter IV:** the normal blue menu, the original theme, and the year 2125 AD.
  - **Chapter IV, after the time skip:** always blood red: every screen, from the main menu (all eight buttons included) to the in-game HUD, pause and inventory menus, uses the red interface, red night with falling ash, the Chapter IV theme, the year 2127 AD, a taunting voice, and a rewritten mission brief.
  - **Chapter V onwards:** back to the normal menu and the original theme, still in 2127 AD. **Settings → Menu style** lets you switch to Blood red (which brings back the Chapter IV theme and the voice).
  - To preview, add `?menu=ch4pre`, `?menu=ch4` or `?menu=ch5` to the game's address.
- **Main menu:** set in Antarctica at polar night, with aurora and snowfall; once James has joined you, he walks alongside your wanderer. The moon-style menu is kept for when the story reaches the Moon.
- **Options:** in the pause menu (and Settings on the main menu) you can turn the music on or off separately from all sound. Both choices are remembered.
- **Nostrapedia** (main menu): the in-game encyclopaedia. **Leaders** holds detailed files on the four species leaders. They are classified until Chapter III, except the leader of your wanderer's species, whose file opens once you have met them in your dream.
  **Companions** holds files on the people who travel with you. James Brown's file is open from Chapter I; the rest are redacted and open as the story continues (Chapter II, III or IV).
  **Ancient figures** is open from the start: history files on people you never meet in the game. They cover **Lord Sevirrus** (defeated in 1800 AD at Alphinos, capital city of Aridaxx), **Shakhak Chompjak** (founder of the Chompy Empire, c. 1.5 billion BC to 199,999,998 BC, victor over the Grob leader Javek at Steca) and **Lianna Erisconos** (mother of Vishara, Alexia and Nyrexia, former Grob Governor of Eris, c. 2.5 billion BC to 1 billion BC).
  **Terra Imperia** appears from Chapter III, with files on its leadership; one of them changes as the story moves through Chapters IV and V.
  Two further sections are **classified**: their files show only redaction bars until they are declassified in Chapter IV, after which they appear in full colour.
  **Creations** lists what you've made in Custom creations; full entries for them are coming soon.
- **Custom creations** (main menu): creator tools in the spirit of Spore's editors and Galactic Adventures. Creations are stored on this device separately from save slots, and are only saved when you press Save.
  - **Species creator:** build a creature with a live 3D preview (drag to rotate, scroll to zoom, Walk to see it move). You can set legs (0, 2, 4 or 6), leg length, arms, body length and width, tail, back spikes, neck, head, snout, 1–8 eyes, horns, ears, skin pattern (plain, stripes, spots, bands, scales), three colours, bioluminescence and size. Add lore: temperament, diet, homeworld and a description.
  - **Planet maker:** pick a preset (terran, ice, desert, ocean, volcanic, jungle, toxic or gas giant) and tune the seed, sea level, continents versus islands, mountains, size, colours, atmosphere, clouds, rings, moons, climate, gravity and life.
  - **Characters:** five ready-made characters from two games, each rigged automatically and armed: from *Project BC*, Josiah Richards (golden chains), Peter Chambers (rifle), Gareth Williams (dual pistols) and Kevin Murderhorn (black chains); from *Sevirrus*, Lord Sevirrus of Janira Prime (black sword, with a slasher-style neck snap). Each has a full biography, and you can preview Idle, Walk and Attack. You can also **upload your own .glb**: it's rigged automatically (using its skeleton if it has one, named arm/leg groups if it has those, or by splitting the model into head, arms and legs), and you can give it a name, weapon, height, description and the neck twitch. Uploads are stored in the browser's IndexedDB on this device.
  - **Adventure maker:** name and summarise an adventure, choose its planet (Earth or one of yours), set the difficulty and XP reward, cast up to 8 characters (Human, one of your species or any character, as ally, neutral or enemy, each with a line of dialogue), and write up to 8 acts with goals (reach, talk, collect, defeat, explore, survive), a target and story text. The preview shows your cast on the stage under your planet. Playing adventures comes in a later update.
- **Levels 1–100:** every wanderer earns XP and levels up from 1 to a maximum of 100. The level and XP bar sit above your objectives, and the level shows in the Wanderers list and on the main menu.
  - **XP from:** mining (rock 12, ice 10, crate 15; half when James mines), crafting (tools 30, everything else 20), placing builds (8), walking outside (1 per 40 m), hunting (skua 30, leopard seal 70, elephant seal bull 130; half when James makes the kill), and story moments (inspecting 15 each, talking to James 50, resting 100, stepping outside 50, the meeting 100, finding James 150, James joining 250).
  - **Each level:** +2 max health (298 at level 100), and a full heal on level up. Levels 20, 50 and 80 each add +1 mining damage.
  - XP needed per level grows from 200 (level 1→2) to about 70,000 (99→100); reaching level 10 takes about 7,400 XP, level 50 about 448,000, and level 100 about 2.7 million. Wanderers made before levels existed get XP for the story they've already played.
- **Antarctic wildlife:** the ice is no longer empty.
  - **Emperor penguins** (passive) waddle about in colonies of 6–12 and belly-slide away if you get too close or hit them. They can't be hurt.
  - **South polar skuas** circle overhead and dive-bomb you (6 damage).
  - **Leopard seals** hunt you on sight within about 20 m and bite hard (12 damage).
  - **Elephant seal bulls** are territorial: get within 9 m and they rear up and charge (20 damage), but they give up if you back off.
  Hostiles show as red dots on the minimap, have health bars once hit, and bring in the combat music. Dodging (Q) avoids a hit. James shoots at anything hostile near you with his rifle. If your health hits zero you black out and wake at the station with half health, keeping your items. Creatures drop **blubber** and **skua feathers**, used for two new recipes: the **Seal ration** (restores 25 health) and the **Insulated lining** (+20 max health while carried). The area around the station stays safe.
- **Minimap and Earth map:** outside, a heading-up minimap (top right) shows the terrain, the station, your beacons and a gold diamond on the current objective, with its distance. Tap it or press M for the full north-up Earth map with your coordinates.
- **Antarctica exploration music:** four tracks play while you're out on the ice, shuffled with quiet gaps of 9–25 seconds between them. The music fades when you go inside, softens during pauses and cutscenes, and steps aside for combat themes.
- **Combat themes:** five tracks (Predator I–IV and Wonders of Laniakea, combat version). In play, one is picked at random whenever something hostile engages you; it takes over from the ambient music and fades out a few seconds after the fight ends. You can preview them in Settings → Combat themes, where each tap plays the next track.
- **Held items:** whatever is selected in the hotbar (ice pick, med kit, thermal lamp, or a placeable) is shown in your right hand, positioned to fit your species.
- **Placeables:** select a placeable in the hotbar (lamp, wind barrier, heater, beacon) and a green preview appears in front of you; attack to place it. Walk up to it and press E (TAKE) to pick it back up.
- **Base building** (B, or the BUILD button): a No Man's Sky-style build menu.
  - **Pieces:** floor, wall, doorway, roof and ramp, each in **wood, stone, metal, obsidian or ice** (2–3 of that material per piece).
  - **Placement:** pieces snap to a 3 m grid. Walls and doorways sit on the grid lines, and turn to face the way you're facing. New pieces line up with the heights of what you've already built, so you can stack storeys: build a ramp, walk up it, and lay floors on top of your walls.
  - **Walking:** floors, roofs and ramps can be walked on, and walls block you. Doorways can be walked through. You can also land on and walk along the tops of walls and crafting tables, and if you ever end up inside a wall, rock or tree you can always walk back out.
  - **Changing your mind:** while building, walk up to a piece and press E (TAKE) to dismantle it for a full refund. The preview turns red when you can't place a piece, or can't afford it.
- **New materials:**
  - **Wood:** chop trees (2–4 each, +14 XP; James chops them too), or find it in supply crates.
  - **Obsidian:** from rare black volcanic glass outcrops. You need the ice pick selected to break them.
  - **Metal plate:** refined from 3 scrap metal at a crafting table.
- **Crafting table** (build menu → Structures): refined recipes (metal plates) and teleporters only work within 5 m of one. Inside the station counts as having one. Press E at a table to open crafting.
- **Merchants:** an Erisian trader keeps a stall on the ice (a pink diamond on the minimap). Press E to trade, selling resources for **Units** and buying materials, med kits and rations. Your Units balance shows in the inventory. Each planet the story reaches gets its own merchants.
- **Teleporters:** a teleporter pad stands outside the station, and you can build your own at any base (it needs a crafting table nearby). Every pad joins one network: step onto a pad and press E to pick a destination. You can rename your bases, and pads show as cyan rings on the minimap. Pads on other planets are listed under their planet, and you can reach them once the story takes you there by ship.
- **Nothing is lost between chapters:** your inventory, Units, everything you've built (stored per planet) and your companions' orders belong to the wanderer, not the chapter, so they carry into every chapter.
- **Commanding companions:** the companion panel and the 1–5 keys work for any companion in your party. With more than one companion, the panel shows who you're commanding; tap a name, choose Everyone, or press V to switch. James is the only companion who has joined so far; the others join in later chapters.
- What you mine and build is remembered per wanderer and saved with your save game.

## Repository layout

```
index.html                  the complete game, with all assets embedded
assets/models/              source 3D models (.glb); primes/, vectors/, companions/ and terra_imperia/ and ancient/ hold Nostrapedia figures; characters/ holds the Project BC and Sevirrus models, including hfos_soldier.glb (original HFOS colours)
assets/audio/               main menu themes (incl. Chapter IV), combat themes (combat/), Antarctica exploration music (antarctica/), opening narration, James Brown's lines (prologue + Chapter I)
assets/models/world/        HD rock and tree-bark models (embedded with JPEG textures in index.html)
assets/audio/storm/         exosuit warning (SUIT, SUIT2) and narrator lines (NARRATOR1–5) for the super blizzard
assets/textures/            HD Antarctica sky panorama and snow texture (embedded as JPEG in index.html)
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
