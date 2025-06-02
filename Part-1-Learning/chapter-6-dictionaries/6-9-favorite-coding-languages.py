fav_lang={'alex':['rust', 'javascript'], 'andy': ['react', 'svelte'], 'sarah':['c']}

for person, lang in fav_lang.items():
    if len(lang)==1:
        print(f'{person} is a loyal hoe to {lang}')
    
    else:
        print(f'{person} loves {lang} languages')
