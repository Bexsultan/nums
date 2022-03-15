#problem1
a = 'Google создаст специальную команду для поиска багов в особо важных приложениях.'
b = a.split()
print(len(b))

#problems2
a = "У вас есть строка'Запуск Ethereum 2.0 состоится 1 декабря. На депозитный контракт внесено более 524 288 ETH "
b = a.split()
print(type(a))

#problem3
a = 'хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
b = (a.title())
print(b)

#problem4
a = input('Напиши любой символ: ')
b = 'GitHub'
print(a.join(b))

#problem5
a = 'Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем'
b = a.replace('е','3')
print(b)

#Exrta_Problem1
a = 'beksultano'
first = a[:int(len(a) / 2)].lower()
second =  a[int(len(a) / 2):].upper()
print(first + second)

#Extra_Problem2
a=True
print(str(a))
