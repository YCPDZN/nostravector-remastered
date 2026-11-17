import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
import json
exec(open('t1.py').read()); exec(open('t2.py').read()); exec(open('t3.py').read()); exec(open('c1.py').read()); exec(open('c2.py').read()); exec(open('q.py').read()); exec(open('x.py').read())
def cnt(d): return sum(len(v) for x in d.values() for v in (x.values() if isinstance(x, dict) else [x]))
def qcnt():
    n=0
    for q in Q.values():
        for part in ('ask','yes','no','reply'):
            if part in q:
                for m in ('talk','chat'):
                    v=q[part][m]; n += sum(len(a) for a in v.values()) if isinstance(v,dict) else len(v)
    return n
print('talk', cnt(T), 'chat', cnt(C), 'questions', qcnt(), 'intents', len(T), len(C))
print('missing in chat', sorted(set(T)-set(C)), 'missing in talk', sorted(set(C)-set(T)))
# after which topics they ask a question back
A = {'greet': ['howru2'], 'missed': ['howru2'], 'back': ['howru2'], 'howru': ['howru'], 'whatsup': ['howru', 'bored'], 'hobby': ['hobby'], 'fav_food': ['food'], 'fav_music': ['music'], 'fav_color': ['color'], 'fav_place': ['fav_place'], 'from': ['from'],
     'ship': ['ship'], 'gear': ['fight'], 'guild': ['guild'], 'pets': ['pet'], 'dream': ['dream'], 'fear': ['fear'], 'joke': ['joke'], 'drink': ['drink'], 'bored': ['bored'], 'whattodo': ['bored'],
     'newplayer': ['long'], 'friends': ['friends'], 'meet': ['long', 'explore'], 'space': ['explore'], 'fu_ack': ['explore', 'hobby', 'fav_place', 'food', 'pet', 'drink', 'dream'], 'fu_laugh': ['joke'],
     'ans_good': ['hobby', 'explore', 'bored'], 'ilike': ['hobby', 'fav_place', 'food'], 'job': ['hobby'], 'level': ['fight'], 'mining': ['explore'], 'unknown': ['tellmore'], 'nm': ['bored', 'hobby', 'explore'], 'family': ['from'], 'weather': ['explore'], 'achieve': ['fight']}
open(__import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..', '..', 'data', 'resConvo.js'), 'w', encoding='utf-8').write('/* Residents in conversation: what they say to what you say, face to face (talk) and in the chat or a whisper (chat), by alignment (h hero, n neutral, v villain); the questions they ask you back (q) and after which topics (after). Read by resConvo() in index.html. */\nwindow.NV_RES_CONVO=' + json.dumps({'talk': T, 'chat': C, 'q': Q, 'qv': QV, 'after': A}, ensure_ascii=False, separators=(',', ':')) + ';\n')
