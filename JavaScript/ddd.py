
# 링크 각개전투
for link in fldzm:
    driver.get(link)
    time.sleep(0.2)
    html2 = driver.page_source
    html2 = driver.page_source
    soup2 = BeautifulSoup(html2, 'html.parser')
    try:
     passs=soup2.find('div', id='stock-status').text.strip()
     if passs == 'In Stock':
        try :     
         wnth=soup2.find('div', 'product-grouping-wrapper defer-block').article['itemid']        
        except AttributeError:
         wnth=''
        except TypeError:
         wnth=''
        except IndexError:
         wnth=''
        else:
         wnthth.append(wnth)  
      
        try :
         vnawjff=soup2.find('div', 'text-danger stock-status-text').get_text().strip()
        except AttributeError:
         vnawjff=''
        else:
         print('품절이에요! '+link)
         print("=" *70)

        try :
         dlfmaa=soup2.find('h1',id='name').get_text()
        except AttributeError:
         dlfmaa=' '
        else:
         dlfma.append(dlfmaa)

        try :
         rkrurr=soup2.find('div',id='price').get_text().strip()
        except AttributeError:     
         rkrurr=' '
        except TypeError:
         rkrurr=' '
        except IndexError:
         rkrurr=' '
        else:      
         rkrur.append(rkrurr)

    # 무게 + 내용물

        try:
         anrpp=soup2.find('span',class_='product-weight').get_text().strip()     
        except AttributeError:
         anrpp=''    
        else:
         anrp.append(anrpp)    

        try:
         sksksk=soup2.find('div', class_='supplement-facts-container').text
        except AttributeError:
         sksksk=' '
         sodydanf.append(sksksk)
        else:
         sodydanf.append(sksksk)

    #     카테고리
    #     try :
    #      zkxprhfll=soup2.select('div > a.last')          
    #      for i in zkxprhfll:
    #       line.append(i.text)
    #      zkxprhflll.append(line)          
    #     except AttributeError:
    #      pass
    #     else:
    #      zkxprhfl.append(zkxprhflll)

        try :
            if len(soup2.find('div', class_='thumbnail-container').find_all('img'))==0:
                img1.append(' ')
                img2.append(' ')
                img3.append(' ')
                img4.append(' ')
                img5.append(' ')
                img6.append(' ')


            if len(soup2.find('div', class_='thumbnail-container').find_all('img'))==1:
                try :
                 img11=soup2.find('div', 'thumbnail-container').img['data-large-img']
                except AttributeError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                except TypeError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                except IndexError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                else:
                 img1.append(img11)

                img2.append(' ')
                img3.append(' ')
                img4.append(' ')
                img5.append(' ')
                img6.append(' ')


            if len(soup2.find('div', class_='thumbnail-container').find_all('img'))==2:
                try :
                 img11=soup2.find('div', 'thumbnail-container').img['data-large-img']
                except AttributeError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                except TypeError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                except IndexError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                else:
                 img1.append(img11)

                try :
                 img22=soup2.select('div .thumbnail-container > img')[1]['data-large-img']
                except AttributeError:
                 img22=' '
                 img2.append(img22)
                 print('이미지2 에러났어용 '+link)
                 print("=" *70)
                except TypeError:
                 img22=' '
                 img2.append(img22)
                 print('이미지2 에러났어용 '+link)
                 print("=" *70)
                except IndexError:
                 img22=' '
                 img2.append(img22)
                 print('이미지2 에러났어용 '+link)
                 print("=" *70)
                else:
                 img2.append(img22)

                img3.append(' ')
                img4.append(' ')
                img5.append(' ')
                img6.append(' ')


            elif len(soup2.find('div', class_='thumbnail-container').find_all('img'))==3:
                try :
                 img11=soup2.find('div', 'thumbnail-container').img['data-large-img']
                except AttributeError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                except TypeError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                except IndexError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                else:
                 img1.append(img11)

                try :
                 img22=soup2.select('div .thumbnail-container > img')[1]['data-large-img']
                except AttributeError:
                 img22=' '
                 img2.append(img22)
                 print('이미지2 에러났어용 '+link)
                 print("=" *70)
                except TypeError:
                 img22=' '
                 img2.append(img22)
                 print('이미지2 에러났어용 '+link)
                 print("=" *70)
                except IndexError:
                 img22=' '
                 img2.append(img22)
                 print('이미지2 에러났어용 '+link)
                 print("=" *70)
                else:
                 img2.append(img22)

                try :
                 img33=soup2.select('div .thumbnail-container > img')[2]['data-large-img']
                except AttributeError:
                 img33=' '
                 img3.append(img33)
                 print('이미지3 에러났어용 '+link)
                 print("=" *70)
                except TypeError:
                 img33=' '
                 img3.append(img33)
                 print('이미지3 에러났어용 '+link)
                 print("=" *70)
                except IndexError:
                 img33=' '
                 img3.append(img33)
                 print('이미지3 에러났어용 '+link)
                 print("=" *70)
                else:
                 img3.append(img33)

                img4.append(' ')
                img5.append(' ')
                img6.append(' ')


            elif len(soup2.find('div', class_='thumbnail-container').find_all('img'))==4:
                try :
                 img11=soup2.find('div', 'thumbnail-container').img['data-large-img']
                except AttributeError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                except TypeError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                except IndexError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                else:
                 img1.append(img11)

                try :
                 img22=soup2.select('div .thumbnail-container > img')[1]['data-large-img']
                except AttributeError:
                 img22=' '
                 img2.append(img22)
                 print('이미지2 에러났어용 '+link)
                 print("=" *70)
                except TypeError:
                 img22=' '
                 img2.append(img22)
                 print('이미지2 에러났어용 '+link)
                 print("=" *70)
                except IndexError:
                 img22=' '
                 img2.append(img22)
                 print('이미지2 에러났어용 '+link)
                 print("=" *70)
                else:
                 img2.append(img22)

                try :
                 img33=soup2.select('div .thumbnail-container > img')[2]['data-large-img']
                except AttributeError:
                 img33=' '
                 img3.append(img33)
                 print('이미지3 에러났어용 '+link)
                 print("=" *70)
                except TypeError:
                 img33=' '
                 img3.append(img33)
                 print('이미지3 에러났어용 '+link)
                 print("=" *70)
                except IndexError:
                 img33=' '
                 img3.append(img33)
                 print('이미지3 에러났어용 '+link)
                 print("=" *70)
                else:
                 img3.append(img33)

                try :
                 img44=soup2.select('div .thumbnail-container > img')[3]['data-large-img']
                except AttributeError:
                 img44=' '
                 img4.append(img44)  
                 print('이미지4 에러났어용 '+link)
                 print("=" *70)
                except TypeError:
                 img44=' '
                 img4.append(img44)  
                 print('이미지4 에러났어용 '+link)
                 print("=" *70)
                except IndexError:
                 img44=' '
                 img4.append(img44)  
                 print('이미지4 에러났어용 '+link)
                 print("=" *70)
                else:
                 img4.append(img44)  

                img5.append(' ')
                img6.append(' ')

            elif len(soup2.find('div', class_='thumbnail-container').find_all('img'))==5:
                try :
                 img11=soup2.find('div', 'thumbnail-container').img['data-large-img']
                except AttributeError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                except TypeError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                except IndexError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                else:
                 img1.append(img11)

                try :
                 img22=soup2.select('div .thumbnail-container > img')[1]['data-large-img']
                except AttributeError:
                 img22=' '
                 img2.append(img22)
                 print('이미지2 에러났어용 '+link)
                 print("=" *70)
                except TypeError:
                 img22=' '
                 img2.append(img22)
                 print('이미지2 에러났어용 '+link)
                 print("=" *70)
                except IndexError:
                 img22=' '
                 img2.append(img22)
                 print('이미지2 에러났어용 '+link)
                 print("=" *70)
                else:
                 img2.append(img22)

                try :
                 img33=soup2.select('div .thumbnail-container > img')[2]['data-large-img']
                except AttributeError:
                 img33=' '
                 img3.append(img33)
                 print('이미지3 에러났어용 '+link)
                 print("=" *70)
                except TypeError:
                 img33=' '
                 img3.append(img33)
                 print('이미지3 에러났어용 '+link)
                 print("=" *70)
                except IndexError:
                 img33=' '
                 img3.append(img33)
                 print('이미지3 에러났어용 '+link)
                 print("=" *70)
                else:
                 img3.append(img33)

                try :
                 img44=soup2.select('div .thumbnail-container > img')[3]['data-large-img']
                except AttributeError:
                 img44=' '
                 img4.append(img44)  
                 print('이미지4 에러났어용 '+link)
                 print("=" *70)
                except TypeError:
                 img44=' '
                 img4.append(img44)  
                 print('이미지4 에러났어용 '+link)
                 print("=" *70)
                except IndexError:
                 img44=' '
                 img4.append(img44)  
                 print('이미지4 에러났어용 '+link)
                 print("=" *70)
                else:
                 img4.append(img44)  

                try :
                 img55=soup2.select('div .thumbnail-container > img')[4]['data-large-img']
                except AttributeError:
                 img55=' '
                 img5.append(img55)  
                 print('이미지5 에러났어용 '+link)
                 print("=" *70)
                except TypeError:
                 img55=' '
                 img5.append(img55)  
                 print('이미지5 에러났어용 '+link)
                 print("=" *70)
                except IndexError:
                 img55=' '
                 img5.append(img55)  
                 print('이미지5 에러났어용 '+link)
                 print("=" *70)
                else:
                 img5.append(img55)  

                img6.append(' ')  

            elif len(soup2.find('div', class_='thumbnail-container').find_all('img'))==6:
                try :
                 img11=soup2.find('div', 'thumbnail-container').img['data-large-img']
                except AttributeError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                except TypeError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                except IndexError:
                 img11=' '
                 img1.append(img11)
                 print('이미지1 에러났어용 '+link)
                else:
                 img1.append(img11)

                try :
                 img22=soup2.select('div .thumbnail-container > img')[1]['data-large-img']
                except AttributeError:
                 img22=' '
                 img2.append(img22)
                 print('이미지2 에러났어용 '+link)
                 print("=" *70)
                except TypeError:
                 img22=' '
                 img2.append(img22)
                 print('이미지2 에러났어용 '+link)
                 print("=" *70)
                except IndexError:
                 img22=' '
                 img2.append(img22)
                 print('이미지2 에러났어용 '+link)
                 print("=" *70)
                else:
                 img2.append(img22)

                try :
                 img33=soup2.select('div .thumbnail-container > img')[2]['data-large-img']
                except AttributeError:
                 img33=' '
                 img3.append(img33)
                 print('이미지3 에러났어용 '+link)
                 print("=" *70)
                except TypeError:
                 img33=' '
                 img3.append(img33)
                 print('이미지3 에러났어용 '+link)
                 print("=" *70)
                except IndexError:
                 img33=' '
                 img3.append(img33)
                 print('이미지3 에러났어용 '+link)
                 print("=" *70)
                else:
                 img3.append(img33)

                try :
                 img44=soup2.select('div .thumbnail-container > img')[3]['data-large-img']
                except AttributeError:
                 img44=' '
                 img4.append(img44)  
                 print('이미지4 에러났어용 '+link)
                 print("=" *70)
                except TypeError:
                 img44=' '
                 img4.append(img44)  
                 print('이미지4 에러났어용 '+link)
                 print("=" *70)
                except IndexError:
                 img44=' '
                 img4.append(img44)  
                 print('이미지4 에러났어용 '+link)
                 print("=" *70)
                else:
                 img4.append(img44)  

                try :
                 img55=soup2.select('div .thumbnail-container > img')[4]['data-large-img']
                except AttributeError:
                 img55=' '
                 img5.append(img55)  
                 print('이미지5 에러났어용 '+link)
                 print("=" *70)
                except TypeError:
                 img55=' '
                 img5.append(img55)  
                 print('이미지5 에러났어용 '+link)
                 print("=" *70)
                except IndexError:
                 img55=' '
                 img5.append(img55)  
                 print('이미지5 에러났어용 '+link)
                 print("=" *70)
                else:
                 img5.append(img55)  

                try :
                 img66=soup2.select('div .thumbnail-container > img')[5]['data-large-img']
                except AttributeError:
                 img66=' '
                 img6.append(img66)  
                 print('이미지6 에러났어용 '+link)
                 print("=" *70)
                except TypeError:
                 img66=' '
                 img6.append(img66)  
                 print('이미지6 에러났어용 '+link)
                 print("=" *70)
                except IndexError:
                 img66=' '
                 img6.append(img66)  
                 print('이미지6 에러났어용 '+link)
                 print("=" *70)
                else:
                 img6.append(img66)  
        except AttributeError:
         print('이미지도 패스할께요~~')
         print("=" *70)
        else:
         pass      
     elif soup2.find('div',class_='return-links').find('a').text == 'Return to Homepage':
      pass
      print('구매 불가능한 상품이에요!!')
      print("=" *70)
    else:  
     pass