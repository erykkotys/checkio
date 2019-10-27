def is_stressful(subj):
    if subj.isupper():
        return True
    if subj.endswith('!!!'):
        return True
    for i in range(len(subj)):
        if subj[i] == subj[i-1] == subj[i-2] and subj[i-2:i].isupper():
            return True
    subj_formatted = subj.lower().replace('-', '').replace('!','').replace('.','')
    for word in ['asap', 'help', 'urgent']:
        if word in subj_formatted:
            return True
# all(i in fdhash for (i for i in ('asa', 'sada')
    else:
        return False

print(is_stressful('HELP'))
print(is_stressful('h-el-p'))
print(is_stressful('where are you?!!!!'))
print(is_stressful('HELP'))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')