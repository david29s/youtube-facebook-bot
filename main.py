from selenium import webdriver

def search(input_message):
    options = webdriver.ChromeOptions()

    options.add_argument('headless')

    driver = webdriver.Chrome(executable_path='/home/david/PycharmProjects/youtube-facebook/chromedriver', options=options)

    driver.get('https://www.youtube.com/results?search_query={}'.format(input_message))

    search_result = driver.find_elements_by_xpath('//a[@class="yt-simple-endpoint inline-block style-scope ytd-thumbnail"][@aria-hidden="true"][@tabindex="-1"]')

    for href in search_result:
        link_result = href.get_attribute('href')

    description_result = driver.find_elements_by_xpath('//*[@id="description-text"]')
    images_result = driver.find_elements_by_xpath('//*[@id="img"]')

    for description in description_result:
        driver.find_elements_by_tag_name('yt-formated-string')
        description_res = description.text
       #print(description_res)

    for image in images_result:
        images_res = image.get_attribute('src')
        #print(images_res)

    title_result = driver.find_elements_by_xpath('//*[@id="video-title"]')

    for title in title_result:
        title_res = title.get_attribute('title')
        print(title_res)

    result = [{'title': title_res},
            {'url': link_result},
            {'image': images_res},
            {'description': description_res}]

    # for i in result:
    #     i = 0
    #     print(i+1)

    #print(title_res)

search('eminem')


