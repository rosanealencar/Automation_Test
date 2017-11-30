import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestingDiscourseWebsite():



driver = webdriver.Firefox()
driver.get("https://www.discourse.org/")
window_before = driver.window_handles[0]
#print window_before
assert "Discourse - Civilized Discussion" in driver.title


#select Demo option
tab = driver.find_element_by_css_selector('#main > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)')
tab.send_keys(Keys.ENTER)

driver.get("https://try.discourse.org/")
window_after = driver.window_handles[1]
#print window_after

#Scroll to the end of page
driver.switch_to_window(window_after)
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#Printing all locked topics
lockeditens = driver.find_elements_by_class_name('link-top-line')
for elements in lockeditens:
    blocked = elements.find_elements_by_class_name('topic-statuses')
    if len(blocked)> 0:
        print elements.text

print "Itens per category:"

discourseqtd = driver.find_elements_by_class_name('category-discourse')
print "Discourse = " + str(len(discourseqtd))

videosqtd = driver.find_elements_by_class_name('category-videos')
print "Videos = " + str(len(videosqtd))

uncqtd = driver.find_elements_by_class_name('category-uncategorized')
print "Uncategorized = " + str(len(uncqtd))

generalqtd = driver.find_elements_by_class_name('category-general')
print "General = " + str(len(generalqtd))

techqtd = driver.find_elements_by_class_name('category-tech')
print "Tech = " + str(len(techqtd))

moviesqtd = driver.find_elements_by_class_name('category-movies')
print "Movies = " + str(len(moviesqtd))

gamingqtd = driver.find_elements_by_class_name('category-gaming')
print "Gaming = " + str(len(gamingqtd))

schqtd = driver.find_elements_by_class_name('category-school')
print "School = " + str(len(schqtd))

sptqtd = driver.find_elements_by_class_name('category-sports')
print "Sport = " + str(len(sptqtd))


driver.close()
