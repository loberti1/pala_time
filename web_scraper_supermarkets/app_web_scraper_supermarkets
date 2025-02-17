"""code to get a mean price for a list of general goods and choose the cheapest supermarket
STILL WORKING 02-2025"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#depending on the site changes, you may change URL or classes depending on the error
urls = {'carrefour':['https://www.carrefour.com.ar/leche-entera-larga-vida-las-tres-ninas-1-l/p',
                     'https://www.carrefour.com.ar/bife-de-chorizo-novillito-x-kg-662854/p',
                     'https://www.carrefour.com.ar/pan-blanco-lactal-rodajas-finas-en-bolsa-460-g-717550/p',
                     'https://www.carrefour.com.ar/tomate-x-kg/p',
                     'https://www.carrefour.com.ar/vino-tinto-malbec-alma-mora-750-cc/p',
                     'https://www.carrefour.com.ar/pollo-entero-congelado-x-kg-699692/p',
                     'https://www.carrefour.com.ar/jabon-liquido-para-ropa-skip-bio-encimas-3-l-695707/p',
                     'https://www.carrefour.com.ar/aceite-de-oliva-extra-virgen-cocinero-suave-500-cc/p',
                     'https://www.carrefour.com.ar/gaseosa-cola-coca-cola-sabor-original-225-lts-30138/p',
                     'https://www.carrefour.com.ar/fideos-tallarines-don-vicente-en-bolsa-500-g-729408/p']
        ,'dia':['https://diaonline.supermercadosdia.com.ar/leche-entera-las-3-ninas-larga-vida-1-lt-58463/p',
                'https://diaonline.supermercadosdia.com.ar/bife-de-chorizo-x-1-kg-279638/p',
                'https://diaonline.supermercadosdia.com.ar/pan-blanco-lactal-460-gr-245473/p',
                'https://diaonline.supermercadosdia.com.ar/tomate-redondo-x-1-kg-90127/p',
                'https://diaonline.supermercadosdia.com.ar/vino-tinto-alma-mora-malbec-750-ml-104269/p',
                'https://diaonline.supermercadosdia.com.ar/pollo-congelado-x-1-kg-718817/p',
                'https://diaonline.supermercadosdia.com.ar/jabon-liquido-para-diluir-skip-bio-enzimas-500-ml-130048/p',
                'https://diaonline.supermercadosdia.com.ar/aceite-de-oliva-cocinero-extra-virgen-suave-500-ml-276154/p',
                'https://diaonline.supermercadosdia.com.ar/gaseosa-coca-cola-sabor-original-175-lt-249072/p',
                'https://diaonline.supermercadosdia.com.ar/fideos-tallarin-don-vicente-500-gr-299848/p']
        ,'coto':['https://www.cotodigital.com.ar/sitios/cdigi/productos/leche-larga-vida-entera-las-tres-ni%C3%B1as-ttb-1l/_/R-00254550-00254550-200',
                 'https://www.cotodigital.com.ar/sitios/cdigi/productos/bife-de-chorizo-peso-aproximado-de-la-unidad-1-020-kg-x-kg/_/R-00035017-00035017-200?Dy=1',
                 'https://www.cotodigital.com.ar/sitios/cdigi/productos/pan-blanco-lactal-460g/_/R-00558090-00558090-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels',
                 'https://www.cotodigital.com.ar/sitios/cdigi/productos/tomate-red-x-kg/_/R-00000684-00000684-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels',
                 'https://www.cotodigital.com.ar/sitios/cdigi/productos/vino-malbec-alma-mora-750cc/_/R-00187089-00187089-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels',
                 'https://www.cotodigital.com.ar/sitios/cdigi/productos/pollo-congelado-x-kg/_/R-00042989-00042989-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels',
                 'https://www.cotodigital.com.ar/sitios/cdigi/productos/jab%C3%B3n-l%C3%ADquido-para-diluir-skip-500ml/_/R-00531047-00531047-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels',
                 'https://www.cotodigital.com.ar/sitios/cdigi/productos/aceite-oliva-extra-virgen-cocinero-500ml/_/R-00562393-00562393-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels',
                 'https://www.cotodigital.com.ar/sitios/cdigi/productos/gaseosa-coca-cola-sabor-original-2-25-lt/_/R-00014450-00014450-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels',
                 'https://www.cotodigital.com.ar/sitios/cdigi/productos/fideos-caserito-con-huevo-don-vicente-500g/_/R-00573936-00573936-200?Dy=1&assemblerContentCollection=%2Fcontent%2FShared%2FAuto-Suggest%20Panels']}

classes = {'carrefour':'valtech-carrefourar-product-price-0-x-sellingPriceValue'
            ,'dia':'diaio-store-5-x-sellingPriceValue'
            ,'coto':'price'}

class Supersearch:
    def __init__(self,market: str):
        self.market = market

    def mean_supermarket(self) ->float:
        prices = []

        #chrome setup
        chrome_options = Options().add_argument('--headless')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(chrome_options,service)

        #get prices for each product
        for url in urls[self.market]:
            driver.get(url)
            driver.implicitly_wait(2)
            price = driver.find_element(By.CLASS_NAME, classes[self.market])
            prices.append(float(price.text.replace(' ','').replace('$','').replace('.','').replace(',','.').replace('\n-54%','')
                                .replace('\nc/u','')))

        #close chrome and return mean price
        driver.quit()
        return round(sum(prices)/len(prices),2)

print('This solutions serves as a finder of the cheapest supermarket nearby home, depending on the month, the cheapest supermarket may change')
print('Searching...')

#getting all average values
mean_carrefour = Supersearch('carrefour').mean_supermarket()
mean_dia = Supersearch('dia').mean_supermarket()
mean_coto = Supersearch('coto').mean_supermarket()
index = {'Carrefour':mean_carrefour,'Dia':mean_dia,'Coto':mean_coto}

print(f'\nMean price for Carrefour is: ${mean_carrefour}')
print(f'Mean price for Dia is: ${mean_dia}')
print(f'Mean price for Coto is: ${mean_coto}')

#getting the best option to buy this week
cheapest_average = min(mean_carrefour,mean_dia,mean_coto)
cheapest_supermarket = ''.join([key for key, val in index.items() if val == cheapest_average])
print(f'\nThis week you should buy in {cheapest_supermarket}, its average price is ${cheapest_average}!!!')