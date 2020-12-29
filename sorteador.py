from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from random import choice

def sorteio(url, n_sorteados=1):
  print('Aguarde...')
  
  #setup para usar webdriver no repl.it
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')

  #driver
  driver = webdriver.Chrome(options=chrome_options)

  #url de inicio
  driver.get("https://www.instagram.com/")

  sleep(2)

  #define local username e password
  username = driver.find_element_by_name("username")
  password = driver.find_element_by_name("password")

  #insere o username e a senha
  username.send_keys("")
  password.send_keys("")

  sleep(2)

  #clica no botão de entrar
  click_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
  click_button.click()

  sleep(5)

  #diz para não salvar o login info
  not_login_info = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
  not_login_info.click()

  sleep(3)

  #nao aceita as notificações
  not_notifications = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
  not_notifications.click()

  sleep(2)

  #entra na url solicitada
  driver.get(url)

  sleep(5)

  try:
    load_comments = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/div[1]/ul/li/div/button/span')
    while load_comments:
      load_comments.click()
      sleep(1)
      load_comments = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/div[1]/ul/li/div/button/span')
 
  except Exception as err_msg:
    print(err_msg)
    pass

  sleep(4)
  #pega os usuarios
  comments = driver.find_elements_by_class_name('gElp9')

  list_users = []

  for comment in comments:
    username = comment.find_element_by_class_name('_6lAjh').text
    if username not in list_users:
      list_users.append(username)

  driver.close()
  
  #sorteia as pessoas
  pessoas_sorteadas = []
  
  for sorteado in range(0, n_sorteados):
    pessoa_sorteada = choice(list_users)
    if pessoa_sorteada not in pessoas_sorteadas:
      pessoas_sorteadas.append(pessoa_sorteada)
    else:
      n_sorteados += 1

  return pessoas_sorteadas, len(list_users)

  