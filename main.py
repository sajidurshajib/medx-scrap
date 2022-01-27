from bs4 import BeautifulSoup
import requests

url = 'https://medex.com.bd/'
i = 1
def app():
    page_number = 1
    last_page = 707

    while page_number <= last_page:
        single_page = url+'brands?page='+str(page_number)
        page(single_page)
        page_number +=1

def page(single_page):
    print('')
    print('    '+single_page)
    print('')
    html_text = requests.get(single_page).text
    soup = BeautifulSoup(html_text, 'lxml')
    hovarable_block = soup.find_all('a', class_ = 'hoverable-block')

    global i
    for b in hovarable_block:
        brand_name = b.select("div:nth-child(1) > div:nth-child(1)")[0].text.replace('\n', '').strip()
        generic_name = b.select("div:nth-child(1) > div:nth-child(3)")[0].text.replace('\n', '').strip()
        
        strength = b.select("div:nth-child(1) > div:nth-child(2)")[0].text.replace('\n', '').strip()
        icon_name = b.find('img').get('title').strip()
        
        pharma = b.select("div:nth-child(1) > div:nth-child(4)")[0].text.replace('\n', '').strip()

        price_split = b.select("div:nth-child(1) > div:nth-child(5) span")[0].text.replace('\n', '').strip().split()
        price = ' '.join(price_split)

        with open('medx.txt','a',newline='\n') as f:
            f.write(f'{brand_name} | {generic_name} | {icon_name} | {strength} | {pharma} | {price}')
            f.write('\n')
            f.close()
        
        print(f'''
        Brand Name: {brand_name},
        Generic Name: {generic_name},
        Strength: {strength},
        Type: {icon_name},
        Pharmaceuticals: {pharma}
        {price}
        ''')


        print('    '+str(i))
        i += 1




if __name__ == '__main__':
    app()