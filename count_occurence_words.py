def freq(str):
    str = str.split()
    str2 =[]

    for i in str:
        if i not in str2:
            str2.append(i)
    for i in range(0,len(str2)):
        print('Frequency of ',str2[i],' is :',str.count(str2[i]))            

def main():
    str = 'AUBAID AUBAID ZAINUL AUBAID JAHANGIR JAHANGIR ZAINUL JANII JANII FAISEL'
    freq(str)
if __name__ == "__main__":
    main()