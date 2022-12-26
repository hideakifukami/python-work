"""JuuKyuu, by Hideaki Fukami
Um jogo onde você recebe dicas e a partir delas precisa descobrir do que se trata."""

import random

# Lista de Coisas:
torneira = [
    'Posso ser de plástico mas geralmente sou de ferro.',
    'As pessoas geralmente me utilizam todos os dias.',
    'Posso estar em mais de um cômodo das casas. As vezes até mesmo fora delas.',
    'Tenho uma função muito específica.',
    'Meu uso muitas vezes é relacionado à limpeza.',
    'Geralmente estou perto de uma pia.',
    'Meu uso tem relação com água.',
    'Perca sua vez.',
    'Avance duas casas.',
    'Volte uma casa.'
]
notebook = [
    'Me diferencio do meu "irmão" pela praticidade em ser carregado para vários lugares.',
    'Posso ser dos mais simples até os mais refinados.',
    'Pessoas me utilizam pra trabalho, estudo, entretenimento, etc. Muitos não ficam sem mim.',
    'Sou composta por muitas partes, uma delas é a tela.',
    'Preciso de comandos para que eu possa funcionar.',
    'Entre muitas das minhas utilidades, uma delas é poder acessar a internet.',
    'Sou sempre acompanhado de um teclado.',
    'Perca sua vez.',
    'Avance duas casas.',
    'Volte uma casa.'
]
torradeira = [
    'Sirvo para preparar um alimento em específico.',
    'No Brasil não sou tão popular, e a maioria prefere usar uma frigideira ou um forno ao invés de mim.',
    'Geralmente me utilizam no café da manhã.',
    'O que é feito em mim muitas vezes acompanha ovos ou manteiga.',
    'Sou um eletrodoméstico e fico na cozinha.',
    'Sou prática por fazer o preparo sem precisar de supervisão.',
    'Quando presente, geralmente fico em uma bancada.',
    'Perca sua vez.',
    'Avance duas casas',
    'Volte uma casa.'
]
mesa = [
    'Sou um objeto presente no cotidiano de muitas pessoas.',
    'Muitas vezes sou feita de madeira, mas existem algumas variações.',
    'Sou utilizada de manhã, a tarde e a noite.',
    'As pessoas se reunem em minha volta em muitos encontros.',
    'Estou em cozinhas, salas e escritórios.',
    'Em muitos países, ao me utilizarem, usa-se também uma cadeira.',
    'Já ouvi muita conversa.',
    'Perca sua vez.',
    'Avance duas casas',
    'Volte uma casa.'
]
cafe = [
    'Sou um grão mas quase ninguém me conhece dessa forma.',
    'Geralmente sou consumido de forma líquida.',
    'Meu gosto é intenso mas muitos não vivem sem mim.',
    'Ajudo aqueles que não conseguem dormir.',
    'O Brasil tem muito impacto no meu mercado de vendas.',
    'Não tenho a cor escura por natureza, mas no processo de preparo para o consumo fico bem torrado.',
    'Sou ótimo para acompanhar um bom pão na chapa.',
    'Perca sua vez.',
    'Avance duas casas.',
    'Volte uma casa.'
]
copo = [
    'Posso ser de vidro, plástico, alumínio e até algumas coisas mais exóticas.',
    'Geralmente sirvo para receber líquidos.',
    'Fico na cozinha, muitas vezes dentro de armários.',
    'Também posso ser usado como unidade de medida para receitas.',
    'Estou presente em alguns ditados populares.',
    'Em restaurantes muitas vezes me pedem junto à gelo e limão.',
    'Meu uso se faz ao me levar à boca.',
    'Perca sua vez.',
    'Avance duas casas.',
    'Volte uma casa.'
]
salgadinho = [
    'Geralmente sou feito de milho.',
    'Sou um ótimo acompanhamento para um refrigerante e um filme.',
    'Sou comprado no mercado, dentro de uma embalagem.',
    'Possuo diversos sabores e marcas, com grandes diferenças entre elas.',
    'Sou considerado junk food.',
    'Quando sou aberto todo mundo do ambiente sabe que fui aberto, pelo cheiro e pelo barulho da embalagem.',
    'Muitas vezes considerado comida de criança.',
    'Perca sua vez.',
    'Avance duas casas.',
    'Volte uma casa.'
]
chocolate = [
    'Posso ser bem doce mas também posso ser bem amargo.',
    'Apenas de não ser tão comum, também posso ser utilizado em comidas salgadas e vou bem com carne de caça.',
    'Existe uma categoria de pessoas que são viciadas em mim.',
    'Estou presente como ingrediente de muitos doces, mas também posso ser consumido sozinho.',
    'Meu consumo faz com que o cérebro libere hormônios do prazer.',
    'Uma combinação exótica minha, mas muito conhecida, é com pimenta.',
    'Tim Maia fez uma música para mim.',
    'Perca sua vez.',
    'Avance duas casas.',
    'Volte uma casa.'
]

coisas = [torneira, notebook, torradeira, mesa, cafe, copo, salgadinho, chocolate]

def main():
    print(f'''JuuKyuu! Um jogo de adivinhação.
By Hideaki Fukami

Bem vindo ao 10Q!
Nesse jogo você terá a possibilidade de escolher entre dez opções e receber uma dica para te ajudar a descobrir qual a coisa em questão.

Quando menos dicas você precisar receber, mais pontos você ganha!

Vamos jogar?!
''')

    while True: #Looping Principal
        secretObject = getSecretObject()
        random.shuffle(secretObject)
        pontosTotal = 0
        
        secretName = ''
        if secretObject[0] in torneira:
            secretName = 'torneira'
        elif secretObject[0] in notebook:
            secretName = 'notebook'
        elif secretObject[0] in torradeira:
            secretName = 'torradeira'
        elif secretObject[0] in mesa:
            secretName = 'mesa'
        elif secretObject[0] in cafe:
            secretName = 'cafe'
        elif secretObject[0] in copo:
            secretName = 'copo'
        elif secretObject[0] in salgadinho:
            secretName = 'salgadinho'
        elif secretObject[0] in chocolate:
            secretName = 'chocolate'

        for i in range(0, 10):
            secretObject[i] = f'{i+1}. ' + secretObject[i]

        numGuesses = 1
        numChoices = list(range(1, 11))
        while numGuesses <= 10:
            guess = ''         
            while guess.lower() != secretName:
                choice = int(input('Vamos lá! Escolha um número de 1 a 10!\n> '))
                if choice in numChoices:
                    print(f'Você escolheu a dica #{choice}: \n')
                    clue = secretObject[choice - 1]
                    print(clue + '\n')
                    guess = input('Qual o seu palpite?\n> ')
                    print('\n')
                    numChoices.remove(choice)
                elif choice not in numChoices:
                    print('Você já escolheu esse número. Tente novamente.\n')
                
            if guess.lower() == secretName:
                points = 10 - numGuesses
                print(f'Você ganhou {points}!')
                break
            if numGuesses > 10:
                points = 0
                print('Todas suas dicas acabaram e você não pontuou!\n')
                print(f'A resposta era {secretName.title()}.')
                break
            
            numGuesses += 1

        pontosTotal += points
        print('Você quer jogar novamente? (Sim ou Não)')
        if not input('> ').lower().startswith('s'):
            print(f'Seu total de pontos foi de {pontosTotal} pontos.')
            break
    print('Obrigado por jogar!')

def getSecretObject():
    random.shuffle(coisas)
    secretObject = coisas[0]
    return secretObject

if __name__ == '__main__':
    main()