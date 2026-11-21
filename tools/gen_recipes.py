#!/usr/bin/env python3
"""
Writes OverKnights' recipes: Knights & Heraldry's arms and armour made the Overgeared way.

Knights & Heraldry 1.2.0 (NeoForge 1.21.1) makes its gear on StoneyCore's craftsman anvil from hot iron and manuscripts.
Each of those recipes is replaced here, under the same id (data/knightsheraldry/recipe/craftmananvil/<name>.json), by:

- Overgeared forging (overgeared:forging) for everything hammered out of metal: weapon heads (heated steel, polished and
  quenched as Overgeared's own tool heads), helmet shells and armour parts (steel plates), and the pieces finished from a part
  and more hot iron. The forging minigame gives them their quality.
- Overgeared crafting (overgeared:crafting_shapeless) for what is put together from forged parts: a weapon from its head and
  haft, a helmet from its shell and lining, the golden and dark finishes, the smithing-hammer variants. It carries the parts'
  forging quality into the result and refuses parts that are still unpolished or unquenched, as Overgeared's own tools do.

Heraldic crests and cloth (plumes, chaperons, torses, beasts) are not smithing: their recipes are left to Knights & Heraldry.

Usage: gen_recipes.py <Knights & Heraldry 1.2.0 jar or its extracted data/knightsheraldry/recipe directory> <resources dir>
"""
import json
import os
import shutil
import sys
import zipfile

KH = 'knightsheraldry:'
OG = 'overgeared:'
OK = 'overknights:'

P = OG + 'steel_plate'
S = OG + 'heated_steel_ingot'
I = OG + 'heated_iron_ingot'
N = OG + 'steel_nugget'
C = OK + 'chainmail_mesh'
L = OK + 'leather_strip'
LP = OK + 'leather_patch'
WP = OK + 'woolen_patch'

# ---- Weapon heads: forged from heated steel (the pitchfork from iron), polished and quenched like Overgeared's tool heads.
# Every pattern differs from Overgeared's own (sword ['#','#'], axe ['##','# '], pickaxe ['###'], ...) and from each other.
HEADS = {
    'dagger_head': (['S', 'n'], 3),
    'stiletto_head': (['n', 'n', 'S'], 3),
    'sword_head': (['S', 'S', 'n'], 4),
    'rapier_head': (['n', 'S', 'S'], 4),
    'falchion_head': (['S ', 'SS'], 4),
    'longsword_head': (['S', 'S', 'S'], 5),
    'greatsword_head': ([' S ', ' S ', 'SSS'], 6),
    'axe_head': (['SS', 'SS'], 4),
    'halberd_head': (['SS ', 'SSS', ' S '], 6),
    'billhook_head': (['SS', 'S ', 'S '], 5),
    'hammer_head': (['SSS', ' n '], 5),
    'mace_head': (['nSn', 'nSn'], 5),
    'spear_head': ([' S ', 'nSn'], 4),
    'pitchfork_head': (['I I', 'III'], 3),
}

