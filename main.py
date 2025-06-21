from bs4 import BeautifulSoup
import requests
import pandas as pd
import os



while True:
    try :
        if os.path.exists('num.txt') == False:
            with open('num.txt' , 'w') as f1 :
                f1.write("1")
                num = 1
        else:
            with open('num.txt' , 'r') as f1 :
                num = f1.read()
                num = int(num)
        
        if num < 25:

            url = f"https://www.scrapethissite.com/pages/forms/?page_num={num}"
            table = requests.get(url)
            soup = BeautifulSoup(table.text, 'html')

            head = soup.find_all('th')
            final_head = [elem.text.strip() for elem in head]

            df = pd.DataFrame(columns = final_head) 
            row_all = soup.find_all('tr')

            for row in row_all[1:]:
                row_data = row.find_all('td')
                clean_row = [i.text.strip() for i in row_data]

                length = len(df)
                df.loc[length] = clean_row

            os.makedirs('CSV' , exist_ok=True)

            df.to_csv(f"CSV/{num}.csv" , index = False)
            with open('num.txt' , 'w') as f2:
                    f2.write(f"{num+1}")


            print(f"CSV file {num}.csv created successfully")
        
        else:
            print("All CSV files are created")
            print("No Pages are left")
            break
        
    except KeyboardInterrupt:
         print("Program Terminated by user")
         break
    
