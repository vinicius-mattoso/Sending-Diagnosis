
![Welcome](/diagnosis_cover.png?raw=true)
# Sending Diagnosis

Esse projeto foi feito com uma extensão do "my first Deploy project of machine Learning".
Nele alem de conter o algoritmo de machine learning em produção por meio do Flask, o usuario ainda pode selecionar a opção para recer o resultado do seu diagnostico por e-mail.

# Primeira parte do projeto

Para esse projeto, foi criado inicialmente um ambiente virtual, para conter apenas as bibliotecas necessárias.
Como ja mencionado, toda a parte de Machine Learning e deploy do modelo veio do repositório "my first Deploy" e foi acoplada nesse projeto.
Para viabilizar o envio do e-mail, foi criado mais um arquivo em html para conter o formulário do envio e o arquivo html resposta que já existia foi adaptado.

# Segunda parte do projeto

Como segunda etapa do projeto, temos o envio do e-mail.

Para essa etapa foi criada a função de envio, assim como duas classes uma para conter os valores do input do usuário e permitir a migração de variaveis entre pagins e a segunda para conter os dados de e-mail e senha de quem ira enviar os e-mail.


# Test

Como teste já enviei o email para diferentes pessoas e está funcionando bem.

# Primeira Pag
Nessa página o usuário ira completar os dados necessários para a inteligencia fazer sua análise.

![Welcome](/PAG01.jpeg?raw=true)

# Segunda Pag
Nessa página o usuário ira receber a sua avaliação assim como uma recomendação para procurar o seu médico. Em seguida ele pode optar por enviar o relatório por e-mail ou retornar a página inicial

![Welcome](/PAG02.jpeg?raw=true)

# Futuras atualizações

Futuras atualizações na parte de Machine Learning podem ser realizadas, como rebalancear a base, validação cruzada ou até mesmo escolher outro tipo de algoritmo para a classificação.

Já para segunda parte, podemos atualizar a forma com que a resposta está sendo enviada colocando por exemplo: alguma logo da empresa, assinatura da empresa com o envio do diagnóstico.

 