# ---- Helmet shells and armour parts: forged from steel plates ('P'), riveted with nuggets ('n').
PARTS = {
    'armet_piece': (['PPP', 'P P', 'nPn'], 5),
    'barbute_piece': (['PPP', 'PnP', 'P P'], 5),
    'bascinet_piece': ([' P ', 'PPP', 'P P'], 5),
    'burgonet_piece': (['PPP', 'P P', ' n '], 5),
    'cage_piece': (['PnP', 'n n', 'PnP'], 5),
    'close_helmet_piece': (['PPP', 'PnP', 'PPP'], 6),
    'frogmouth_piece': (['PP ', 'PPP', 'P P'], 5),
    'great_helmet_piece': (['PPP', 'PnP', 'PnP'], 6),
    'kettle_piece': ([' P ', 'PPP', 'n n'], 4),
    'maximilian_piece': (['PPP', 'nnn', 'P P'], 6),
    'morion_piece': (['nPn', 'PPP'], 4),
    'nasal_piece': (['PPP', 'PnP'], 4),
    'sallet_piece': (['PPP', 'P P', 'P  '], 5),
    'cuirass_piece': (['PnP', 'PPP', 'PPP'], 6),
    'harness_piece': (['PnP', 'P P'], 4),
    'spaulders_piece': (['PP', 'Pn'], 4),
    'tassets': (['P P', 'PnP'], 4),
    'besagews': ([' P ', 'PnP', ' P '], 3),
    'bevor': (['PnP', ' P '], 4),
    'aventail': (['CCC', 'C C'], 3),
    'falling_buffe': (['PPP', ' n '], 4),
    'rim_guards': (['PnP'], 3),
    'visor': (['n n', 'PPP'], 4),
    'greaves': (['P P', 'P P', 'n n'], 5),
    'sabatons': (['n n', 'P P'], 4),
    'plate_cuisses': (['PPP', 'P P', 'n n'], 6),
    'brigandine_cuisses': (['LPL', 'P P', 'L L'], 5),
    'plackart': (['nPn', 'PPP', 'PPP'], 6),
    'horse_barding': (['P P', 'PPP', 'PCP'], 7),
}

# ---- Pieces finished from a forged part ('X', 'Y') and more steel: forged again, the part on the anvil with the plates.
FINISHED = {
    'aragonese_sallet': ('sallet_bevor', None, 6),
    'great_armet': ('armet', None, 6),
    'great_armet_2': ('armet_2', None, 6),
    'great_bascinet': ('visored_bascinet', None, 6),
    'great_houndskul_bascinet': ('houndskull', None, 6),
    'houndskull': ('great_helmet_piece', None, 5),
    'plate_cuirass': ('cuirass_piece', None, 6),
    'plate_harness': ('gauntlet', None, 5),
    'plate_spaulders': ('spaulders_piece', None, 5),
    'viking_helm': ('nasal_piece', None, 4),
    'black_sallet': ('visorless_sallet', 'visor', 5),
}

# Heraldic crests and cloth: Knights & Heraldry's own recipes stay.
KEEP = {'black_horns', 'boar', 'dragon', 'eagle', 'gold_horns', 'lion', 'pegasus', 'snake', 'stag', 'unicorn', 'torse', 'plume',
        'chaperon', 'gilded_chaperon', 'teutonic_snakes', 'teutonic_black_snakes', 'teutonic_black_wings', 'teutonic_gold_wings',
        'teutonic_wings_ball_ends', 'teutonic_wings_sharp_ends'}

# Weapons held by a grip get a leather strip wound round it.
GRIPPED = {'sword', 'longsword', 'greatsword', 'dagger', 'stiletto', 'falchion', 'rapier', 'mace', 'hammer', 'axe'}
# Helmets put together from a shell, and gauntlets, get a lining.
HELMS = {'gauntlet', 'armet', 'barbute', 'bascinet', 'burgonet', 'cage', 'close_helm', 'frogmouth', 'great_helm', 'kettle_helm',
         'maximillian_helmet', 'morion', 'nasal_helm', 'visorless_sallet'}
# The arrows: an Overgeared arrowhead, a shaft and fletching (and what makes each kind).
ARROWS = {
    'bodkin_arrow': [OG + 'steel_arrow_head', 'minecraft:stick', 'minecraft:feather'],
    'broadhead_arrow': [OG + 'iron_arrow_head', 'minecraft:iron_nugget', 'minecraft:stick', 'minecraft:feather'],
    'swallowtail_arrow': [OG + 'steel_arrow_head', 'minecraft:flint', 'minecraft:stick', 'minecraft:feather'],
    'cloth_arrow': [OG + 'iron_arrow_head', '#minecraft:wool', 'minecraft:stick', 'minecraft:feather'],
}

MATERIALS = {'P': P, 'S': S, 'I': I, 'n': N, 'C': C, 'L': L}


def ingredient(name, **extra):
    if name.startswith('#'):
        value = {'tag': name[1:]}
    else:
        value = {'item': name}
    value.update(extra)
    return value


