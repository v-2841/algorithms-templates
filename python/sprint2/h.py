def is_correct_bracket_seq(seq):
    seq = list(seq)
    temp = []
    while seq:
        if not temp or seq[0] == '(' or seq[0] == '{' or seq[0] == '[':
            temp.append(seq[0])
            seq.pop(0)
        else:
            if (seq[0] == ')' and temp[-1] == '(' or
                seq[0] == ']' and temp[-1] == '[' or
                    seq[0] == '}' and temp[-1] == '{'):
                seq.pop(0)
                temp.pop(-1)
            else:
                return False
    if temp:
        return False
    return True


print(is_correct_bracket_seq(input()))
