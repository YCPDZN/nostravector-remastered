import os, json, glob, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
KB = []
def E(names, *s): KB.append({'n': [a.strip() for a in names.split('|') if a.strip()], 's': list(s)})
for f in sorted(glob.glob('k*.py')): exec(open(f, encoding='utf-8').read())
exec(open('frame.py', encoding='utf-8').read()) if os.path.exists('frame.py') else None
n = sum(len(e['s']) for e in KB); seen = {}
for e in KB:
    for a in e['n']:
        if a in seen: print('dup alias', a, seen[a], e['n'][0])
        seen[a] = e['n'][0]
fr = globals().get('FRAME', {})
print('entries', len(KB), 'sentences', n, 'frame', sum(len(v) for v in fr.values()))
open('../../../data/resKnow.js', 'w', encoding='utf-8').write('/* What residents know about real-world history and people, for whispers: each entry is a list of names, then sentences (summary, when, details, legacy). Built by nightmare/tools/res_know/build.py. */\nwindow.NV_RES_KNOW=' + json.dumps({'kb': KB, 'frame': fr}, ensure_ascii=False, separators=(',', ':')) + ';\n')
