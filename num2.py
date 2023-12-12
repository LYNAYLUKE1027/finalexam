def solution(letter) :
    morse = {'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    answer = ''
    alpha = letter.split(' ')
    for i in alpha:
        answer += morse[i]
    return answer.lower()

letter = "-. --- .--. .- .. -. -. --- --. .- .. -."
#no pain, no gain
result = solution(letter)
print(result)