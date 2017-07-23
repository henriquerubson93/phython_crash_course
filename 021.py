nome = ['henrique','rodrigo','sergio']
print (nome[2].title() + ' Você nao pagou a conta e sera expulso')
nome[2] = 'filipe'

print (nome[2] + ' voce foi adicionado deseja ficar ?')
subs_nome = nome.pop()
print ('Como nao obtivemos resposta ' + subs_nome.upper() + ' tambem foi exlso')


