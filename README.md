# Chatbot dedicado à vítima de violência doméstica

O presente chatbot usa o poder das LLMs e do Python para ajudar a vítima de violência doméstica.

O LlamaIndex é empregado para acessar, estruturar e aprender com fontes de dados privadas, no caso, cartilhas publicadas por órgãos oficiais (Governos, MPs, ONGs, etc) com conteúdo dedicado ao enfrentamento da violência doméstica. 

O Streamlit é usado para a construção de uma interface do usuário simples e eficiente.

A solução pode, em algum contexto, ajudar as vítimas a obter, de forma mais rápida e direta, as informações de que necessita para a compreensão do assunto e entendimento sobre os instrumentos de proteção legal colocados a seu alcance.

O cógido foi adaptado de https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/#what-is-llamaindex por José Eduardo de Souza Pimentel, para eventual uso da Promotoria de Justiça de Piracicaba.

Notas da versão de 27/07/2024:

1) Atualizamos para o LLM para o modelo "gpt-4o-mini".
2) Tratando-se de projeto experimental, o usuário deve informar a API key da OpenAI para usar o chat. A informação não será gravada.
