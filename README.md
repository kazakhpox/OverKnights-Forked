# OverKnights (NeoForge 1.21.1)

A fork of [OverKnights](https://github.com/phuccom000/Overgeared-Knights) by StirDrem, ported from Forge 1.20.1 to
**NeoForge 1.21.1** and to Knights & Heraldry's current item set. It brings
[Overgeared](https://modrinth.com/mod/overgeared)'s smithing to [Knights & Heraldry](https://modrinth.com/mod/knights-and-heraldry):
its arms and armour are forged on Overgeared's anvils instead of hammered out of hot iron on StoneyCore's craftsman anvil.

- **Weapons** (new: the released OverKnights had none). Every head is forged from heated steel ingots, each with its own
  pattern, and has to be polished on the grindstone and quenched like Overgeared's own tool heads. A weapon is then put
  together on a crafting table from its head and haft (sticks or logs; a leather strip round the grip of swords, daggers,
  maces, hammers and axes) and takes the head's forging quality. The variants (sword into v-sword, hammer into war hammer...)
  are made with a smithing hammer, keeping the quality. The poleaxe is the halberd head on a haft with a steel spike.
- **Armour.** Helmet shells, cuirass, harness, spaulders and the other parts are forged from steel plates riveted with steel
  nuggets; the pieces finished with more steel (great armet, plate cuirass, plate harness...) are forged with their part on
  the anvil. Helmets and gauntlets are put together from their shell with a leather lining, the golden and dark finishes on a
  crafting table: all keep the forging quality, which raises or lowers the armour as Overgeared's quality does.
- **Arrows**: an Overgeared arrowhead, a stick and a feather (bodkin: steel; broadhead: iron with a nugget; swallowtail: steel
  with flint; cloth: iron with wool).
- **Its own parts**: chainmail mesh (forged from chains; it replaces chains in mail), leather strips (leather cut with shears)
  and patches, woollen padding.
- Heraldic crests, plumes, chaperons and other cloth keep Knights & Heraldry's own recipes.

The recipes are written by `tools/gen_recipes.py` from Knights & Heraldry 1.2.0's own: every one of its craftsman-anvil
smithing recipes is replaced under the same id, so nothing of it is left to make from hot iron.

## Download

The jar is on the [Releases](https://github.com/kazakhpox/OverKnights-Forked/releases) page (built by
`.github/workflows/release.yml` from `mod_version`).

## Requirements

| | Version |
|---|---|
| Minecraft | 1.21.1 |
| NeoForge | 21.1.253 or newer |
| Overgeared | 1.21.1-1.7.0 or newer |
| Knights & Heraldry | 1.2.0 (NeoForge) and its StoneyCore |

Install on the client and on the server.

## Weapon heads

| Result | Pattern | Key | Blows |
|---|---|---|---|
| axe_head | `SS / SS` | S heated_steel_ingot | 4 |
| billhook_head | `SS / S· / S·` | S heated_steel_ingot | 5 |
| dagger_head | `S / n` | S heated_steel_ingot, n steel_nugget | 3 |
| falchion_head | `S· / SS` | S heated_steel_ingot | 4 |
| greatsword_head | `·S· / ·S· / SSS` | S heated_steel_ingot | 6 |
| halberd_head | `SS· / SSS / ·S·` | S heated_steel_ingot | 6 |
| hammer_head | `SSS / ·n·` | S heated_steel_ingot, n steel_nugget | 5 |
| longsword_head | `S / S / S` | S heated_steel_ingot | 5 |
| mace_head | `nSn / nSn` | S heated_steel_ingot, n steel_nugget | 5 |
| pitchfork_head | `I·I / III` | I heated_iron_ingot | 3 |
| rapier_head | `n / S / S` | S heated_steel_ingot, n steel_nugget | 4 |
| spear_head | `·S· / nSn` | S heated_steel_ingot, n steel_nugget | 4 |
| stiletto_head | `n / n / S` | S heated_steel_ingot, n steel_nugget | 3 |
| sword_head | `S / S / n` | S heated_steel_ingot, n steel_nugget | 4 |

`S` heated steel ingot, `I` heated iron ingot, `n` steel nugget; `·` an empty cell. Shapes may be mirrored.

## Armour parts

| Result | Pattern | Key | Blows |
|---|---|---|---|
| aragonese_sallet | `·P· / PXP` | P steel_plate, X sallet_bevor | 6 |
| armet_piece | `PPP / P·P / nPn` | P steel_plate, n steel_nugget | 5 |
| aventail | `CCC / C·C` | C chainmail_mesh | 3 |
| barbute_piece | `PPP / PnP / P·P` | P steel_plate, n steel_nugget | 5 |
| bascinet_piece | `·P· / PPP / P·P` | P steel_plate | 5 |
| besagews | `·P· / PnP / ·P·` | P steel_plate, n steel_nugget | 3 |
| bevor | `PnP / ·P·` | P steel_plate, n steel_nugget | 4 |
| black_sallet | `·Y· / PXP` | P steel_plate, X visorless_sallet, Y visor | 5 |
| brigandine_cuisses | `LPL / P·P / L·L` | L leather_strip, P steel_plate | 5 |
| burgonet_piece | `PPP / P·P / ·n·` | P steel_plate, n steel_nugget | 5 |
| cage_piece | `PnP / n·n / PnP` | P steel_plate, n steel_nugget | 5 |
| close_helmet_piece | `PPP / PnP / PPP` | P steel_plate, n steel_nugget | 6 |
| cuirass_piece | `PnP / PPP / PPP` | P steel_plate, n steel_nugget | 6 |
| falling_buffe | `PPP / ·n·` | P steel_plate, n steel_nugget | 4 |
| frogmouth_piece | `PP· / PPP / P·P` | P steel_plate | 5 |
| great_armet | `·P· / PXP` | P steel_plate, X armet | 6 |
| great_armet_2 | `·P· / PXP` | P steel_plate, X armet_2 | 6 |
| great_bascinet | `·P· / PXP` | P steel_plate, X visored_bascinet | 6 |
| great_helmet_piece | `PPP / PnP / PnP` | P steel_plate, n steel_nugget | 6 |
| great_houndskul_bascinet | `·P· / PXP` | P steel_plate, X houndskull | 6 |
| greaves | `P·P / P·P / n·n` | P steel_plate, n steel_nugget | 5 |
| harness_piece | `PnP / P·P` | P steel_plate, n steel_nugget | 4 |
| horse_barding | `P·P / PPP / PCP` | C chainmail_mesh, P steel_plate | 7 |
| houndskull | `·P· / PXP` | P steel_plate, X great_helmet_piece | 5 |
| kettle_piece | `·P· / PPP / n·n` | P steel_plate, n steel_nugget | 4 |
| maximilian_piece | `PPP / nnn / P·P` | P steel_plate, n steel_nugget | 6 |
| morion_piece | `nPn / PPP` | P steel_plate, n steel_nugget | 4 |
| nasal_piece | `PPP / PnP` | P steel_plate, n steel_nugget | 4 |
| plackart | `nPn / PPP / PPP` | P steel_plate, n steel_nugget | 6 |
| plate_cuirass | `·P· / PXP` | P steel_plate, X cuirass_piece | 6 |
| plate_cuisses | `PPP / P·P / n·n` | P steel_plate, n steel_nugget | 6 |
| plate_harness | `·P· / PXP` | P steel_plate, X gauntlet | 5 |
| plate_spaulders | `·P· / PXP` | P steel_plate, X spaulders_piece | 5 |
| rim_guards | `PnP` | P steel_plate, n steel_nugget | 3 |
| sabatons | `n·n / P·P` | P steel_plate, n steel_nugget | 4 |
| sallet_piece | `PPP / P·P / P··` | P steel_plate | 5 |
| spaulders_piece | `PP / Pn` | P steel_plate, n steel_nugget | 4 |
| tassets | `P·P / PnP` | P steel_plate, n steel_nugget | 4 |
| viking_helm | `·P· / PXP` | P steel_plate, X nasal_piece | 4 |
| visor | `n·n / PPP` | P steel_plate, n steel_nugget | 4 |

`P` steel plate, `n` steel nugget, `C` chainmail mesh, `L` leather strip, `X`/`Y` the piece being finished.

## Building

```bash
./gradlew build
```

`python3 tools/gen_recipes.py <knightsheraldry-neoforge-1.21.1-1.2.0.jar> src/main/resources` writes the recipes again (for
another Knights & Heraldry version). `./gradlew runCheck` (dev only) starts a server with all the mods and checks that every
recipe loaded.

## License

MIT, as the original OverKnights by StirDrem. Its item textures are kept.
