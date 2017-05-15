from selenium import webdriver
webpage = "https://www.dspayments.com/evanston"

plateInfo = ['DELETED',				   # License Plate Number
			 'DELETED']				   # License Plate State, with state abbreviation in all caps (i.e. Alabama is 'AL')
driver = webdriver.Chrome()
driver.get(webpage)

sbox = driver.find_element_by_id("Plate")
sbox.send_keys(plateInfo[0])

driver.find_element_by_xpath("//select[@name='PlateStateProv']/option[@value='" + plateInfo[1] + "']").click()
submit = driver.find_element_by_class_name("search_btn")
submit.click()

alertMessage = driver.find_element_by_xpath("//*[contains(text(), 'sorry')]")

assert ('sorry' not in driver.page_source), "You have no tickets"
paymentOption = input('Want to pay the ticket(s)? Type y or n: ')

if (paymentOption == 'y'):
	submit = driver.find_element_by_id("citationPayment")
	submit.click()
	personalInfo = ['DELETED',				# 'Credit' or 'Debit'
					'DELETED',				# Expiration month with two digits (i.e. January is '01', October is '10')
					'DELETED',				# Expiration year in format YYYY
					'DELETED',				# Card type--Options are 'VISA', 'MC'(MasterCard), 'DISC' (Discover)
					'DELETED',				# Name as it appears on card
					'DELETED',				# Phone number without dashes
					'DELETED', 				# Card number
					'DELETED',				# Card security code
					'DELETED'] 				# Billing zip code

	textboxIDs = ['CardholderName',
				  'PhoneNumber',
				  'CreditCardNumber',
				  'Cvv',
				  'ZipCode']

	#take care of the select boxes for card type and expiration stuff
	driver.find_element_by_xpath("//select[@name='CardType2']/option[@value='" + personalInfo[0] + "']").click()
	driver.find_element_by_xpath("//select[@name='ExpirationMonth']/option[@value='" + personalInfo[1] + "']").click()
	driver.find_element_by_xpath("//select[@name='ExpirationYear']/option[@value='" + personalInfo[2] + "']").click()
	driver.find_element_by_xpath("//select[@name='CardType']/option[@value='" + personalInfo[3] + "']").click()

	for i in range(4, 9):
		box = driver.find_element_by_id(textboxIDs[i-4])
		box.send_keys(personalInfo[i])
	
	assurance = input('Total is ' + driver.find_element_by_id("TotalPayEdit").get_attribute('value') +', do you still want to pay? Type y or n: ')
	if (assurance == 'y'):
		driver.find_element_by_id("button submit").click()
		driver.find_element_by_id("submitbutton").click()
		print('Payment Successful')
