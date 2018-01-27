from bs4 import BeautifulSoup
import requests
import re
class PNRAPI:
	
	url_pnr = "http://www.indianrail.gov.in/cgi_bin/inet_pnrstat_cgi.cgi"
	headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"}
	
	def __init__(self,pnr=""):
		self.response_json = {}
		if len(pnr)!=10:
			raise ValueError("PNR Number has to be of 10 digits.")
		else:
			self.pnr = pnr
	
	def request(self):
		request_data = {}
		request_data["lccp_pnrno1"] = self.pnr
		request_data["submit"] = "Wait For PNR Enquiry!" #not required
		r = requests.post(PNRAPI.url_pnr,request_data,headers=PNRAPI.headers)
		if r.text.find("Please try again later") > 0:
			return False
		else:
			soup = BeautifulSoup(r.text)
			self.__getDetails(soup)
			return True
	
	def __getDetails(self,soup):
		#set pnr
		self.response_json["pnr"] = self.pnr	
		#set ticket_type
		ticket_type_re = re.compile("\(.*\)")
		enq_heading = soup.find("td",{"class":"Enq_heading"}).text
		ticket_type = str(ticket_type_re.findall(enq_heading)[0])
		ticket_type = ticket_type.lstrip("\(").rstrip("\)")
		self.response_json["ticket_type"] = ticket_type
		#get tables
		tables = soup.findAll("table",{"class":"table_border"})
		#get journey_rows
		journey_cols = tables[0].findAll("tr")[2].findAll("td")
		#get train_number
		self.response_json["train_number"] = str(journey_cols[0].text).lstrip("*")
		#get train_name
		self.response_json["train_name"] = str(journey_cols[1].text).strip()
		#get boarding_date
		boarding_date = str(journey_cols[2].text).split("-")
		boarding_date = boarding_date[0]+"-"+boarding_date[1].strip()+"-"+boarding_date[2]
		self.response_json["boarding_date"] = boarding_date
		#get from
		self.response_json["from"] = str(journey_cols[3].text).strip()
		#get to
		self.response_json["to"] = str(journey_cols[4].text).strip()
		#get reserved_upto
		self.response_json["reserved_upto"] = str(journey_cols[5].text).strip()
		#get boarding_point
		self.response_json["boarding_point"] = str(journey_cols[6].text).strip()
		#get class
		self.response_json["class"] = str(journey_cols[7].text).strip()

		#get passengers
		passengers = []
		totalPassengers = 0
		rows = tables[1].findAll("tr")
		rowLength = len(rows)
		for i in range(1,rowLength):
			cols = rows[i].findAll("td")
			if str(cols[0].text).split()[0] == "Passenger":
				totalPassengers = totalPassengers + 1
				passengerData = {}
				booking_data = str(cols[1].text).split()
				booking_status = ""
				for element in booking_data:
					booking_status = booking_status+" "+element
				booking_status = booking_status.strip()
				passengerData["booking_status"] = booking_status
				current_data = str(cols[2].text).split()
				current_status = ""
				for element in current_data:
					current_status = current_status+" "+element
				current_status = current_status.strip()
				passengerData["current_status"] = current_status
				passengers.append(passengerData)
			elif str(cols[0].text).split()[0] =="Charting":
				charting_data = str(cols[1].text).split()
				charting_status = ""
				for element in charting_data:
					charting_status = charting_status+" "+element
				charting_status = charting_status.strip()
				#get charting_status
				self.response_json["charting_status"] = charting_status
		#get total_passengers
		self.response_json["total_passengers"] = totalPassengers
		#get passenger_status
		self.response_json["passenger_status"] = passengers

	def get_json(self):
		return self.response_json