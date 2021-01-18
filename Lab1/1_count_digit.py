# Write a program to count number of significant digits in a given number.

def count_sig_figs(digits):
    '''Return the number of significant figures of the input digit string'''
    sig_fig_count = 0
    for index, digit in enumerate(digits):
        if digit == ".":
            continue
        if digit != '0':
            sig_fig_count += 1
        else:
            sig_fig_count += check_zero_sig(index, digits, sig_fig_count)
    return sig_fig_count

def check_zero_sig(index, digits, sig_fig_count):
    '''
    Returns if a zero digit at a given position is significant,
    given a count of significant digits preceding it.
    '''
    if not sig_fig_count:
        return False
    try:
        decimal = digits.index('.')
    except ValueError:
        return any(digit != '0' for digit in digits[index+1:])
    else:
        return index > decimal

print(count_sig_figs('0.0001234')) # 4 sig fig
print(count_sig_figs('3.50')) # 3 sig fig
print(count_sig_figs('0.001234')) # 4 sig fig
print(count_sig_figs('0.01234')) # 4 sig figs
print(count_sig_figs('65.0')) # 3 sig figs
print(count_sig_figs('0.230')) # 3 sig figs

