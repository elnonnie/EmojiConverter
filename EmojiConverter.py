if __name__ == '__main__':
    
    emoji_assignment = {'😂': '[LOL]'}

    text = 'Wetin be this? 😂'
    text_tokens = text.split(' ')
    print(text_tokens)
    
    new_text = ''
    for item in text_tokens:
        if item in emoji_assignment:
            new_text += ' ' +emoji_assignment[item]
        else:
            new_text += ' ' + item

    print(new_text)