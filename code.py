hard_vowels = []
soft_vowels = []

def vowel_extraction(text):
    hard = ["a", "ı", "o", "u"]
    soft = ["e", "ə", "i", "ö", "ü"]

    for i in text:
        if i in hard:
            hard_vowels.append(i)
        elif i in soft:
            soft_vowels.append(i)
        else:
            pass
    
    print(len(hard_vowels), len(soft_vowels))
