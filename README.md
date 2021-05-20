
<img width="877" alt="Screen Shot 2021-05-20 at 9 42 16 AM" src="https://user-images.githubusercontent.com/22969988/119017776-330dd980-b950-11eb-9dc6-2c34d1304dc5.png">


## Install
- git clone and cd to directory 
- install Selenium 
- download chromedriver.exe to same directory
 
## First Run
Platforms like PrimeVideo, Hulu, and HBO Max aren't very kind to bots so `ChromeOptions` loads cookies from previous useage. First run opens a chrome browser, goes to streaming platform and asks the user to log in. (Hulu and Amazon require captcha's/SMS). <br>
Once the browser is recognized the first time, it stays logged in the next time.

## Regular Use 
`python search.py --movie Movie Title`

## Future Updates
- Improve search results: Mainly uses `if substring in string` where `substring` is user's movie_title and `string` is movie title as listed on streaming platform. (I.e. movie_title="Now You See Me" is found as "Pretty Little Liars, S4 E12: Now You See Me, Now You Don’t." which is not ideal)
- threading/parallel: `from multiprocessing import Pool` to query platforms simultaneously.
- headless browser mode
