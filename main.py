import sys, os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

MOSTRAR_NAVEGADOR = True
BROWSER = 'Chrome'

if (BROWSER == 'Firefox'):
    options = webdriver.firefox.options.Options()
    options.add_argument("--no-sandbox")

    if (not MOSTRAR_NAVEGADOR):
        options.add_argument("--headless")

    driver = webdriver.Firefox(
        executable_path = os.path.dirname(os.path.realpath(__file__)) + '/geckodriver', 
        options=options
    )
else:
    options = webdriver.chrome.options.Options()
    options.add_argument("--no-sandbox")

    if (not MOSTRAR_NAVEGADOR):
        options.add_argument("--headless")

    driver = webdriver.Chrome(
        executable_path = os.path.dirname(os.path.realpath(__file__)) + '/chromedriver', 
        options=options
    )

driver.set_window_size(1366, 768)
wait = WebDriverWait(driver, 10)

try:
    url = "https://infallible-heyrovsky-9b3be9.netlify.app/"
    print('Acessando URL ', url)
    driver.get(url)

    # Apenas para facilitar a visualização
    if (MOSTRAR_NAVEGADOR):
        time.sleep(1)

    title = "React App"
    assert title in driver.title, ('O título da janela deve ser "' + title + '"')
    print('OK')

    print('Realizar login no site')
    driver.find_element_by_name("email").send_keys("selenium@selenium.com")
    driver.find_element_by_name("senha").send_keys("123456")

    # Apenas para facilitar a visualização
    if (MOSTRAR_NAVEGADOR):
        time.sleep(1)

    driver.find_element_by_css_selector('.form-group + button').click()
    print('OK')

    print('Aguardando login ser concluído')
    try:
        element = wait.until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, 'table[class="table"]')
            )
        )

        print('OK')
    except TimeoutException:
        print('\n\033[91mNão foi possível encontrar a tabela de tarefas após o login!\033[0m')
        driver.close()
        sys.exit(1)


    # Apenas para facilitar a visualização
    if (MOSTRAR_NAVEGADOR):
        time.sleep(1)

    print('Validar pós-login')
    cabecalho = driver.find_element_by_css_selector('h1.mb-3').text
    assert cabecalho.startswith('Tarefas cadastradas'), ("O título da página deveria ser 'Tarefas cadastradas', porém ele é: " + cabecalho)
    print('OK')

    # Apenas para facilitar a visualização
    if (MOSTRAR_NAVEGADOR):
        time.sleep(1)
        
    print("Validação do ambiente finalizada com sucesso.")
except AssertionError as e:
    print('Erro ao executar validação:', e)
    raise
except Exception as e:
    print('Erro na execução:')
    raise

finally:
    driver.close()
