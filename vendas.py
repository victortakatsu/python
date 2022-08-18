import time
print('-------------------------------')
print('-------------------------------')
meta = 15000
nome = input('Olá! Por favor, digite seu nome: ')
print('-------------------------------')
vendas = input('Pronto, {}. Agora insira o valor total de suas vendas: '.format(nome))

if vendas != '':
    vendas = float(vendas)
    time.sleep(1)
    print('---------------------------------------')
    print('Ok, verificando as informações. Aguarde, por favor.')
    print('---------------------------------------')
    time.sleep(3)
    if vendas >= (meta * 2):
        bonus = 0.07 * vendas
        print('Uau! {}, você vendeu mais que o dobro da meta deste mês! Você receberá um bônus de R$ {:.2f}.'.format(nome, bonus))
    elif vendas >= meta:
        bonus = 0.03 * vendas
        print('Parabéns {}! Suas vendas alcançaram a meta desse mês. Você receberá um bônus de R$ {:.2f}.'.format(nome, bonus))
    else:
        print('Poxa, {}. Dessa vez não vai rolar aquele bônus. Continue se empenhando para garanti-lo no próximo mês!'.format(nome))
else:
    print('Preencha o campo de vendas corretamente.')
