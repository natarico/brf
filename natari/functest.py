from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time, unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_user_registers(self):
        # USER opens up a terminal and goes to the BRF website
        self.browser.get('http://localhost:8000')

        # The home page welcomes USER and displays signup form with link up top for login form
        self.assertIn('BRF', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('header').text
        self.assertIn('BRF', header_text)
        self.assertIn('Login', header_text)
        self.assertIn('SignUp', header_text)

        form_button = self.browser.find_element_by_tag_name('form').text
        self.assertIn('Register', form_button)

        # USER enters their name, a username, an email and a password and confirmation. The user clicks the register button again and is redirected to a survey asking for weather preference and city.
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.send_keys('testuser3')
        inputbox = self.browser.find_element_by_id('id_password1')
        inputbox.send_keys('123456789z')
        inputbox = self.browser.find_element_by_id('id_password2')
        inputbox.send_keys('123456789z')
        self.browser.find_element_by_id('reg').click()
        time.sleep(1)
        page = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Personalize', page)

        # USER chooses rainy, adds Seattle as their city and clicks on the submit button.
        inputbox = self.browser.find_element_by_id('id_city')
        inputbox.send_keys('Seattle')
        self.browser.find_element_by_id('survey').click()
        time.sleep(1)
        page = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Dashboard', page)
        
        # USER is redirected to a dashboard showing the top 10 high scores. Towards the top of the page, a navigation bar had links to the profile, as well as the game and to log out. On the right side of the page is a list of online players.
        self.fail('Finish the test!')


        # USER clicks on the link to their profile and are redirected to a page listing their full name, their username, location, high score (currently zero), how many matches they've played (zero for now), and how many games they've played (also zero). On the right, there's a box showing the current status - 5 health bars, 0 points, and 0 twinkies. Below the box, a button to resume game is greyed out. Towards the bottom of the page is a button to start a new game.
        # USER clicks to start a new game and are redirected to a gameplay page
        # Under the nav bar, there is a box showing current health, points, twinkies, nuclear (written in grey) and computer. There is also a button for how to play, under which are three images. The images for the food and the roach are animated but the bomb image is greyed out.
        # USER clicks on the button to learn how to play and a pop up appears with instructions on how to play and what each thing in the current status box means.
        # USER reads through everything and clicks ok to exit the pop up.
        # USER clicks the image showing the roach to start. After a second, a pop-up appears.
        # The pop-up shows USER's choice and opponent's choice, followed by the "effects" and who won the round. There's a choice to go to a new match.
        # USER clicks to play again and the current status box changes to say live instead of computer.
        # After a few rounds, USER reaches more than 1358 points, a pop up asks if they would like to purchase some twinkies.
        # USER clicks the button to purchase Twinkies and sees their points reduce by 1358, and 10 be added to their twinkies. The twinkie count becomes a link.
        # USER clicks on the Twinkie link to see the same popup, this time showing how many twinkies they have and asking if they would like to use or purchase twinkies. There is an exit button at the bottom.
        # USER clicks to exit and continues to play. At over 1945 points, a popup appears asking the USER if they would like to have access to the nuclear bomb.
        # USER clicks to gain access and sees their points reduce by 1945, but the nuclear bomb image becomes animated and colorful.
        # After a few more rounds, USER exits the game by clicking to log out. USER is redirected to the login/reg page.
        # The next day, USER decides to play again. When they arrive at the home page, they click to log in and the form drops down.
        # USER enters username and password and clicks on the login button again to submit the form.
        # The USER is redirected to the dashboard, where they click on profile to check that their score from the day before was saved.
        # The profile has updated to show the high score, how many matches were played, and how many games were played. It also shows their current health, score, and  twinkie count. The button to resume game is no longer greyed out.
        # USER selects the button to resume game and is redirected back to the game play page.

if __name__ == '__main__':
    unittest.main()
