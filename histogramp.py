import wordcount

def f3(lst):
    # count total number of words
    total = 0
    for cnt, label in lst:
        total += cnt

    # produce a histogram
    for cnt, label in lst:
        print(label.ljust(15), "\t[", sep='', end='')
        per = int(cnt) * 100 // total
        for i in range(0, per, 5):
            print("*", sep='', end='')
        print("] ", per, "%", sep='')


def main(file):

    dict = wordcount.f1(file)

    lst = wordcount.f2(dict)

    f3(lst)


f = "test.txt"
main(f)