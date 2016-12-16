import random
import datetime
import csv


class Policy:
	Type = 'Policy'
	policysum=0
	def __init__(self):
                Policy.policysum += 1
		self.policy_id = Policy.policysum #check existing policy and do greatest id +1
		self.user_id = random.randrange(1,1001,2) #pick one at random from the user list
		self.asset_value = random.randrange(500, 1000000,2) #pick a random asset value
		self.created_date = datetime.datetime.utcnow() #timestamp the item upon creation
		self.underwriting_company = random.randrange(1,11,2) #pick at random from the list of underwriting companies
		self.premium_per_month = random.gauss(self.asset_value*.2/12,self.asset_value*.2/12*.1) #pick a random number between 50-100,000
		self.big_risk = random.gauss(1,.25)#chance of a large claim
		self.small_risk = random.gauss(10,2) #chance of a small claim
		self.big_risk_amount = random.gauss(self.asset_value, self.asset_value*.1)#large claim amount if it happens
		self.small_risk_amount = random.gauss(self.asset_value*.1,self.asset_value*.01)#small claim amount if it happens
		


#Automated Test to see if it worked
A = Policy()

print 'type: ' + A.Type
print 'Policy id: ' + str(A.policy_id)
print 'User id: ' + str(A.user_id)
print 'Created Date: ' + str(A.created_date)
print 'Underwriting Company ' + str(A.underwriting_company)
print 'Premium Per Month: ' + str(A.premium_per_month)
print 'Asset Value: ' + str(A.asset_value)
print 'Big Risk Chance: ' + str(A.big_risk)
print 'Small Risk Chance: ' + str(A.small_risk)
print 'Big Risk Amount: ' + str(A.big_risk_amount)
print 'Small Risk Amount: ' + str(A.small_risk_amount)









#Now we need to make a list from the object that was created

datalist = []
datalist.append(A.Type)
datalist.append(A.policy_id)
datalist.append(A.user_id)
datalist.append(A.asset_value)
datalist.append(A.created_date)
datalist.append(A.underwriting_company)
datalist.append(A.premium_per_month)
datalist.append(A.big_risk)
datalist.append(A.small_risk)
datalist.append(A.big_risk_amount)
datalist.append(A.small_risk_amount)


# Now we put that list into the simdata.csv file
myfile = open('/home/josh/Desktop/Special_Projects/Random_Data_Stream/Source_Num/simdata.csv', 'a')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerow(datalist)

