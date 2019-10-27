def is_stressful(subj):
    if subj.isupper():
        return True

# all(i in fdhash for (i for i in ('asa', 'sada')
        return True
    else:
        return False

print(is_stressful('HELP'))
print(is_stressful('h-el-p'))
print(is_stressful('fjsahkfjhsa'))
print(is_stressful('HELP'))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')