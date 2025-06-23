import pytest
from selenium.webdriver.common.by import By

#Q1: Find parent and first child element of a given element underlined in red color.
def test_find_xpath_of_parent_child_elements(setup):
    driver = setup

    #Xpath for "LIVE Classes" and its parent
    driver.find_element(By.XPATH, "//div[@id='liveclasses']") #xpath of LIVE Classes
    live_classes_parent = driver.find_element(By.XPATH, "//div[@id='liveclasses']/parent::div").text #parent of Live Classes still refer to the LIVE Class element along with drop down
    live_classes_grandparent= driver.find_element(By.XPATH, "//div[@id='liveclasses']/parent::div/parent::div").text #Grandparent of LIVE Classes
    print (f"Immediate parent element of live Classes: {live_classes_parent}")
    assert "LIVE Classes" in live_classes_parent
    print(f"Grand parent element of live Classes: {live_classes_grandparent}")
    assert "Courses" in live_classes_grandparent


    #Child elements on LIVE Classes
    driver.find_element(By.XPATH, "//div[@id='liveclasses']/p[@id='liveclasseslink']") #The first child of the LiveClasses element
    driver.find_element(By.XPATH, "//div[@id='liveclasses']").click() #getting into the drop down options of LIVE Classes
    #Visually Zen Class option under LIVE Classes seems to be the first child.
    live_class_first_child = driver.find_element(By.XPATH, "//div[@id='liveclasses']/parent::div/div[2]//li[1]//p[1]").text
    print(f"First child of LIVE classes is: {live_class_first_child}")
    assert "ZEN CLASS" in live_class_first_child


#Q2: locate the second sibling of LIVE Classes
def test_xpath_of_second_sibling(setup):
    driver = setup
    #Finding the second sibling of LIVE Classes
    second_sibling_live_classes = driver.find_element(By.XPATH, "//div[@id='liveclasses']/parent::div/following-sibling::div[2]").text
    print(f"Second sibling of LIVE Classes is: {second_sibling_live_classes}")
    assert "Resources" in second_sibling_live_classes

#Q3: Select the parent element of an element with the attribute href
def test_find_parent_element_of_href(setup):
    driver = setup

    #Finding the parent element of Courses, which is an href element
    parent_of_href_courses = driver.find_element(By.XPATH, "//a[@href='/courses/' and text()='Courses']/parent::div").text

    #validating the text of parent element has all the below content
    expected_content = ['Courses', 'LIVE Classes', 'Practice', 'Resources', 'Products']
    missing_content = [content for content in expected_content if content not in parent_of_href_courses]

    #printing missing text if any
    assert not missing_content, f"Missing text is: {missing_content}"

#Q4: Find the ancestor elements of 'signup'
def test_find_all_ancestor_elements(setup):
    driver = setup

    #find all the ancestor elements of 'Sign up'
    all_ancestors_of_signup = driver.find_element(By.XPATH, "//a[text()='Sign up']/ancestor::*").text
    print(f"All the ancestor elements of Sign up: {all_ancestors_of_signup}")

    #find all the ancestor elements of 'Sign up' at div level
    ancestor_elements_of_signup = driver.find_element(By.XPATH, "//a[text()='Sign up']/ancestor::div").text
    print(f"All the ancestor elements of Sign up at div level: {ancestor_elements_of_signup}")

#Q5: Locate all following siblings
@pytest.mark.smoke
def test_find_all_following_siblings(setup):
    driver = setup

    #get all the following siblings of "Courses"
    following_sibling_list = driver.find_elements(By.XPATH, "//a[@href='/courses/' and text()='Courses']/following-sibling::div")
    sibling_list = []

    #Iterate the following_sibling_list and store the text into a sibling_list
    for element in following_sibling_list:
        sibling_list.append(element.text)

    #Validate sibling_list matches the expected list
    expected_content = ['LIVE Classes', 'Practice', 'Resources', 'Products']
    print(f'Siblings of "Courses" are : {sibling_list}')
    assert sibling_list == expected_content

#Q6: Locate all preceding elements
@pytest.mark.smoke
def test_find_all_preceding_elements(setup):
    driver = setup

    #find all the preceding siblings of 'Products'
    preceding_sibling_of_products = driver.find_elements(By.XPATH, "//a[@href='/courses/' and text()='Courses']/parent::div/div[4]/preceding-sibling::*")
    actual_sibling_list = []

    for element in preceding_sibling_of_products:
        actual_sibling_list.append(element.text)

    expected_sibling_list = ['Courses', 'LIVE Classes', 'Practice', 'Resources']
    print(f"All the preceding siblings of Products: {actual_sibling_list}")

    assert actual_sibling_list == expected_sibling_list

    #validate count all preceding list elements from Courses
    preceding_elements_of_courses = driver.find_elements(By.XPATH, "//a[@href='/courses/' and text()='Courses']/preceding::li")

    no_of_list_elements_preceding_to_courses = len(preceding_elements_of_courses)
    print(f"No of list elements preceding to 'Courses' is: {no_of_list_elements_preceding_to_courses}")

    assert no_of_list_elements_preceding_to_courses == 22

