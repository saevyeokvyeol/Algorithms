def solution(numbers):
    dic = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    for k in dic.keys():
        numbers = numbers.replace(k, dic[k])
    return int(numbers)