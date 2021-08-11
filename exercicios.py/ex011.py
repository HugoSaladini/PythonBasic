altu = float(input('Digite a Altura da parede: '))
larg = float(input('Digite a Largura da parede: '))
area = larg*altu
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(altu, larg, area))
tinta = area/2
print('Para pintar sua parede você vai precisar de {}l de Tinta'.format(tinta))