def forging(pattern, key, result, hammering, category, tool_head):
    recipe = {
        'type': OG + 'forging',
        'category': category,
        'hammering': hammering,
        'pattern': pattern,
        'key': {symbol: ingredient(item) for symbol, item in key.items()},
        'result': {'count': 1, 'id': result},
        'show_notification': False,
    }
    if not tool_head:
        # Armour as Overgeared's own: no polishing on the grindstone, no quenching.
        recipe['has_polishing'] = False
        recipe['need_quenching'] = False
    return recipe


def shapeless(ingredients, result, count=1, category='equipment'):
    return {
        'type': OG + 'crafting_shapeless',
        'category': category,
        'ingredients': [i if isinstance(i, dict) else ingredient(i) for i in ingredients],
        'result': {'count': count, 'id': result},
    }


def material_key(pattern):
    used = {c for row in pattern for c in row if c != ' '}
    return {c: MATERIALS[c] for c in used}


def stack_id(entry):
    stack = entry.get('stack', entry)
    return stack.get('id') or '#' + stack.get('tag', '')


def kh_ingredients(recipe):
    if 'ingredients' in recipe:
        return [stack_id(i) for i in recipe['ingredients']]
    return [stack_id(recipe['key'][c]) for row in recipe['pattern'] for c in row if c in recipe['key']]


def hammer():
    """A smithing hammer, given back a little worn: what turns a weapon into its variant."""
    return ingredient('#' + OG + 'smithing_hammers', remainder=True, durability_decrease=1)


def load_kh(source):
    recipes = {}
    if source.endswith('.jar'):
        with zipfile.ZipFile(source) as jar:
            for name in jar.namelist():
                if name.startswith('data/knightsheraldry/recipe/') and name.endswith('.json'):
                    recipes[name[len('data/knightsheraldry/recipe/'):-5]] = json.loads(jar.read(name))
    else:
        for root, _, files in os.walk(source):
            for f in files:
                if f.endswith('.json'):
                    path = os.path.join(root, f)
                    recipes[os.path.relpath(path, source)[:-5]] = json.load(open(path))
    return recipes


