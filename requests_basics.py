import requests as req
from requests.auth import HTTPBasicAuth
import bs4
from bs4 import BeautifulSoup


## send get request with headers

## to get req

## DOCUMENTATION - HTTPBIN.org 


##### START - END TICKER ## 
def start()
    start_time = time.time()
    return start_time
    def end()
        print(f'[SYSTEM] Download complete in: [{time_to_complete}]')
        end_time = time.time()
        time_to_complete = end_time - start_time



print(f'[SYSTEM] Download complete in: [{time_to_complete}]')
end_time = time.time()
time_to_complete = end_time - start_time




#### DOWNLOADER ####
def downloader_00_LARGE_FILES_TO_READ(URL):
    with req.get(URL, stream=True) as rq:
        FILENAME = URL.split('/')[-1]
        with open(FILENAME, 'wb') as f:
            f.write(rq.content)  # rq.content contains the content needed (use for small files)
            # basic methods and atributes
            for line in rq.iter_lines(delimiter=b'\\n'):  ### buffers, so to save ram in bytes (delimiter is set to return new line_
                print(rq.headers)
                #print(rq.apparent_encoding)
                #print(rq.elapsed)  # prints the time between get request and receiving headers
                print(rq.status_code)
                print(rq.ok)  # prints webrequest status code
                print(rq.encoding)
                print(rq.url)
                f.write(line)

                return FILENAME

def downloader_00_simple(URL):
    local_filename = url.split('/')[-1]  # remove the last char '/'' 
    with requests.get(URL, stream = True) as r:
        print("downloading.. ")
        with open(FILE_LOC+local_filename, 'wb') as f: ## determie FILE_LOC later
            print('writing data to disk')
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        f.close()
        print('Completed Download in.. ')
        print('File Saved as ' + local_filename)


   



def downloader_01(url, filename):
    
    try:
        print(req.headers())
        print(req.url())
        print(req.status_code)
        if file_name:
            pass
        else:
            filename = req.url[
                        url.rfind('/')+1:]  ## string splicing for URL    with open (file_name, 'wb') as f:
        with req.get(url):
            with open(filename, 'wb') as f:
                for buffer in req.iter_content(chunk_size=8192):
                    if buffer:
                        f.write(buffer)
            return filename

    except exception as e:
        return e


def downloader_03():  #
            try:  # parsing w/header
                print()
                print(f'[SYSTEM]** Connecting To Server. Sleeping for 5 seconds... ')
                time.sleep(3)
                URL = key
                print(type(URL))
                print(URL)
                HEADERS = {}
                HEADERS[
                    "User-Agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

                req = urllib.request.Request(URL, headers=HEADERS)
                resp = urllib.request.urlopen(req)
                respData = resp.read()

                saveFile = open("resp_data.txt", "w")
                saveFile.write(str(respData))
                saveFile.close()
                print(f'[SYSTEM]server response data saved to {saveFile} in program directory')

                return req
                # respData = resp.read(req)
                ## save file for further analasys --






################################################################################
## Creates files when passed a URL 
def file_name_creator(URL):
    URL = url.split('/')[-1] ## splits string to list, specififies delimitor 
    return URL 

    ## or ## 
    NAME_LEN = len(DOWNLOAD_NAME)
    DOWNLOAD_NAME = DOWNLOAD_NAME[NAME_LEN - 25 :]


## what would you like to search for ## ? 
def url_query(): 
    ### QUERY SEARCH ###
    payload = {'query': 'sega dreamcast'}
    r = requests.get('https://archive.org/search.php', params=payload)
    print(),print()
    print(r.text) ## to receieve response 
    print(),print()
    print(r.headers) ## to print headers 
    print(),print()
    print(r.url)
    print(),print()
    print(r.json)



## BUILD WEBSITE STATUS CHECKER ## 
## BUILD PASSWORD GUESSER for ##
## passing credentials for basic authentication - 
def basic_authentication_login(url, auth)
    r = req.get('http://httpbin.org/basic-auth/penis/man', auth=('penis', 'man'), timeout=3)
    print(r) ## to receive response back 
    print(r.status_code)


## to pass credentials:: 
# specifiy credentials in url to test against.

def simple_downloader(filename)
    with open(filename,'wb') as f: ## specify path name in with open param
        print(r.status_code)
        # print(r.ok) respond true if status 200-400
        print(r.content)  ## returns contents of file (byte format etc..)
        f.write(r.content)




def downloader_00(URL):
    with req.get(URL, stream=True) as rq:
        FILENAME = URL.split('/')[-1]
        with open(FILENAME, 'wb') as f:
            f.write(rq.content)  # rq.content contains the content needed (use for small files)
            # basic methods and atributes
            for line in rq.iter_lines(delimiter=b'\\n'):  ### buffers, so to save ram in bytes (delimiter is set to return new line_
                print(rq.headers)
                #print(rq.apparent_encoding)
                #print(rq.elapsed)  # prints the time between get request and receiving headers
                print(rq.status_code)
                print(rq.ok)  # prints webrequest status code
                print(rq.encoding)
                print(rq.url)
                f.write(line)

                return FILENAME


def downloader_01(url, filename):
    print(req.headers())
    print(req.url())
    print(req.status_code)
    try:
        if file_name:
            pass
        else:
            filename = req.url[
                        url.rfind('/')+1:]  ## string splicing for URL    with open (file_name, 'wb') as f:

        with req.get(url):
            with open(filename, 'wb') as f:
                for buffer in req.iter_content(chunk_size=8192):
                    if buffer:
                        f.write(buffer)
            return filename

    except exception as e:
        return e

        






# input_url = 'https://archive.org/download/NaomiRomsReuploadByGhostware/Capcom_vs_SNK_2_Mark_of_the_Millennium_2001.zip'


input_url = 'https://archive.org/download/NaomiRomsReuploadByGhostware'
r = req.get(input_url) # ininize object as r
#print(r.help)
print(dir(r))
print(r.text) # to get html data as unicode
print(r) # returns status

## to access specific url by keyword param
# ## SAMPLE WEBSITE https://archive.org/search.php?query=sega%20dreamcast ##
# payload = {'query':sega%20dreamcast}
# r = requests.get('https://archive.org/search.php?')






# downloader(input_url)
#### BEAUTIFUL SOUP ##
# soup = BeautifulSoup(html_doc, 'html.parser')











