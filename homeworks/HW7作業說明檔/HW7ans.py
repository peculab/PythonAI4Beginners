import jieba
from collections import Counter
import jieba.analyse
text = """
隋末民間動亂削弱了隋朝的軍事實力，而導致突厥崛起，成為中原一帶強大的勢力，藉此對中原形成巨大壓力。
而李淵在起兵反隋時，由於意識自身力量不足，依劉文靜建議，決定借助突厥的支持，以財帛金寶作為借兵的交換條件，
從而增強反隋的實力。而若根據《舊唐書》記載可以發現到，李淵起兵時兵源有限，因此決定「財帛金寶入突厥」以求借兵，
並借用胡騎作為援兵。此外，在突厥的統治者中像是始畢可汗、處羅可汗等相繼去世後，李淵也罷朝致哀，並「詔百官就館吊其使」。
而從《資治通鑑》中亦記載：「劉文靜勸李淵與突厥相結，資其士馬以益兵勢。淵從之，自以卑辭厚禮，遺始畢可汗。」。
所以，可以反映出唐初為應對內外壓力而採取的妥協策略。而陳寅恪曾在《論唐高祖稱臣於突厥事》中提出唐高祖李淵曾向突厥稱臣的說法，
而李樹桐撰寫《唐高祖稱臣於突厥考辯》以後，根據封號使用問題、對突厥使用「啓」字、史官紀載之過以及稱臣紀錄不存在等方面，
反駁了陳寅恪的觀點。兩者基於對史料的不同解讀，揭示出學者對同一歷史事件的不同詮釋。
因此，針對唐朝建國初期面對強大突厥勢力的複雜抉擇及其學術爭論，本研究將深入探討李淵與突厥之間的關係及其對唐朝建立的影響，
並分析學術界長期辯論的原因及意義。這不僅有助於理解唐朝初期的外交策略，亦為唐史研究提供新視角。
陳寅恪認為隋末中國北方群雄多臣於突厥，或受其封號，或得具突厥圖騰的狼頭纛，唐高祖亦不例外，且稱臣突厥之主謀實為唐太宗與劉文靜，
而後李唐欲改稱臣突厥的立場，故殺劉文靜。陳寅恪先以太宗欲改白旗、符讖和興國寺兵脅高祖證之，言起兵時的絳白旗一方面欲以絳色示初時擁立隋幼主的立場，
另方面表示其不純服於突厥，並以「童子木上懸白旗，胡兵紛紛滿前後」，證白旗為突厥之旗色，再論太宗與突厥有和突利結香火之盟的特殊關係，故突厥視太宗為其部落之人。
李樹桐認為高祖未稱臣的論點有四，其一為高祖不稱天子表示其未受突厥封號，也未稱臣，且當時情勢並不危急，無稱臣之必要；其二高祖致書突厥用啓字為政治操作；
其三記載高祖稱臣之紀錄為史官欲討太宗喜所寫，因修史者缺乏史德，素有「誣高祖之惡，溢太宗之美」之舉，且高祖與太宗間有嫌隙，其晚景淒涼，故當朝史官多抹黑高祖以悅太宗，
而李樹桐以記載高祖稱臣與太宗渭水之恥的時間點推論史官欲以高祖誠稱臣掩太宗的渭水之恥，此亦符合史官一貫貶高祖的敘事筆法，若真稱臣當為國恥，豈會不察而錄；其四因未有稱臣與結束稱臣的紀錄，故未稱臣。
"""
text = text.replace("\n", "")

stop_words = set(['所以', '好', '因為', '；', '的', '是', '了', '欲', '也', '在', '和', '就', '不', '有',
                 '以', '與', '、', '為', '這個', '而', '「', '」', '，', '。', '《', '》', "對", "於", "\n"])

custom_dict = [
    '陳寅恪',
    "渭水之恥",
    "論唐高祖稱臣於突厥事",
    "資治通鑑",
    "舊唐書"# 直接添加词汇
]

for word in custom_dict:
    jieba.add_word(word)

words = jieba.lcut(text)

filtered_words = [word for word in words if word not in stop_words]

word_count = Counter(filtered_words)

filtered_word_count = {word: count for word, count in word_count.items() if count > 1}

sorted_filtered_word_count = sorted(filtered_word_count.items(), key=lambda x: x[1], reverse=True)

keywords = jieba.analyse.extract_tags(text, topK=10)

sentences = text.split('。')

top_sentences = sorted(sentences, key=lambda x: sum(1 for word in jieba.cut(x) if word in keywords), reverse=True)[:3]

summary = '。'.join(top_sentences).replace("\n", "")
print(summary)
print("-----")
print(''.join(keywords))
print("-----")
print(sorted_filtered_word_count)