def main(source, resources):
    kh = load_kh(source)
    out = {}
    anvil = {k[len('craftmananvil/'):]: v for k, v in kh.items() if k.startswith('craftmananvil/')}

    for name, (pattern, hammering) in HEADS.items():
        out['knightsheraldry/recipe/craftmananvil/' + name] = forging(pattern, material_key(pattern), KH + name, hammering,
                                                                     'TOOL_HEADS', True)
    for name, (pattern, hammering) in PARTS.items():
        out['knightsheraldry/recipe/craftmananvil/' + name] = forging(pattern, material_key(pattern), KH + name, hammering,
                                                                     'ARMORS', False)
    for name, (base, second, hammering) in FINISHED.items():
        if second:
            pattern, key = [' Y ', 'PXP'], {'P': P, 'X': KH + base, 'Y': KH + second}
        else:
            pattern, key = [' P ', 'PXP'], {'P': P, 'X': KH + base}
        out['knightsheraldry/recipe/craftmananvil/' + name] = forging(pattern, key, KH + name, hammering, 'ARMORS', False)
    for name, parts in ARROWS.items():
        count = anvil.get(name, {}).get('result', {}).get('count', 1)
        out['knightsheraldry/recipe/craftmananvil/' + name] = shapeless(parts, KH + name, max(count, 2))

    for name, recipe in sorted(anvil.items()):
        key = 'knightsheraldry/recipe/craftmananvil/' + name
        if key in out or name in KEEP or recipe['type'] != 'stoneycore:craftman_anvil_crafting':
            continue
        result = recipe['result']['id']
        short = result.split(':')[1]
        parts = [i for i in kh_ingredients(recipe) if i != 'minecraft:sand']
        if 'stoneycore:hot_iron' in parts:
            raise SystemExit('No forging recipe designed for ' + name + ': ' + str(parts))
        # Overgeared's own materials where Knights & Heraldry used vanilla ones for the smithing.
        parts = [C if i == 'minecraft:chain' else L if i == 'minecraft:leather' else i for i in parts]
        if short.startswith('poleaxe'):
            parts = parts + [N]
        if short in GRIPPED:
            parts = parts + [L]
        if short in HELMS:
            parts = parts + [LP]
        if len(parts) == 1 and parts[0].startswith(KH) and short not in HELMS:
            # One weapon or piece made into another (a hammer into a war hammer): with a smithing hammer, as the variants.
            parts = [parts[0], hammer()]
        out[key] = shapeless(parts, result, recipe['result'].get('count', 1))

    # The smithing-hammer variants (a sword into a v-sword...) and the add-ons put on with the hammer.
    for name, recipe in sorted(kh.items()):
        if '/' in name or recipe.get('type') != 'stoneycore:craftman_anvil_crafting':
            continue
        parts = [i for i in kh_ingredients(recipe) if i != 'minecraft:sand']
        if name.startswith('upgrade_'):
            parts = parts + [hammer()]
        out['knightsheraldry/recipe/' + name] = shapeless(parts, recipe['result']['id'], recipe['result'].get('count', 1))

    # OverKnights' own parts.
    shears = ingredient('minecraft:shears', remainder=True, durability_decrease=1)
    out['overknights/recipe/leather_strip'] = shapeless(['minecraft:leather', shears], L, 4, 'misc')
    out['overknights/recipe/leather_from_patch'] = shapeless([LP, shears], 'minecraft:leather', 2, 'misc')
    out['overknights/recipe/leather_patch'] = {
        'type': 'minecraft:crafting_shaped', 'category': 'misc', 'pattern': ['#S', 'S#'],
        'key': {'#': {'item': 'minecraft:leather'}, 'S': {'item': 'minecraft:string'}}, 'result': {'count': 1, 'id': LP}}
    out['overknights/recipe/woolen_patch'] = {
        'type': 'minecraft:crafting_shaped', 'category': 'misc', 'pattern': ['#S', 'S#'],
        'key': {'#': {'tag': 'minecraft:wool'}, 'S': {'item': 'minecraft:string'}}, 'result': {'count': 2, 'id': WP}}
    out['overknights/recipe/chainmail_mesh'] = {
        'type': OG + 'forging', 'category': 'misc', 'hammering': 3, 'has_quality': False, 'need_quenching': False,
        'has_polishing': False, 'pattern': ['##', '##'], 'key': {'#': {'item': 'minecraft:chain'}},
        'result': {'count': 1, 'id': C}, 'show_notification': True}

    # Two forging recipes on the same anvil must never look alike: the same pattern with the same materials.
    seen = {}
    for path, recipe in out.items():
        if recipe['type'] != OG + 'forging':
            continue
        signature = (tuple(recipe['pattern']), tuple(sorted((k, json.dumps(v, sort_keys=True)) for k, v in recipe['key'].items())))
        if signature in seen:
            raise SystemExit('Same forging pattern for ' + seen[signature] + ' and ' + path)
        seen[signature] = path

    # The heads are tool parts to Overgeared (its book tabs, its traders' quality).
    tags = {'overgeared/tags/item/tool_parts': {'replace': False, 'values': [KH + h for h in HEADS]}}

    data = os.path.join(resources, 'data')
    for folder in ('knightsheraldry', 'overknights', 'overgeared'):
        shutil.rmtree(os.path.join(data, folder), ignore_errors=True)
    for path, value in {**out, **tags}.items():
        file = os.path.join(data, path + '.json')
        os.makedirs(os.path.dirname(file), exist_ok=True)
        with open(file, 'w') as f:
            json.dump(value, f, indent=2)
            f.write('\n')
    counts = {}
    for recipe in out.values():
        counts[recipe['type']] = counts.get(recipe['type'], 0) + 1
    print(len(out), 'recipes', counts)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
